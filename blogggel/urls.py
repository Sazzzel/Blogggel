from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
    path('delete_testimonial/<int:testimonial_id>/', views.testimonial_delete, name='testimonial_delete'),
    path('edit_testimonial/<int:testimonial_id>/', views.testimonial_edit, name='testimonial_edit'),
    path('add_testimonial/', views.testimonial_add, name='testimonial_add'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    
]