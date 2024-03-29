from django.shortcuts import render

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    context = {
       'contacts': contacts,
   }

    return render(
        request,
        'contact/index.html',
         context
    )

def contact(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)
    context = {
       'contacts': single_contact,
   }

    return render(
        request,
        'contact/contact.html',
         context
    )