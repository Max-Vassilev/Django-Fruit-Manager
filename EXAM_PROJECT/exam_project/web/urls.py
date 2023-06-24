from django.urls import path
from .views import *

urlpatterns = [
    path("", index_page, name='index page'),
    path("dashboard/", dashboard_page, name='dashboard page'),

    path("create/", fruit_create_page, name='fruit create'),
    path("<int:fruit_id>/details/", fruit_details, name='fruit details'),
    path("<int:fruit_id>/edit/", fruit_edit, name='fruit edit'),
    path("<int:fruit_id>/delete/", fruit_delete, name='fruit delete'),

    path("profile/create", profile_create_page, name='profile create'),
    path("profile/details", profile_details_page, name='profile details'),
    path("profile/edit", profile_edit_page, name='profile edit'),
    path("profile/delete", profile_delete_page, name='profile delete'),

]

