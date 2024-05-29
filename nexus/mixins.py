from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
import json
import datetime
from humanfriendly import format_timespan
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def is_ajax(request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def FormErrors(*args):
	'''
	Handles form error that are passed back to AJAX calls
	'''
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message

def reCAPTCHAValidation(token):

	''' reCAPTCHA validation '''
	result = requests.post(
		'https://www.google.com/recaptcha/api/siteverify',
		data={
		 	'secret': settings.G_CAPTCHA_S_KEY,
			'response': token
		})

	return result.json()

def RedirectParams(**kwargs):
	'''
	Used to append url parameters when redirecting users
	'''
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response

class AjaxFormMixin(object):

	'''
	Mixin to ajaxify django form - can be over written in view by calling form_valid method
	'''

	def form_invalid(self, form):
		response = super(AjaxFormMixin, self).form_invalid(form)
		if is_ajax(request=self.request):
			message = FormErrors(form)
			return JsonResponse({'result':'Error', 'message': message})
		return response

	def form_valid(self, form):
		response = super(AjaxFormMixin, self).form_valid(form)
		if is_ajax(request=self.request):
			# form.save()
			return JsonResponse({'result':'Success', 'message': ""})
		return response

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)