from django import forms
from django.forms import ModelForm
from Profile.models import UserInfo, MyGroup
from django.contrib.auth import (
    authenticate,
    get_user_model

)
class SignUpForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
     #   super(SignUpForm, self).__init__(*args, **kwargs)
      #  self.fields['username'].widget.attrs.update({
       #     'class': 'myform'
        #})
        #for fieldname, field in self.fields.items():
         #   field.widget.attrs.update({
          #      'class': 'yeetform'
           # })
    class Meta:
        model = UserInfo
        fields = [
            'username',
            'password',
            'email',
            'zipcode'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your email'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Enter your zipcode'}),
            
        }
        labels = {
        "username": "Username"
        }
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(SignUpForm, self).clean(*args, **kwargs)
User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = MyGroup
        fields = [
            'groupName',
            'groupDescription',
            'dayOfDelivery',
            'shopId',
            'addshop',
            'zipcode',
        ]
        widgets = {
            'groupName': forms.TextInput(attrs={'placeholder': 'Enter group name','class': 'form-control'}),
            'groupDescription': forms.TextInput(attrs={'placeholder': 'Enter group description','class': 'form-control'}),
            'addshop': forms.TextInput(attrs={'placeholder': 'Add and select here', 'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'Enter group zipcode','class': 'form-control'}),
        }
    def clean(self, *args, **kwargs):
        groupName = self.cleaned_data.get('groupName')
        groupName_qs = MyGroup.objects.filter(groupName=groupName)
        if groupName_qs.exists():
            raise forms.ValidationError(
                "This group has already been registered")
        return super(GroupCreationForm, self).clean(*args, **kwargs)