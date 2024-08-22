from django.urls import path
from .views import (
    home, about, contact, contact_submit, modules_view, module_register,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView,
    user_profile_view  # Make sure this is correctly imported
)

app_name = 'lmsreporting'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('contact/submit/', contact_submit, name='contact_submit'),
    path('modules/', modules_view, name='modules'),
    path('modules/register/<int:pk>/', module_register, name='module-register'),
    path('issues/', PostListView.as_view(), name='report'),
    path('issues/<int:pk>/', PostDetailView.as_view(), name='issue-detail'),
    path('issues/new/', PostCreateView.as_view(), name='issue-create'),
    path('issues/<int:pk>/update/', PostUpdateView.as_view(), name='issue-update'),
    path('issues/<int:pk>/delete/', PostDeleteView.as_view(), name='issue-delete'),
    path('issues/<str:username>/', UserPostListView.as_view(), name='user-issues'),
    path('user/<int:pk>/', user_profile_view, name='user-profile'),  # Updated to user_profile_view
]
