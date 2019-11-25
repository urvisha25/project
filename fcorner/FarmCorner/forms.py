from django import forms 
from .models import *

# upload equipment images
class equipments(forms.ModelForm):   
    class Meta: 
        model = uploadequip 
        fields = ['E_name','Category','Image','year','Condition','hp','Rent_price']   
        labels={               
                'E_name': 'Equipment Name',  
                'Rent_price': 'Rent Price in Per Day',
                'hp':'Tractor Power in HP',
                'year':'Year of Equipment',               
            }

# upload product images

class uploadproduct(forms.ModelForm):   
    class Meta: 
            model = uproduct 
            fields = ['Image','Quantity','Grade']   
            labels={               
                'Image': 'Choose the Image',
                'Quantity':'Quantity in Mann(1Mann=20kg)',
                'Grade':'Product Grade'
            }             

 # upload product price

class upldprice(forms.ModelForm):   
    class Meta: 
            model = uploadprice 
            fields = ['P_name','Gradea','Gradeb','Gradec']   
            labels={ 
                'P_name':'Product Name',  
                'Gradea':'Price for Grade A (Rs In 20kg)',
                'Gradeb':'Price for Grade B (Rs In 20kg)',
                'Gradec':'Price for Grade C (Rs In 20kg)',
            }       

# edit profile Equipmentholder
class editprofileh(forms.ModelForm):
    class Meta:
        model=eholder
        fields=[
            'H_name','shop_name','Address','District','Taluka','City','Pincode','password']

        labels={ 
                'H_name':'Equipmentholder Name',               
                'shop_name':'Shop Name',
                'password':'Password'
            } 

# edit profile  Trader
class editprofilet(forms.ModelForm):
    class Meta:
        model=traderreg
        fields=[
            'T_name','Address','District','Taluka','City','Pincode','password']

        labels={ 
                'T_name':'Trader Name',  
                'password':'Password'
            } 

# edit profile Farmer
class editprofilef(forms.ModelForm):
    class Meta:
        model=Farmerreg
        fields=[
            'F_name','Address','District','Taluka','City','Pincode','Area','password' ]

        labels={ 
                'F_name':'Farmer Name',  
                'password':'Password'
            } 

# edit profile admin
class editprofilea(forms.ModelForm):
    class Meta:
        model=authorize
        fields=[
            'A_name','Email','Password']

        labels={ 
                'A_name':'Admin Name' } 

# edit Upload Equipments by Holder

class editequipments(forms.ModelForm):
    class Meta:
        model=uploadequip
        fields=['Category','E_name','Image','year','hp','Rent_price']

        labels={ 
                'E_name':'Equipment Name',
                'Rent_price':'Rent Price In Rs',
                'hp':'Power',
                'year':'Year of Equipment'
                 } 

#Edit Product Price by Holder

class editeprodprice(forms.ModelForm):
    class Meta:
        model=uploadprice
        fields=['Gradea','Gradeb','Gradec']

        labels={ 
                'Gradea':'Grade A Price in 20kg',
                'Gradeb':'Grade B Price in 20kg',
                'Gradec':'Grade C Price in 20kg'
                 } 

#Edit Farm Productby Farmer

class editeproduct(forms.ModelForm):
    class Meta:
        model=uproduct
        fields=['Quantity']

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

class uploadtaluka(forms.ModelForm):
    class Meta:
        model = talukas
        fields=["Taluka"]


