from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .forms import ContactForm

from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    context = {
        'title': "This is the homepage."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': "This is the contact page.",
        'content': "Welcome to the contact page.",
        'form': contact_form,

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json[')

    return render(request, "contact/view.html", context)


