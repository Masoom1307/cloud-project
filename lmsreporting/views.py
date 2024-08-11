from django.shortcuts import render
from django.http import HttpResponse
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic.edit import DeleteView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.
def home(request): 

    return render(request, 'lmsreporting/home.html', {'title': 'Welcome'})

def about(request): 

    return render(request, 'lmsreporting/about.html', {'title': 'About'})


def contact(request): 

    return render(request, 'lmsreporting/contact.html', {'title': 'Contact'})


def modules(request): 

    return render(request, 'lmsreporting/modules.html', {'title': 'Modules'})


def report(request):
   
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}
    return render(request, 'lmsreporting/report.html', daily_report)

class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'lmsreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination

class UserPostListView(ListView): 

    model = Issue
    template_name = 'lmsreporting/user_issues.html' 
    context_object_name = 'issues'
    paginate_by = 5


    def get_queryset(self):

        user=get_object_or_404(User, username=self.kwargs.get('username'))

        return Issue.objects.filter(author=user).order_by('-date_submitted')


class PostDetailView(DetailView):
    model = Issue
    template_name = 'lmsreporting/issue_detail.html'

    
class PostCreateView(LoginRequiredMixin, CreateView):

    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 

        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 

    model = Issue

    fields = ['type', 'room', 'details']
    
    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Issue

    success_url = '/issues'
    
    def test_func(self):

        issue = self.get_object()

        return self.request.user == issue.author




