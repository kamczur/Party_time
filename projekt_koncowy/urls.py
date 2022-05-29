"""projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from imprezy.views import (register_request, homepage, login_request, logout_request, AddParty,
                           PartiesListView, AddGift, DeletePartyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('register/', register_request, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
    path('add_party/', AddParty.as_view(), name="add-party"),
    path('party_list/', PartiesListView.as_view(), name="party-list"),
    path('add_gift/', AddGift.as_view(), name="add-gift"),
    path('party_delete/<int:party_id>/', DeletePartyView.as_view(), name="delete-party"),
]
