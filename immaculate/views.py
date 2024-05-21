from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.views.generic import FormView
from django.template import loader
# from unittest import loader, result
from nexus.forms import (
    ContactForm
)
from nexus.mixins import(
    AjaxFormMixin, 
    reCAPTCHAValidation     
)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# Create your views here.
def home(request):
    return render(request,'home.html')

def events(request):
    return render(request,'events.html')

class ContactFormView(AjaxFormMixin,FormView):    
    form_class = ContactForm
    template_name = 'contacts.html'
    success_url='/contact-success/'    

    def form_valid(self, form):        
        response = super(AjaxFormMixin, self).form_valid(form)        
        if is_ajax(request=self.request): 
            # token = form.cleaned_data.get('token')
            # captcha = reCAPTCHAValidation(token)
            # if captcha["success"]:
                context = {
                    'name': form.cleaned_data['full_name'],
                    'subject': form.cleaned_data['subject'],
                    'email': form.cleaned_data['email'],
                    'email_message': form.cleaned_data['message'],
                }
                template = loader.get_template('contact_email.txt')
                message= template.render(context)
                email = EmailMultiAlternatives(
                    "{} from {}".format(form.cleaned_data['subject'],form.cleaned_data['full_name']),message,
                    "{} sent a message".format(form.cleaned_data['full_name']) ,
                    [settings.EMAIL_HOST_USER]
                )

                email.content_subtype = 'html'
                email.send()
                messages.success(self.request, 'Your message has been received. We will reach out shortly')                    
                # print(form.cleaned_data) 
                form = ContactForm()                   
                return JsonResponse(context)                
        else:
            return response

def contactPush(request): 
    contactForm = ContactForm(request.POST)

    return HttpResponseRedirect('/contact')   

    
def courses(request):
    return render(request,'courses.html')

def admissions(request):
    return render(request,'admissions.html')

def about(request):
    return render(request,'about.html')