
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from Profile.forms import SignUpForm, LoginForm, GroupCreationForm
from django.contrib.auth.forms import AuthenticationForm
from Profile.models import UserInfo, MyGroup, FormedGroup, SHOPS
from django.http import Http404, HttpResponsePermanentRedirect
from Cal.models import Event
from django.urls import reverse
def welcome(request):
    return render(request,'(welcome).html')
def signup_view(request):
    next = request.GET.get('next')
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        if next:
            return redirect(next)
        val = 35
        return render(request, 'homepage.html', {'val': val})

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)
def login_view(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        val = 35
        return render(request, 'homepage.html', {'val': val})

    context = {
        'form': form,
    }
    return render(request, "login.html", context)
def profile_view(request):
    data = get_user_model()
    val = 2    
    return render(request, 'profile.html', {'data': data, 'val':val})
def logout_view(request):
    logout(request)
    return render(request, 'welcome.html')

def create_group_view(request):
    next = request.GET.get('next')
    group = GroupCreationForm(request.POST or None)
    if group.is_valid():
        #group = group.save(commit=False)
        addshopthing = group.cleaned_data.get('addshop')
        if addshopthing != "":
            SHOPS.append((addshopthing, addshopthing))
            group.shopId = addshopthing
        group.save()
        response = 'Refresh the page by clicking groups to join the new group'
        if next:
            return redirect(next)
        val = 2
        return render(request, 'grouplist.html', {'response': response, 'val':val})
    context = {
        'group': group,
    }
    return render(request, "creategroup.html", context)
def join_group_view(request, group_id):
    try:
        group = MyGroup.objects.get(groupId=group_id)
        current_user = request.user
        get_user_db = FormedGroup.objects.filter(userEmail= request.user.email)
        try: 
            get_user_db[0]
            response = f'{request.user.username} already exist in a group'
        except IndexError:
            new_group_member = FormedGroup(userEmail= current_user, userGroupID= group)
            new_group_member.save()
            response = f'You are now in {group.groupName}. Go to Calendar and Grocery List for more.'
    except MyGroup.DoesNotExist:
        raise Http404("group not found")
        response = ""
    val = 2
    return render(request, "profile.html", {'response': response, 'val':val})
def display_groups(request):
    groups = MyGroup.objects.all()
    try: 
        groups[0]
        response = 'These are current groups'
    except IndexError:
        response = 'There are no groups currently.'
    val = 2
    return render(request, "grouplist.html", {'groups':groups, 'response':response, 'val':val})

def check_calendar(request):
    user_email = request.user.email
    try:
        get_user_group_formed = FormedGroup.objects.get(userEmail=user_email)
        #group_id = get_user_group_formed.userGroupID
        #ggroup = group_id.groupId
        #group = MyGroup.objects.get(groupId=ggroup)
        return redirect('cal/calendar/')
    except FormedGroup.DoesNotExist:
        response = "You haven't joined a group. Join a group to see its calendar."
        val = 2
        return redirect(reverse('failed', args=(response,)))

def welcome_redirect(request):
    return HttpResponsePermanentRedirect("/welcome/")

def homepage_view(request):
    val = 35
    return render(request, 'homepage.html', {'val':val})
def about_view(request):
    return render(request, 'GropoolAbout.html')