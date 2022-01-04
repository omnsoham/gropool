"""gropool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from Profile.views import welcome, signup_view, profile_view, login_view, display_groups, create_group_view, join_group_view, check_calendar, welcome_redirect, homepage_view, about_view
from _List.views import check_grocery_list, display_lists, create_list, create_listitem, delete_list, delete_listitem, failed, edit_listitem
urlpatterns = [
    url('admin/', admin.site.urls),
    url('login/', login_view, name='login'),
    url('welcome/',welcome, name="welcome"),
    path('',welcome_redirect, name="welcomeredirect"),
    url('signup/', signup_view, name="signup"),
    url('profile/', profile_view, name="profile"),
    path('check_calendar/cal/', include('Cal.urls')),
    url('groups/', display_groups, name="displayGroups"),
    url('create_group/', create_group_view, name ='creategroup'),
    path('join_group/<int:group_id>/', join_group_view, name ='joingroup'),
    path('check_calendar/', check_calendar, name = "checkcalendar"),
    path('check_grocery_list/', check_grocery_list, name= "checkgrocerylist"),
    path('check_grocery_list/lists/', display_lists, name= "list"),
    path('create_list/', create_list, name= "createlist"),
    path('create_listitem/', create_listitem, name= "createlistitem"),
    path('delete_list/', delete_list, name= "delete_list"),
    path('delete_listitem/', delete_listitem, name= "delete_listitem"),
    path('failed/<arg1>', failed, name= "failed"),
    path('edit_listitem/', edit_listitem, name= "edit_listitem"),
    url('homepage/', homepage_view, name="homepage"),
    url('about/', about_view, name="about"),


]
from django.conf.urls.static import static
from gropool import settings
