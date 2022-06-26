from django.shortcuts import render,redirect
from .models import Information
from django.http import HttpResponseRedirect
from .forms import InfromationForm
        
        
def Contacts(request):
    contacts = Information.objects.all()
    query = request.GET.get('search')
    if query:
        # findcontact = contact.filter(name__icontains=query)
        # findcontact = 
        find =Information.objects.filter(fname__regex=query)
        return render(request,'contacts.html',{'result':find})
            
    if request.method =="POST":
        info = Information()
                    
        info.fname = request.POST['fname']
        info.lname = request.POST['lname']
        info.email = request.POST['email']
        info.phoneNumber = request.POST['phoneNumber']                 
        
        info.save()
        return HttpResponseRedirect("/")
                    
    return render(request,'contacts.html',{'contacts':contacts})
        
        
        
        
def delete_contact(request,contact_id):
    Information.objects.get(id=contact_id).delete()
    return HttpResponseRedirect("/")
def edit_contact(request,contact_id):
    if request.method == "GET":
        info = Information.objects.get(pk=contact_id)
        form = InfromationForm(instance=info)
        return render(request, "editcontect.html", {'form': form})   
    else:
        if id == 0:
        
            form = InfromationForm(request.POST)
        else:
            employee = Information.objects.get(pk=contact_id)
            form = InfromationForm(request.POST,instance= employee)
            if form.is_valid():        
                form.save()
            return redirect('/')    
    return render(request, "editcontect.html")       
        
        
def  SearchContact(request):
    contact = Information.objects.all()
    print(contact)
    return render(request,'contacts.html')
