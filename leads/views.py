from django.db.models.query import QuerySet
from django.shortcuts import render,redirect,resolve_url
from django.http import HttpResponse
from .form import LeadForm,LeadModelForm,CustomUserCretionForm
from django.core.mail import send_mail
from .models import Agent, Lead
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm

#! Signup
class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCretionForm

    def get_success_url(self):
        return resolve_url("login")


#! Landing Page 
 
#* Leading Page in Genegric Template 
class LandingPageView(TemplateView):
    template_name = "landing.html"


#? Landing Page in Functional Component 
def Landing_Page(request):
    return render(request,'landing.html')

###########################################################################################################

#! Leads List 

#* Leads List in Genegric Template 

class LeadListViews(ListView):
    template_name='leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = 'leads' # By Default it is object_list


#? Leads List in Functional Component 

def lead_list(request):
    leads = Lead.objects.all()
    context={
        "leads":leads
    }
    return render(request,"leads/lead_list.html",context)


####################################################################################################################

#! Leads Detail 

#* Leads Detail  in Genegric Template 
class LeadDetailView(DetailView):
    template_name="leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name='lead'

#? Leads Detail  in Functional Component 
def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context={
        'lead':lead
    }
    return render(request,"leads/lead_detail.html",context)


###################################################################################################################

#! Leads Create 

#* Leads Create  in Genegric Template 
class LeadCreateView(CreateView):
    template_name='leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self):
        return resolve_url("leads:lead-list")

    def form_valid(self, form):
        # TODO Send Email

        send_mail(
            subject="A New Lead Has Been Created",
            message="Go To Site to see the new Lead",
            from_email="testing@testAnu.com",
            recipient_list=["testing@testAnu2.com"]
        )
        return super(LeadCreateView,self).form_valid(form)


#? Leads Create  in Functional Component 


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        print('Reaciving A post Request')
        form = LeadModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/leads")

    context = {
        'form':form
    }
    return render(request,'leads/lead_create.html',context)

# def lead_create(request):
    # form = LeadForm()
    # if request.method == 'POST':
    #     print('Reaciving A post Request')
    #     form = LeadForm(request.POST)

    #     if form.is_valid():
    #         print('The Form Is Valid')
    #         print(form.changed_data)
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = Agent.objects.first()

    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent
    #         ) 
    #         print('New Lead Is Created')
    #         return redirect("/leads")

#     context = {
#         'form':form
#     }
#     return render(request,'leads/lead_create.html',context)

################################################################################################################


#! Leads Update

#* Leads Update  in Genegric Template 

class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return resolve_url('leads:lead-list')

#? Leads Update  in Functional Component 

def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        print('Reaciving A post Request')
        form = LeadModelForm(request.POST,instance=lead)

        if form.is_valid():
            form.save()
            return redirect("/leads")
    context ={
        'form':form,
        'lead':lead
    }
    return render(request,'leads/lead_update.html',context)


# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == 'POST':
#         print('Reaciving A post Request')
#         form = LeadForm(request.POST)

#         if form.is_valid():
#             print('The Form Is Valid')
#             print(form.changed_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age

#             lead.save()
         
#             print('New Lead Is Created')
#             return redirect("/leads")

#     context={
#         'lead':lead,
#         'form':form
#     }
#     return render(request,'leads/lead_update.html',context)

########################################################################################################################################

#! Lead Delete 

#* Lead Delete in Generic Templates 
class LeadDeleteView(DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return resolve_url('leads:lead-list')

#? Lead Delete in Functional Component

def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

 #######################################################################################################################################