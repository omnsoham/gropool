from django.shortcuts import render, redirect
from Profile.models import FormedGroup, MyGroup, UserInfo
from _List.models import MyList, MyListItems
from _List.forms import ListItemForm, EditItemForm
from django.urls import reverse
# Create your views here.
def check_grocery_list(request):
    user_email = request.user.email
    try:
        get_user_group_formed = FormedGroup.objects.get(userEmail=user_email)
        group_id = get_user_group_formed.userGroupID
        ggroup = group_id.groupId
        group = MyGroup.objects.get(groupId=ggroup)
        return redirect('lists/')
    except FormedGroup.DoesNotExist:
        response = "You haven't joined a group. Join a group to see its grocery lists."
        val = 2
        return redirect(reverse('failed', args=(response,)))

def display_lists(request):
    user_email = request.user.email
    get_user_group_formed = FormedGroup.objects.get(userEmail=user_email)
    group_id = get_user_group_formed.userGroupID
    ggroup = group_id.groupId
    group = MyGroup.objects.get(groupId=ggroup)
    thatlists = MyList.objects.filter(listGroupId= group)
    list_dictionary = {}
    if len(thatlists) > 0: 
        response = "These are your group's lists"
        for list in thatlists:
            variable = []
            li = MyListItems.objects.filter(listMaster= list)
            if len(li) > 0:
                for i in li:
                    variable.append(i.listItemName)
            else:
                variable.append("This list is empty")
            list_dictionary[list.listName] = variable
            val = 2
    else:
        response = "Your group hasn't made any lists currently."
        val = 2
    return render(request, "displaylists.html", {'list_dictionary':list_dictionary, 'response':response, 'val':val})

def create_listitem(request):
    user = UserInfo.objects.get(email = request.user.email)
    form = ListItemForm(request.POST or None)
    try:
        userlist = MyList.objects.get(listCreator= user)
        if request.POST and form.is_valid():
            itemName = form.cleaned_data['listItemName']
            new = MyListItems(listMaster= userlist, listItemName= itemName)
            new.save()
            return redirect(display_lists)
    except MyList.DoesNotExist:
        response = "You can't create a list item in YOUR non-existant list"
        return redirect(reverse('failed', args=(response,)))
    return render(request, 'listform.html', {'form': form})

def create_list(request):
    user_email = request.user.email
    get_user_group_formed = FormedGroup.objects.get(userEmail=user_email)
    group_id = get_user_group_formed.userGroupID
    ggroup = group_id.groupId
    group = MyGroup.objects.get(groupId=ggroup)
    check_created = MyList.objects.filter(listCreator= request.user.email)
    user = UserInfo.objects.get(email = request.user.email)
    try:
        check_created[0]
        response = "You already created your grocery list"
        val = 2
        return render(request, 'allreadycreated.html', {'response': response, 'val':val})
    except IndexError:
        list = MyList(listGroupId= group, listCreator= user, listName= f"{request.user.username}'s Grocery List")
        list.save()
        return redirect(display_lists)
def delete_listitem(request):
    user = UserInfo.objects.get(email = request.user.email)
    userlist = MyList.objects.filter(listCreator= user)
    form = ListItemForm(request.POST or None)
    if len(userlist) == 1:
        userlist = MyList.objects.get(listCreator= user)
        if request.POST and form.is_valid():
            itemName = form.cleaned_data['listItemName']
            try:
                old = MyListItems.objects.get(listMaster= userlist, listItemName= itemName)
                old.delete()
                return redirect(display_lists)
            except MyListItems.DoesNotExist:
                response = "The list item you specified isn't existing, or you made two similar entrees. Edit one to delete the other"
                return redirect(reverse('failed', args=(response,)))
    else:
        response = "You can't delete a list item from YOUR non-existant list"
        return redirect(reverse('failed', args=(response,)))
    return render(request, 'listform.html', {'form': form})

def delete_list(request):
    user = UserInfo.objects.get(email = request.user.email)
    userlist = MyList.objects.filter(listCreator= user)
    if len(userlist) > 0:
        userlist.delete()
        return redirect('/profile/')
    else:
        response = "You can't delete a non-existant list"
        return redirect('/failed/<response>')
def edit_listitem(request):
    user = UserInfo.objects.get(email = request.user.email)
    userlist = MyList.objects.filter(listCreator= user)
    form = EditItemForm(request.POST or None)
    if len(userlist) == 1:
        userlist = MyList.objects.get(listCreator= user)
        if request.POST and form.is_valid():
            itemName = form.cleaned_data['listItemName']
            editedName = form.cleaned_data['EditItemName']
            try:
                old = MyListItems.objects.filter(listMaster= userlist, listItemName= itemName)
                old.update(listItemName = editedName)
                for object in old:
                    object.save()
                return redirect(display_lists)
            except MyListItems.DoesNotExist:
                response = "The list item you specified isn't existing, or you made two similar entrees. Edit one to delete the other"
                return redirect(reverse('failed', args=(response,)))
    else:
        response = "You can't edit a list item from YOUR non-existant list"
        return redirect(reverse('failed', args=(response,)))
    return render(request, 'editform.html', {'form': form})
def failed(request, arg1):
    response = arg1
    val = 2
    return render(request, 'itemfailed.html', {'response': response, 'val':val})
