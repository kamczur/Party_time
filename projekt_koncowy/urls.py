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
                           PartiesListView, AddGiftView, GiftsListView, DeleteGiftView, DeletePartyView, EditPartyView, PartyDetailsView,
                           GuestsView, LastPageView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="homepage"),
    path('register/', register_request, name="register"),
    path('login/', login_request, name="login"),
    path('logout/', logout_request, name="logout"),
    path('add_party/', AddParty.as_view(), name="add-party"),
    path('party_list/', PartiesListView.as_view(), name="party-list"),
    path('add_gift/', AddGiftView.as_view(), name="add-gift"),
    path('gifts_list/', GiftsListView.as_view(), name="gifts-list"),
    path('gift_delete/<int:gift_id>/', DeleteGiftView.as_view(), name="delete-gift"),
    path('party_delete/<int:party_id>/', DeletePartyView.as_view(), name="delete-party"),
    path('party_edit/<int:party_id>/', EditPartyView.as_view(), name="edit-party"),
    path('party_details/<int:party_id>/', PartyDetailsView.as_view(), name="party-details"),
    path('guests/<party_id>/', GuestsView.as_view(), name="guests"),
    path('last_page/<party_id>/', LastPageView.as_view(), name="last-page"),
]
