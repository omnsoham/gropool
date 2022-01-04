from django import forms
from django.forms import ModelForm
from _List.models import MyListItems
from django.contrib.auth import (
    authenticate,
    get_user_model
)
class ListItemForm(ModelForm):
  class Meta:
    model = MyListItems
    fields = [
        'listItemName',
      ]
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'listItemName': forms.TextInput(attrs={'placeholder': 'Your list item'}),
    }

class EditItemForm(forms.Form):  
    listItemName = forms.CharField(label= 'List Item To Select', required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your existing list item'}))
    EditItemName = forms.CharField(label= 'Edit Item', required=True, widget=forms.TextInput(attrs={'placeholder': 'Edit your list item here'}))

    