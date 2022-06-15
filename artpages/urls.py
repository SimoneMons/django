from django.urls import path
from .views import AboutPageView,  get_name, create_contact_info

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("name/", get_name, name="name"),  # new
    path("", create_contact_info, name='home'),
]