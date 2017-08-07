"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^settings/',views.settings),
    url(r'^add_category$',views.add_category),
    url(r'^delete_category/(?P<category>\w+)',views.deleteCategory),#()代表如果match到 ,\w+一到多個文字,  符合就取出,category這個東西就可以直接被使用
    url(r'^add_record$',views.add_Record),
    url(r'^delete_record$',views.deleteRecord),
]
