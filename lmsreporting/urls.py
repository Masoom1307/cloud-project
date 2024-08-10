from django.urls import path
from . import views 
app_name = 'lmsreporting' 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [ 

    path('', views.home, name = 'home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('modules/', views.modules, name='modules'),
    path('issues/', PostListView.as_view(), name = 'report'),
    path('issues/<int:pk>', PostDetailView.as_view(), name = 'issue-detail'),
    path('issues/new', PostCreateView.as_view(), name = 'issue-create'),
    path('issues/<int:pk>/update/', PostUpdateView.as_view(), name = 'issue-update'),
    path('issues/<int:pk>/delete/', PostDeleteView.as_view(), name = 'issue-delete'),

]