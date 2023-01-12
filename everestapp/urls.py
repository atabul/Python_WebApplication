from django.urls import path
from .views import *
app_name = "everestapp"

urlpatterns = [
    path("", ClientHomeView.as_view(), name ="clienthome"),
    path("about/", ClientAboutView.as_view(), name="clientabout"),
    path("news/", ClientNewsView.as_view(), name="clientnews"),
    path("news/<int:pk>/detail/", ClientNewsDetailView.as_view(), name="clientnewsdetail"),
    path("news/create/",ClientNewsCreateView.as_view(),name="clientnewscreate"),
    path("news/update/<int:pk>/",ClientNewsUpdateView.as_view(),name="clientnewsupdate"),
    path("news/delete/<int:pk>/",ClientNewsDeleteView.as_view(),name="clientnewsdelete"),
    path("admin/login/",AdminLoginView.as_view(), name="adminlogin"),
    path("admin/logout/",AdminLogoutView.as_view(), name="adminlogout")



]