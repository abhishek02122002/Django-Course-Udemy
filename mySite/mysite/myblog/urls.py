from django.urls import path,include

from . import views 
urlpatterns = [
    path("",views.starting_page, name="starting-page"),
    path("posts/",views.all_posts, name="all-posts" ),
    path("post/<slug:slug>/",views.post_details,name="post-details"),
]
