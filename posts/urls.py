from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.posts_list,name="list"),
    path('new-post/',views.post_new,name="new-post"),
    path('<slug:slug>',views.post_page,name="page"),
    path('update/<slug:slug>', views.update_post, name='update'),
    path('delete/<slug:slug>', views.delete_post, name='delete'),
    path('comment/<slug:slug>', views.create_comment, name="comment"),
]