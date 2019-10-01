from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth import *
from django.shortcuts import *
from . import views
from urllib import request
from .models import *
import requests 
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from FarmCorner.forms import *
from datetime import *
from django.db.models import Q
from django.views.decorators.cache import cache_control
import datetime
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa 
from .utils import *
from datetime import *
from dateutil import parser
# Create your views here..

# Home page 
def home(request):
      plist= uploadequip.objects.all()
      context={
            'plist':plist
      }
      return render(request, 'home.html',context)

# Farmer Registration 

def farmerregis(request):
    a= districts.objects.all()
    if request.method=="POST":      
      name= request.POST.get('name','')   
      address= request.POST.get('address','')
      mobileno= request.POST.get('mobileno','')
      dist= request.POST.get('dist','')
      taluka= request.POST.get('taluka','')
      city= request.POST.get('city','')    
      email1= request.POST.get('email','')
      area= request.POST.get('area','')
      pincode= request.POST.get('pincode','')      
      password= request.POST.get('password','')   
      password1= request.POST.get('password1','')  

  # check mobile number and email already exist or not!
      if password==password1:
            # mobile number and email check
        if eholder.objects.filter(email=email1).exists():
          if eholder.objects.filter(Mobileno=mobileno).exists():
            messages.warning(request,'mobile number and Email already exists as a Equipmentholder!') 
            return render(request,'registration/fregis.html')             
          else:
              messages.warning(request,'Email already exists as a Equipmentholder!') 
          return render(request,'registration/fregis.html') 
       
          # mobile number and email check
        elif traderreg.objects.filter(email=email1).exists():
          if traderreg.objects.filter(Mobileno=mobileno).exists():
              messages.warning(request,'mobile number and Email already exists as a Trader!') 
              return render(request,'registration/fregis.html')             
          else:
              messages.warning(request,'Your email already exists as a Trader! please enter another email!') 
          return render(request,'registration/fregis.html') 

          # mobile number and email check              
        elif Farmerreg.objects.filter(email=email1).exists():
           if Farmerreg.objects.filter(Mobileno=mobileno).exists():
                  messages.warning(request,'mobile number and Email already exists as a Farmer!')  
                  return render(request,'registration/fregis.html')            
           else:
              messages.warning(request,'Your email already exists as a  Farmer! please enter another email!') 
           return render(request,'registration/fregis.html')  

          # mobile number check
        elif Farmerreg.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Farmer!')
              return render(request,'registration/fregis.html') 
        elif traderreg.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Trader!')
              return render(request,'registration/fregis.html') 
        elif eholder.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Equipmentholder!')
              return render(request,'registration/fregis.html')                  

        # email number check
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/fregis.html')
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/fregis.html')
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/fregis.html')           
         
        else:
              reg= Farmerreg(F_name=name,Address=address,Mobileno=mobileno,District=dist,Taluka=taluka,City=city,email=email1,Area=area,Pincode=pincode,password=password)
              reg.save() 
              subject = 'Thank you for registering to our site'
              message = ' it  means a world to us '
              email_from = settings.EMAIL_HOST_USER
              recipient_list = [email1]
              send_mail( subject, message, email_from, recipient_list )
              messages.success(request,'Successfully Register!')
              return render(request,'registration/fregis.html')
      else:  
          messages.error(request,'email already exists!')   
          return render(request,'registration/fregis.html',locals())
    else:       
        return render(request,'registration/fregis.html',locals())

# Trader Registration

def traderegis(request): 
    a= districts.objects.all()   
    if request.method=="POST":      
      name= request.POST.get('name','')   
      address= request.POST.get('address','')
      mobileno= request.POST.get('mobileno','')
      dist= request.POST.get('dist','')
      taluka= request.POST.get('taluka','')
      city= request.POST.get('city','')    
      email1= request.POST.get('email','')     
      pincode= request.POST.get('pincode','')
      password= request.POST.get('password','')   
      password1= request.POST.get('password1','') 

    # check mobile number and email already exist or not!
      if password==password1:
            # mobile number and email check
        if eholder.objects.filter(email=email1).exists():
          if eholder.objects.filter(Mobileno=mobileno).exists():
            messages.warning(request,'mobile number and Email already exists as a Equipmentholder!')
            return render(request,'registration/traderregis.html')             
          else:
              messages.warning(request,'Email already exists as a Equipmentholder!') 
          return render(request,'registration/traderregis.html') 
       
          # mobile number and email check
        elif traderreg.objects.filter(email=email1).exists():
          if traderreg.objects.filter(Mobileno=mobileno).exists():
              messages.warning(request,'mobile number and Email already exists as a Trader!') 
              return render(request,'registration/traderregis.html')            
          else:
              messages.warning(request,'Your email already exists as a Trader! please enter another email!') 
          return render(request,'registration/traderregis.html') 

          # mobile number and email check              
        elif Farmerreg.objects.filter(email=email1).exists():
           if Farmerreg.objects.filter(Mobileno=mobileno).exists():
                  messages.warning(request,'mobile number and Email already exists as a Farmer!') 
                  return render(request,'registration/traderregis.html')            
           else:
              messages.warning(request,'Your email already exists as a  Farmer! please enter another email!') 
           return render(request,'registration/traderregis.html')  

          # mobile number check
        elif Farmerreg.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Farmer!')
              return render(request,'registration/traderregis.html') 
        elif traderreg.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Trader!')
              return render(request,'registration/traderregis.html') 
        elif eholder.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Equipmentholder!')
              return render(request,'registration/traderregis.html')                  

        # email number check
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/traderregis.html')
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/traderregis.html')
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/traderregis.html')           
 
        else:
            reg= traderreg(T_name=name,Address=address,Mobileno=mobileno,District=dist,Taluka=taluka,City=city,email=email1,Pincode=pincode,password=password)
            reg.save() 
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email1]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'Successfully Register!')
            return render(request,'registration/traderregis.html') 
      else: 
          messages.error(request,'Password not matching!')
          return render(request,'registration/traderregis.htmt',locals())  
    else:       
        return render(request,'registration/traderregis.html',locals())

# Equipmentholder Registration

def holderregis(request):   
    a= districts.objects.all()
    if request.method=="POST":     
      name= request.POST.get('hname','')
      shopname= request.POST.get('shopname','')
      address= request.POST.get('haddress','')
      mobileno= request.POST.get('hmobileno','')
      dist= request.POST.get('hdist','')
      taluka= request.POST.get('htaluka','')
      city= request.POST.get('hcity','')
      pincode= request.POST.get('hpincode','')
      email1= request.POST.get('hemail','')
      password= request.POST.get('hpassword','')  
      password1= request.POST.get('hpassword1','')

    # check mobile number and email already exist or not!
      if password==password1:
            # mobile number and email check
        if eholder.objects.filter(email=email1).exists():
          if eholder.objects.filter(Mobileno=mobileno).exists():
            messages.warning(request,'mobile number and Email already exists as a Equipmentholder!') 
            return render(request,'registration/holderregister.html')             
          else:
              messages.warning(request,'Email already exists as a Equipmentholder!') 
              return render(request,'registration/holderregister.html') 
       
          # mobile number and email check
        elif traderreg.objects.filter(email=email1).exists():
          if traderreg.objects.filter(Mobileno=mobileno).exists():
              messages.warning(request,'mobile number and Email already exists as a Trader!')
              return render(request,'registration/holderregister.html')              
          else:
              messages.warning(request,'Your email already exists as a Trader! please enter another email!') 
              return render(request,'registration/holderregister.html') 

          # mobile number and email check              
        elif Farmerreg.objects.filter(email=email1).exists():
           if Farmerreg.objects.filter(Mobileno=mobileno).exists():
                  messages.warning(request,'mobile number and Email already exists as a Farmer!') 
                  return render(request,'registration/holderregister.html')            
           else:
              messages.warning(request,'Your email already exists as a  Farmer! please enter another email!') 
              return render(request,'registration/holderregister.html')

          # mobile number check
        elif Farmerreg.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Farmer!')
              return render(request,'registration/holderregister.html') 
        elif traderreg.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Trader!')
              return render(request,'registration/holderregister.html') 
        elif eholder.objects.filter(Mobileno=mobileno).exists():
              messages.error(request,'mobile number already exists as a Equipmentholder!')
              return render(request,'registration/holderregister.html')                  

        # email number check
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/holderregister.html')
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/holderregister.html')
        elif Farmerreg.objects.filter(email=email1).exists():
              messages.error(request,'Your email already exists as a Farmer! please enter another email!')
              return render(request,'registration/holderregister.html')           
        else:  
            reg= eholder(H_name=name,shop_name=shopname, Address=address,Mobileno=mobileno,District=dist,Taluka=taluka,City=city,email=email1,Pincode=pincode,password=password)
            reg.save() 
            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email1]
            send_mail( subject, message, email_from, recipient_list ) 
            messages.success(request,'Successfully Register!') 
            return render(request,'registration/holderregister.html')
      else:
        messages.warning(request,'Password not matching!')
        return render(request,'registration/holderregister.html',locals())
    else:       
      return render(request,'registration/holderregister.html',locals())

# Equipmentholder,Trader,Farmer,Admin Login

def hlogin(request):      
   request.session["idf"]=0
   request.session["tid"]=0
   if request.method == 'POST':
         #holder
        if eholder.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            hold = eholder.objects.get(email=request.POST['email'], password=request.POST['password'])  
            if hold.status==0:
                  messages.warning(request,'Your Approval is still panding please wait')
                  return render(request,'login/hlogin.html')
            else:      
              request.session["lgnh"] ='Welcome' + " " +hold.H_name                 
              request.session['prff']=hold.email 
              request.session["hnm"] =hold.H_name 
              request.session["hid"] =hold.H_id
              request.session["city"] =hold.City            
              return redirect('home.html')
        
          #farmer
        elif Farmerreg.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
             hold = Farmerreg.objects.get(email=request.POST['email'], password=request.POST['password'])   
             if hold.status==0:
                  messages.warning(request,'Your Approval is still panding please wait')
                  return render(request,'login/hlogin.html')
             else:  
              request.session["lgnf"] ='Welcome' + " " +hold.F_name 
              request.session["idf"]=hold.F_id
              request.session['prff']=hold.email   
              request.session["fname"] =hold.F_name                    
              return redirect('home.html')
        # trader
        elif traderreg.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
             hold = traderreg.objects.get(email=request.POST['email'], password=request.POST['password'])  
             if hold.status==0:
                  messages.warning(request,'Your Approval is still panding please wait')
                  return render(request,'login/hlogin.html')
             else: 
              request.session["lgnt"] ='Welcome' + " " +hold.T_name
              request.session['prff']=hold.email  
              request.session["tname"] =hold.T_name    
              request.session["tid"] =hold.T_id                       
              return redirect('home.html')
        #admin
        elif authorize.objects.filter(Email=request.POST['email'], Password=request.POST['password']).exists():
            hold = authorize.objects.get(Email=request.POST['email'], Password=request.POST['password']) 
            request.session["lgna"] ='Welcome' + " " +hold.A_name  
            request.session['prff']=hold.Email                        
            return redirect('home.html')
        else:
          messages.error(request,'Invalid username and Password!') 
          return render(request,'login/hlogin.html')
   return render(request,'login/hlogin.html')

# about

def about(request):
    return render(request,'home.html')

# contact

def contact(request):      
    return render(request,'profiles/contact.html')

# forgot password Equipmentholder,admin,trader,Farmer

def forgotpass(request):
    if request.method == 'POST':  
          email= request.POST.get('email','')
          # farmer
          if Farmerreg.objects.filter(email=request.POST['email']).exists():
            dri = Farmerreg.objects.get(email=request.POST['email'])
            password=dri.password
            name=dri.F_name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour password is:'+ password           
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'email sent successfully')
            return render(request,'login/forgotpassword.html')
            #holder
          elif eholder.objects.filter(email=request.POST['email']).exists():
            dri = eholder.objects.get(email=request.POST['email'])
            password=dri.password
            name=dri.H_name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour Password is:'+ password             
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'email sent successfully')
            return render(request,'login/forgotpassword.html')
            #trader
          elif traderreg.objects.filter(email=request.POST['email']).exists():
            dri = traderreg.objects.get(email=request.POST['email'])
            password=dri.password
            name=dri.T_name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour Password is:'+ password             
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'email sent successfully')
            return render(request,'login/forgotpassword.html')
            #admin
          elif authorize.objects.filter(Email=request.POST['email']).exists():
            dri = authorize.objects.get(Email=request.POST['email'])
            password=dri.Password
            name=dri.A_name
            subject = 'recover your password'
            message = 'Your Name is:'+ name + '\nYour Password is:'+ password             
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,'email sent successfully')
            return render(request,'login/forgotpassword.html')
          else:
            return render(request,'login/forgotpassword.html')
    else:
       return render(request,'login/forgotpassword.html')

# logout
@cache_control(no_cache=True, must_revalidate=True,non_store=True,max_age=0)
def logout(request):
    request.session.modified = True
    request.session.flush()
    request.session.modified = True
    return redirect('home.html')

# upload equipment

def equipmentupload(request): 
      storage= messages.get_messages(request)
      storage.used= True   
      if request.method == 'POST': 
            form = equipments(request.POST, request.FILES)   
            if form.is_valid(): 
                mb= eholder.objects.get(H_id=request.session["hid"])
                mob= mb.Mobileno
                mail= mb.email
                city= mb.City
                equipmentupload= form.save(commit=False)
                equipmentupload.H_id= request.session["hid"]        
                equipmentupload.H_name= request.session["hnm"]
                equipmentupload.Mobileno= mob
                equipmentupload.email = mail
                equipmentupload.City = city
                equipmentupload.save()                 
                messages.success(request,'successfully Upload Equipments')
                return render(request,'upload/uploadequipment.html')                 
      else: 
            form = equipments()
            messages.warning(request,'Not Upload Equipments!') 
      return render(request, 'upload/uploadequipment.html', {'form' : form}) 

# upload Farmer Products

def productupload(request,id):  
      storage= messages.get_messages(request)
      storage.used= True  
      a= uploadprice.objects.get(P_id=id) 
      b= a.P_name
      request.session["rmv"]=0
      request.session['tame']=a.T_name    
      request.session['pname']=a.P_name   
      if request.method == 'POST': 
            form = uploadproduct(request.POST, request.FILES)   
            if form.is_valid(): 
                mb= Farmerreg.objects.get(F_id=request.session["idf"])
                mob= mb.Mobileno
                mail= mb.email
                city= mb.City
                productupload= form.save(commit=False)
                productupload.F_id= request.session["idf"]                   
                productupload.P_id=id   
                productupload.F_name= request.session["fname"]
                productupload.Mobileno= mob
                productupload.email = mail
                productupload.City = city
                productupload.P_name = b
                productupload.save()    
                request.session["rmv"]=1             
                messages.success(request,'successfully Product Upload')
                return render(request,'productupload.html')   
            else:
                  messages.warning(request,'Not Upload Products!') 
      else: 
            form = uploadproduct()             
      return render(request, 'productupload.html', {'form' : form}) 

# upload Trader  Products Prices

def priceupload(request):     
       if request.method == 'POST': 
            form = upldprice(request.POST, request.FILES)   
            if form.is_valid():                
                priceupload= form.save(commit=False)
                priceupload.T_id= request.session["tid"]             
                priceupload.T_name= request.session["tname"]               
                priceupload.save()                 
                messages.success(request,'successfully Price Upload!!')
                return render(request,'upload/priceupload.html')     
            else:
                 messages.warning(request,'Not Upload Price!')              
       else: 
            form = upldprice()              
       return render(request, 'upload/priceupload.html', {'form' : form}) 

# Trader upload price List show farmer
def pricelist(request):
      prolist= uploadprice.objects.all()
      return render(request,'upload/pricelist.html',locals())


# All Entity Edit Profile

def edit_profile(request):  
    if eholder.objects.filter(email=request.session['prff']).exists():
      user = eholder.objects.get(email=request.session['prff'])
      form = editprofileh(instance=user)
      if request.method == "POST":
        form = editprofileh(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save()         
    elif traderreg.objects.filter(email=request.session['prff']).exists():
      user = traderreg.objects.get(email=request.session['prff'])
      form = editprofilet(instance=user)
      if request.method == "POST":
        form = editprofilet(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save()   
          messages.success(request,'Your profile update Successfully')        
    elif Farmerreg.objects.filter(email=request.session['prff']).exists():
      user = Farmerreg.objects.get(email=request.session['prff'])
      form = editprofilef(instance=user)
      if request.method == "POST":
        form = editprofilef(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save() 
          messages.success(request,'Your profile update Successfully')          
    elif authorize.objects.filter(Email=request.session['prff']).exists():
      user = authorize.objects.get(Email=request.session['prff'])
      form = editprofilea(instance=user)
      if request.method == "POST":
        form = editprofilea(request.POST, request.FILES, instance=user)
        if form.is_valid():
          update = form.save(commit=False)               
          update.user = user
          update.save()    
          messages.success(request,'Your profile update Successfully')       
    return render(request, 'profiles/edit_profile.html', {'form': form})

# Authorized Admin

def authorized(request):
      istekler = Farmerreg.objects.all()
      holderacp = eholder.objects.all()
      trader=traderreg.objects.all() 
      prc=uploadprice.objects.filter(T_id=request.session["tid"])
      fupld=uproduct.objects.all()      
      return render(request, 'admin/authorized.html', locals())
          
# delete All  request
def reject(request, F_id):
      if Farmerreg.objects.filter(F_id=F_id).exists():
            Farmerreg.objects.get(F_id=F_id).delete()
      elif eholder.objects.filter(H_id=F_id).exists():
            eholder.objects.get(H_id=F_id).delete()
      elif traderreg.objects.filter(T_id=F_id).exists():
            traderreg.objects.get(T_id=F_id).delete()   
      elif uploadequip.objects.filter(E_id=F_id).exists():
            uploadequip.objects.get(E_id=F_id).delete()  
            return redirect('equiplist.html0')
      
      else:  
            uproduct.objects.get(S_id=F_id).delete()          
      messages.warning(request,'Rejected Successfully')
      return redirect('authorized.html')
           
#accept All request
def accept(request,F_id):
      Farmerreg.objects.filter(F_id=F_id).update(status=1)
      eholder.objects.filter(H_id=F_id).update(status=1)
      traderreg.objects.filter(T_id=F_id).update(status=1)     
      messages.success(request,'Approved Successfully')   
      return redirect('authorized.html')

# Show product List

def productlist(request):                
            d= request.session["idf"]          
            if  d != 0:
                  upld=uproduct.objects.filter(F_id=d)
                  return render(request, 'admin/productlist.html', locals()) 
            else:
                  upld=uproduct.objects.all() 
                  return render(request, 'admin/productlist.html', locals()) 
            return render(request, 'admin/productlist.html', locals()) 
            
# Show Equipments List

def equipmentlist(request):   
      uplde=uploadequip.objects.all()         
      el=rentequipment.objects.all()       
      return render(request, 'equiplist.html', locals())        
     

def equipmentlisth(request,id): 
      uplde=uploadequip.objects.filter(H_id = request.session["hid"])        
      return render(request, 'equiplist.html', locals())    
     

# Show Trader Price List

def tpricelist(request):
      pricel=uploadprice.objects.all()  
      return render(request, 'admin/tpricelist.html', locals())

def tpricelistt(request):      
      sdate= request.POST.get('sdate','')
      ldate = request.POST.get('ldate','')
      if sdate != '' and ldate != '':
            pricel= uploadprice.objects.filter(mydate__range=(sdate,ldate))
            if request.method == 'POST':
                  updt=request.POST.get('updt','')
                  request.session["updt"] = updt
                  upid= request.POST.get('pid','') 
                  if updt != "" and upid != "":
                        uploadprice.objects.filter(P_id=upid).update(Price=updt)
                        messages.success(request,'upload price successfully')
            return render(request, 'admin/tpricelist.html', locals())

      else:   
            pricel=uploadprice.objects.filter(T_id = request.session["tid"])  
            if request.method == 'POST':
                  updt=request.POST.get('updt','')
                  request.session["updt"] = updt
                  upid= request.POST.get('pid','') 
                  if updt != "" and upid != "":
                        uploadprice.objects.filter(P_id=upid).update(Price=updt)
                        messages.success(request,'upload price successfully')
            return render(request, 'admin/tpricelist.html', locals())

# All equipments list in home page

def tractors(request,id):
      if id==1:
            nam="tractor"
            d=uploadequip.objects.filter(Category=nam)
      elif id==2:
            nam="Harvesters"
            d=uploadequip.objects.filter(Category=nam)
      elif id==3:
            nam="tiller"
            d=uploadequip.objects.filter(Category=nam)
      elif id==4:
            nam="Sowing and Planting Equipments"
            d=uploadequip.objects.filter(Category=nam)
      elif id==5:
            nam="Pesticide applicators"
            d=uploadequip.objects.filter(Category=nam)
      elif id==6:
            nam="landscaping Equipments"
            d=uploadequip.objects.filter(Category=nam)
      elif id==7:
            nam="postharvest equipments"
            d=uploadequip.objects.filter(Category=nam)
      return render(request,'tractor/tractor.html',locals())

# Farmer rent in equipments
def rent(request,id):
      sd=rentequipment.objects.filter(E_id=id)
      storage=messages.get_messages(request)
      storage.used=True   
      a=uploadequip.objects.get(E_id=id)   
      if request.method == 'POST':    
        sdate = request.POST.get('sdate','')
        edate = request.POST.get('edate','')    
        form = rentequipments(request.POST, request.FILES) 
        if form.is_valid(): 
                mb= Farmerreg.objects.get(F_id=request.session["idf"])
                fnm= mb.F_name
                mob= mb.Mobileno
                mail= mb.email
                city= mb.City
                add= mb.Address
                pin= mb.Pincode              
                productupload= form.save(commit=False)
                productupload.startdate=parser.parse(sdate)
                productupload.enddate=parser.parse(edate)
                productupload.F_id=request.session["idf"]  
                productupload.H_id=a.H_id
                productupload.E_id=id               
                productupload.Name= fnm
                productupload.Mobileno= mob
                productupload.Email = mail
                productupload.City = city
                productupload.Address = add
                productupload.Pincode = pin
                productupload.save()
                uploadequip.objects.filter(E_id=id).update(status=1)
                messages.success(request,'booking successfully!')
                return render(request, 'rent.html') 
      else: 
        form = rentequipments()       
      return render(request,'rent.html',locals(),{'form':form})

# Equipment holder show rent farmer list
def rentlist(request):    
      c= rentequipment.objects.filter(H_id= request.session["hid"])
      return render(request,'rentlist.html',locals())

# Equipment holder Accept rent farmer list

def acptrent(request,id):
      rentequipment.objects.filter(R_id=id).update(status=1)

      d=rentequipment.objects.get(R_id=id)          
      subject = 'Authentication of request For Rent in Equipments'
      message = 'Your Authentication Successfully '
      to = d.Email     
      email_from = settings.EMAIL_HOST_USER    
      send_mail( subject, message, email_from, [to] )
      return redirect('rentlist.html')

# Equipment holder Reject rent farmer list

def rjctrent(request, id):
      rentequipment.objects.get(R_id=id).delete()
      return redirect('rentlist.html')

# All data list to Admin

def listall(request,id):
      sdate= request.POST.get('sdate','')
      ldate = request.POST.get('ldate','')
      if sdate== '' and ldate=='':
            if id== 1:
                  request.session["alist"] = "flist"
                  farmerlst= Farmerreg.objects.all()
            elif id == 2:
                  request.session["alist"] = "tlist"
                  traderlst= traderreg.objects.all()
            elif id == 3:
                  request.session["alist"] = "ehlist"
                  holderlst= eholder.objects.all()
            elif id == 4:
                  request.session["alist"] = "fplist"
                  fmprdlst= uproduct.objects.all()
            elif id == 5:
                  request.session["alist"] = "tplist"
                  trprdlst= uploadprice.objects.all()
            elif id == 6:
                  request.session["alist"] = "helist"
                  holdeqlst= uploadequip.objects.all()
            elif id == 7:
                  request.session["alist"] = "frlist"                 
                  farentlst= rentequipment.objects.all()
                  fareqip= uploadequip.objects.all()
            elif id == 8:
                  request.session["alist"] = "buylist"                 
                  buylst= buyproduct.objects.all()
            return render(request,'admin/list.html',locals())
      else:
            if id== 1:
                  request.session["alist"] = "flist"
                  farmerlst= Farmerreg.objects.filter(mydate__range=(sdate,ldate)) 
            elif id == 2:
                  request.session["alist"] = "tlist"
                  traderlst= traderreg.objects.filter(mydate__range=(sdate,ldate)) 
            elif id == 3:
                  request.session["alist"] = "ehlist"
                  holderlst= eholder.objects.filter(mydate__range=(sdate,ldate)) 
            elif id == 4:
                  request.session["alist"] = "fplist"
                  fmprdlst= uproduct.objects.filter(mydate__range=(sdate,ldate)) 
            elif id == 5:
                  request.session["alist"] = "tplist"
                  trprdlst= uploadprice.objects.filter(mydate__range=(sdate,ldate)) 
            elif id == 6:
                  request.session["alist"] = "helist"
                  holdeqlst= uploadequip.objects.filter(mydate__range=(sdate,ldate)) 
            elif id == 7:
                  request.session["alist"] = "frlist"
                  farentlst= rentequipment.objects.filter(mydate__range=(sdate,ldate))   
            elif id == 8:
                  request.session["alist"] = "buylist"
                  farentlst= buyproduct.objects.filter(mydate__range=(sdate,ldate))                
            return render(request,'admin/list.html',locals())

# Buying Products Trader to Farmer

def buyprod(request,id):
      storage= messages.get_messages(request)
      storage.used= True   
      mb= uproduct.objects.get(S_id=id)
      fid= mb.F_id
      name= mb.F_name
      qtty=mb.Quantity
      pnm = mb.P_name
      request.session["fnm"]=mb.F_name
      pb=uploadprice.objects.filter(T_id=request.session["tid"])
      prc=0
      for i in pb:
            if i.P_name == pnm:
                  prc=i.Price   
      mbt= traderreg.objects.get(T_id=request.session["tid"])
      namet=mbt.T_name
      mail= mbt.email
      if request.method == 'POST': 
            quty= request.POST.get("qty",'')
            form = buyproducts(request.POST, request.FILES)   
            if form.is_valid(): 
                productupload= form.save(commit=False)
                productupload.T_id= mbt.T_id
                productupload.F_id= fid             
                productupload.F_name= name
                productupload.T_name= namet
                productupload.email = mail 
                productupload.P_name = pnm     
                productupload.Quantity = quty 
                productupload.Price = int(quty) *  int(prc)             
                productupload.save()  
                fqty= int(qtty)- int(quty)
                if fqty == 0:
                      uproduct.objects.get(S_id = id).delete()
                uproduct.objects.filter(S_id=id).update(Quantity=fqty,status=1)  
                messages.success(request,'successfully Buy Product')
                return render(request,'buy.html')                 
      else: 
            form = buyproducts() 
           #messages.warning(request,'Not Buy Products!') 
      return render(request, 'buy.html', {'form' : form}) 
      return render(request,'buy.html')

# List Rent product by farmer

def rentprolist(request):
      c= rentequipment.objects.filter(H_id= request.session["hid"])   
      if request.method =='POST': 
            pid= request.POST.get('rid','')
            d=rentequipment.objects.get(R_id=pid)            
            a = d.startdate
            b = d.enddate
            delta = b - a
            dd=delta.days
            e=eholder.objects.get(H_id=request.session["hid"])
            f=uploadequip.objects.get(E_id=d.E_id)
            total=f.Rent_price * dd
            form = rentbill(request.POST, request.FILES)
            if form.is_valid():
                  rentprolist = form.save(commit = False) 
                  rentprolist.H_id=request.session["hid"]
                  rentprolist.E_id=d.E_id
                  rentprolist.F_id=d.F_id   
                  rentprolist.R_id=d.R_id
                  rentprolist.F_name=d.Name
                  rentprolist.H_name=e.H_name      
                  rentprolist.Name=f.E_name   
                  rentprolist.Total= total                                    
                  rentprolist.save() 
                  rentequipment.objects.filter(R_id= pid).update(status=2)
                  messages.success(request,'Bill sent')
                  return render(request, "rentbill.html")
            else: 
                  return render(request, "rentbill.html", {'form':details}) 
      else: 
            form = rentbill(None)    
            return render(request, 'rentbill.html', locals(), {'form':form})    
      return render(request,'rentbill.html',locals())   

def transactions(request):
      if request.method =='POST': 
            details = rentbill(request.POST, request.FILES)
            if details.is_valid():
                  post = details.save(commit = False) 
                  post.save() 
                  return HttpResponse("data submitted successfully") 
            else: 
                  return render(request, "rentbill.html", {'form':details}) 
      else: 
            form = rentbill(None)    
            return render(request, 'rentbill.html', {'form':form}) 


# Transaction List show in Farmer

def transactionlist(request,id):
      sdate= request.POST.get('sdate','')
      ldate = request.POST.get('ldate','')
      
      if sdate== '' and ldate=='' and request.session["tid"] == 0:
            if id== 9:
                  request.session["alistt"] = "translist"
                  translst=transaction.objects.filter(F_id = request.session["idf"])
                  return render(request,'transaction.html',locals())
            elif id == 10:
                  request.session["alistt"] = "prolist"
                  tproductlst= buyproduct.objects.filter(F_id = request.session["idf"])            
            return render(request,'transaction.html',locals())

      elif sdate== '' and ldate=='' and request.session["tid"] != 0:
           tprotlst= buyproduct.objects.filter(T_id = request.session["tid"])
           return render(request,'transaction.html',locals())

      elif buyproduct.objects.filter(T_id = request.session["tid"]).exists():
            tprotlst= buyproduct.objects.filter(mydate__range=(sdate,ldate)) 
            return render(request,'transaction.html',locals())
      
      else:
            if id == 9:
                  request.session["alistt"] = "translist"                  
                  translst= rentequipment.objects.filter(mydate__range=(sdate,ldate))   
            elif id == 10:
                  request.session["alistt"] = "prolist"
                  tproductlst= buyproduct.objects.filter(mydate__range=(sdate,ldate))                
            return render(request,'transaction.html',locals())
      return render(request,'transaction.html',locals())

# Generate PDF 

def GeneratePDF(request,id,*args, **kwargs):                
        if id == 1:           
            a = "flist"            
            b = Farmerreg.objects.all() 
            
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            }
        elif id == 2:
            a ="tlist"            
            b = traderreg.objects.all() 
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            }  
        elif id == 3:           
            a =  "ehlist"
            b = eholder.objects.all() 
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            } 
        elif id == 4:            
            a = "fplist"
            b = uproduct.objects.all() 
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            } 
        elif id == 5:           
            a = "tplist"
            b = uploadprice.objects.all() 
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            } 
        elif id == 6:            
            a = "helist"
            b = uploadequip.objects.all() 
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            } 
        elif id == 7:            
            a = "frlist"
            b = rentequipment.objects.all() 
            j = uploadequip.objects.all()
            context = {
                'a':a,
                'b':b,
                'j':j,
                'date':datetime.now()
            } 
        elif id == 8:            
            a ="buylist"
            b = buyproduct.objects.all() 
            context = {
                'a':a,
                'b':b,
                'date':datetime.now()
            }         
        template = get_template('pdf.html')      
        html = template.render(context)
        pdf = render_to_pdf('pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Alllist_%s.pdf" %("1")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

# Generate pdf for Rent bill and Trader Buy Product

def rentfarmlist(request,id):     
      a=""
      b=""
      x=""
      y=""
      z=""
      if  transaction.objects.filter(Rb_id=id).exists(): 
            a ="billlist"
            b = transaction.objects.get(Rb_id=id)  
            y = Farmerreg.objects.get(F_id=b.F_id) 
            z = uploadequip.objects.all()

      elif buyproduct.objects.filter(B_id=id).exists() :
            a ="tradbill"
            b = buyproduct.objects.get(B_id=id)
            x = traderreg.objects.get(T_id=b.T_id)
             
      context = {
            'a':a,
            'b':b,
            'x':x,
            'y':y,
            'z':z,
            'date':datetime.now()
      }  
      template = get_template('rentfarmlist.html')      
      html = template.render(context)
      pdf = render_to_pdf('rentfarmlist.html', context)
      if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Bill_%s.pdf" %("1")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
      return HttpResponse("Not found") 

# Admin Upload Districts

def updisttrict(request):
      c= districts.objects.all()           
      if request.method=="POST":      
                  district= request.POST.get('dist','') 
                  if district != "":
                        reg= districts(District=district)
                        reg.save() 
                        messages.success(request,'Upload Successfully')
      return render(request,'uplddistrict.html',locals())  

# Admin Delete Districts

def deletedis(request,id):   
            districts.objects.get(D_id=id).delete()
            messages.success(request,'District Delete')
            return redirect('districtupld.html')       

def basic(request):
      return render(request,'basic.html')
