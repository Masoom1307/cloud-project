from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Issue, Module, Student

# Home view
def home(request):
    return render(request, 'lmsreporting/home.html', {'title': 'Welcome'})

# About view
def about(request):
    return render(request, 'lmsreporting/about.html', {'title': 'About'})

# Contact page view
def contact(request):
    return render(request, 'lmsreporting/contact.html', {'title': 'Contact'})

# Contact form submission handling
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Process the form data, save to a model, or send an email
        messages.success(request, 'Thank you for your message!')
        return redirect('lmsreporting:contact')
    return redirect('lmsreporting:contact')

# View for issue detail
def issue_detail_view(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'lmsreporting/issue_detail.html', {'issue': issue})

# View for module list
def module_list_view(request):
    modules = Module.objects.all()
    return render(request, 'lmsreporting/module_list.html', {'modules': modules})

# View for user profile (replaces the previous student_profile_view)
def user_profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'lmsreporting/user_profile.html', {'user': user})

# View for listing modules
def modules_view(request):
    modules = Module.objects.all()
    return render(request, 'lmsreporting/modules.html', {'modules': modules, 'title': 'Modules'})

# View for module registration/unregistration
@login_required  # Ensure user is logged in to register/unregister for a module
def module_register(request, pk):
    module = get_object_or_404(Module, pk=pk)
    user = request.user

    try:
        # Get the Student instance associated with the logged-in user
        student = Student.objects.get(user=user)
    except Student.DoesNotExist:
        messages.error(request, "You are not registered as a student.")
        return redirect('lmsreporting:modules')

    # Register or unregister the student in the module
    if student in module.registered_students.all():
        module.registered_students.remove(student)
        messages.success(request, f'You have successfully unregistered from {module.title}.')
    else:
        module.registered_students.add(student)
        messages.success(request, f'You have successfully registered for {module.title}.')

    return redirect('lmsreporting:modules')

# View for listing all reported issues
def report(request):
    issues = Issue.objects.all()
    return render(request, 'lmsreporting/report.html', {'issues': issues, 'title': 'Issues Reported'})

# Class-based view for listing all issues
class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'lmsreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination

# Class-based view for listing issues by a specific user
class UserPostListView(ListView):
    model = Issue
    template_name = 'lmsreporting/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Issue.objects.filter(author=user).order_by('-date_submitted')

# Class-based view for viewing issue details
class PostDetailView(DetailView):
    model = Issue
    template_name = 'lmsreporting/issue_detail.html'

# Class-based view for creating a new issue
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class-based view for updating an issue
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author

# Class-based view for deleting an issue
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = reverse_lazy('lmsreporting:report')

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author

# Inline form for Module creation and update
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title', 'code', 'credit', 'category', 'description', 'availability', 'allowed_courses']

# Class-based view for creating a new module
class ModuleCreateView(LoginRequiredMixin, CreateView):
    model = Module
    form_class = ModuleForm
    template_name = 'lmsreporting/module_form.html'
    success_url = reverse_lazy('lmsreporting:modules')

# Class-based view for updating a module
class ModuleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Module
    form_class = ModuleForm
    template_name = 'lmsreporting/module_form.html'
    success_url = reverse_lazy('lmsreporting:modules')

    def test_func(self):
        return self.request.user.is_superuser  # Only superusers can update modules

# Class-based view for deleting a module
class ModuleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Module
    success_url = reverse_lazy('lmsreporting:modules')

    def test_func(self):
        return self.request.user.is_superuser  # Only superusers can delete modules
