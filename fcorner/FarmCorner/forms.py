from django import forms 
from .models import *

# upload equipment images
class equipments(forms.ModelForm):   
    class Meta: 
        model = uploadequip 
        fields = ['E_name','Category','Image','Rent_price']   
        labels={
               
                'E_name': 'Equipment Name',    
            }

# upload product images

class uploadproduct(forms.ModelForm):   
    class Meta: 
            model = uproduct 
            fields = ['Image','Quantity']   
            labels={               
             
                'Quantity':'Quantity in Mann(1Mann=20kg)'
            }

 # upload product price

class upldprice(forms.ModelForm):   
    class Meta: 
            model = uploadprice 
            fields = ['P_name','Price']   
            labels={ 
                'P_name':'Product Name',               
                'Price':'Price (Rs/20kg)'
            }       

# edit profile Equipmentholder
class editprofileh(forms.ModelForm):
    class Meta:
        model=eholder
        fields=[
            'H_name','shop_name','Address','Mobileno','District','Taluka','City','Pincode','password'
        ]

# edit profile  Trader
class editprofilet(forms.ModelForm):
    class Meta:
        model=traderreg
        fields=[
            'T_name','Address','Mobileno','District','Taluka','City','email','Pincode','password'
        ]

# edit profile Farmer
class editprofilef(forms.ModelForm):
    class Meta:
        model=Farmerreg
        fields=[
            'F_name','Address','Mobileno','District','Taluka','City','email','Pincode','Area','password'
        ]

# edit profile admin
class editprofilea(forms.ModelForm):
    class Meta:
        model=authorize
        fields=[
            'A_name','Email','Password'
        ]

# rent

class DateInput(forms.DateInput):
    input_type = 'date'

class rentequipments(forms.ModelForm):
    class Meta:
        model = rentequipment
        fields=[]#'startdate','enddate']

       # widgets = {
        #    'startdate': DateInput(attrs={'class': 'datepicker'}),
        #    'enddate':DateInput(attrs={'class': 'datepicker'}),           
 #  }

# Buying Product

class buyproducts(forms.ModelForm):
    class Meta:
        model = buyproduct
        fields=[]

# generate rent bill

class rentbill(forms.ModelForm):
    class Meta:
        model = transaction
        fields=[]

