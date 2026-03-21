from django.urls import path
from .views import signup, entry_list, create_entry, entry_detail, edit_entry, delete_entry

urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('entries/new/', create_entry, name='create_entry'),
    path('entries/<int:id>/', entry_detail, name='entry_detail'),
    path('entries/<int:id>/edit/', edit_entry, name='edit_entry'),
    path('entries/<int:id>/delete/', delete_entry, name='delete_entry'),
    path('signup/', signup, name='signup'),
]
