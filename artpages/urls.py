from django.urls import path
from .views import AboutPageView,  get_name, create_contact_info, create_new_book, list_of_book

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("name/", get_name, name="name"),  # new
    path("", create_contact_info, name='home'),
    path("newbook/", create_new_book, name='newbook'),
    path("homebook/", list_of_book, name='homebook'),
]