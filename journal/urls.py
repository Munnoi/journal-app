from django.urls import path
from .views import signup, entry_list, create_entry, entry_detail

urlpatterns = [
    path('', entry_list, name='entry_list'),
    path('entries/new/', create_entry, name='create_entry'),
    path('entries/<int:id>/', entry_detail, name='entry_detail'),
    path('signup/', signup, name='signup'),
]
