from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Contact
# Create your views here.
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def display_contacts(request):
  mycontacts = Contact.objects.all().values()
  template = loader.get_template('all_contacts.html')
  context = {
    'mycontacts': mycontacts,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mycontacts = Contact.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mycontacts': mycontacts,
  }
  return HttpResponse(template.render(context, request))

def add_contact(request):
    #template = loader.get_template('add.html')
    if request.method == 'POST':
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        ph = int(request.POST.get('ph', ''))
        contact=Contact(firstname=fname,lastname=lname,phone=ph)
        contact.save()
        return redirect(display_contacts)
    
    return render(request, 'add.html')

def update_contact(request,id):
   mycontact = Contact.objects.get(id=id)
   template = loader.get_template('update.html')
   context = {
    'mycontact': mycontact,
   }
   if request.method == 'POST':
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    ph = int(request.POST.get('ph', ''))
    mycontact.firstname=fname
    mycontact.lastname=lname
    mycontact.phone=ph
    mycontact.save()
    return redirect(display_contacts)
   return HttpResponse(template.render(context, request))

def delete_contact(request,id):
   mycontact = Contact.objects.get(id=id)
   mycontact.delete()
   return redirect(display_contacts)