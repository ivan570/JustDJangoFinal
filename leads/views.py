from email import message
from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Agent, Lead
from .form import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, "landing.html")


class LeadListView(LoginRequiredMixin, ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_list(request):
    # return HttpResponse("Hello World")
    # return render(request=request, template_name='leads/home_page.html')
    context = {
        'leads': Lead.objects.all()
    }
    return render(request, 'leads/lead_list.html', context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = 'leads/lead_details.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_details(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        'lead': lead
    }
    return render(request, 'leads/lead_details.html', context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('lead-list')

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A lead has been created", 
            message="GO to the site to see the new lead", 
            from_email='test@test.com', 
            recipient_list=['test2@test.com', 'ivankshu@gmail.com']
        )
        return super(LeadCreateView, self).form_valid(form)


def lead_create(request: HttpRequest):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('lead-list')


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)

    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        'form': form,
        'lead': lead
    }
    return render(request, 'leads/lead_update.html', context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('lead-list')


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()

#     if request.method == "POST":
#         print("thank you for reqeusting a POST method")
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             print('form is valid')
#             print(form.cleaned_data)

#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']

#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age

#             # committing the model
#             lead.save()

#             return redirect("/leads")

#     context = {
#         'form': form,
#         'lead': lead
#     }
#     return render(request, 'leads/lead_update.html', context)


# def lead_create(request: HttpRequest):
#     form = LeadModelForm()
#     if request.method == "POST":
#         print("thank you for reqeusting a POST method")
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             print('form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = form.cleaned_data['agent']
#             Lead.objects.create(first_name=first_name,
#                                 last_name=last_name, age=age, agent=agent)
#             return redirect("/leads")
#     context = {
#         'form': form
#     }
#     return render(request, 'leads/lead_create.html', context)
