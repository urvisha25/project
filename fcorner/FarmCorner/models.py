from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime
from .render import validate_file_size
from django.core.exceptions import ValidationError

# Create your models here.
# discribe district

class districts(models.Model):
   D_id = models.AutoField(primary_key=True)
   District=models.CharField(max_length=15, default="")

   def __str__(self):
        return self.District

# Farmer Registration form
class Farmerreg(models.Model):
   F_id= models.AutoField(primary_key=True)
   F_name= models.CharField(max_length=40)
   Address= models.CharField(max_length=70, default="")
   Mobileno= models.CharField(max_length=13, default="")
   District= models.CharField(max_length=15, default="")
   Taluka= models.CharField(max_length=15, default="")
   City= models.CharField(max_length=15, default="")  
   email= models.EmailField(max_length=50, default="")
   Area=models.CharField(max_length=10, default="")
   Pincode= models.IntegerField(default=0)   
   password= models.CharField(max_length=20)  
   mydate = models.DateTimeField(default=datetime.now())  
   status=models.IntegerField(default=0)
  
   def __str__(self):
        return self.F_name

# Equipmentholder Registration
class eholder(models.Model):
       H_id= models.AutoField(primary_key=True)
       H_name= models.CharField(max_length=40, default="")
       shop_name= models.CharField(max_length=40, default="")
       Address= models.CharField(max_length=70, default="")
       Mobileno= models.CharField(max_length=13, default="")
       District= models.CharField(max_length=15, default="")
       Taluka= models.CharField(max_length=15, default="")
       City= models.CharField(max_length=15, default="") 
       email= models.EmailField(max_length=50, default="") 
       Pincode= models.IntegerField(default=0) 
       password= models.CharField(max_length=30)
       mydate = models.DateTimeField(default=datetime.now())
       status=models.IntegerField(default=0)
       
       def __str__(self):
          return self.H_name
   

cat = (
    ('Tractor','Tractor'),
    ('Tiller', 'Tiller'),
    ('Harvesters','Harvesters'),
    ('Sowing and Planting Equipments','Sowing and Planting Equipments'),
    ('Pesticide Applicators','Pesticide Applicators'),   
    ('Landscaping Equipments','Landscaping Equipments'),
    ('postharvest Equipments','postharvest Equipments'),
    ('Others','Others')
     )

# Equipmentholder upload equipments
class uploadequip(models.Model):
       E_id= models.AutoField(primary_key=True)    
       H_id= models.IntegerField(default=0)  
       H_name= models.CharField(max_length=40, default="")
       E_name= models.CharField(max_length=40, default="")      
       City= models.CharField(max_length=15, default="")   
       Mobileno= models.CharField(max_length=13, default="")  
       Category=models.CharField(max_length=50, choices=cat,default="")  
       email= models.EmailField(max_length=50, default="") 
       year= models.CharField(default="",max_length=12)   
       hp = models.FloatField(default="")
       Image= models.ImageField(upload_to="Image", default="",validators=[validate_file_size])       
       Rent_price= models.IntegerField(default="") 
       mydate = models.DateTimeField(default=datetime.now())
       startdate=models.DateField(default=datetime.now())
       enddate = models.DateField(default=datetime.now())
       Rating = models.FloatField(default=0)
       status=models.IntegerField(default=0)
       
       def __str__(self):
          return self.E_name
     

# Trader Registration form
class traderreg(models.Model):
       T_id= models.AutoField(primary_key=True)
       T_name= models.CharField(max_length=40, default="")       
       Address= models.CharField(max_length=70, default="")
       Mobileno= models.CharField(max_length=13, default="")
       District= models.CharField(max_length=15, default="")
       Taluka= models.CharField(max_length=15, default="")
       City= models.CharField(max_length=15, default="") 
       email= models.EmailField(max_length=50, default="") 
       Pincode= models.IntegerField(default=0) 
       password= models.CharField(max_length=30)
       mydate = models.DateTimeField(default=datetime.now())
       status=models.IntegerField(default=0)
     
       def __str__(self):
        return self.T_name

# Trader upload Product related prices
class uploadprice(models.Model):
   P_id= models.AutoField(primary_key=True)    
   T_id= models.IntegerField(default=0) 
   T_name=models.CharField(max_length=40, default="")  
   P_name= models.CharField(max_length=40, default="")  
   Gradea = models.IntegerField(default="")
   Gradeb = models.IntegerField(default="")
   Gradec = models.IntegerField(default="")  
   mydate = models.DateTimeField(default=datetime.now())
 
   def __str__(self):
      return self.P_name

# Admin Registration form
class authorize(models.Model):
   A_id= models.AutoField(primary_key=True)   
   A_name= models.CharField(max_length=40, default="")
   Email= models.EmailField(max_length=50, default="")  
   Password= models.CharField(max_length=30)    

   def __str__(self):
      return self.Email 

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = authorize.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=authorize)

class uproduct(models.Model):
   gradechoice=(('A','Grade A'),('B','Grade B'),('C','Grade C'))
   S_id= models.AutoField(primary_key=True)   
   F_id= models.IntegerField(default=0)    
   P_id= models.IntegerField(default=0)  
   F_name= models.CharField(max_length=40, default="")
   P_name= models.CharField(max_length=40, default="")
   Mobileno= models.CharField(max_length=13, default="")
   City= models.CharField(max_length=15, default="")
   Image= models.ImageField(upload_to='Image', default="",validators=[validate_file_size])
   email=models.EmailField(max_length=50, default="")   
   Quantity= models.IntegerField(default="") 
   status=models.IntegerField(default=0)
   Grade = models.CharField(default="",choices=gradechoice,max_length=7)
   mydate = models.DateTimeField(default=datetime.now())   
   def __str__(self):
      return self.P_name

class rentequipment(models.Model):
   R_id=models.AutoField(primary_key=True)
   F_id= models.IntegerField(default=0)    
   H_id= models.IntegerField(default=0)
   E_id= models.IntegerField(default=0) 
   Name = models.CharField(max_length=40, default="")
   Mobileno=models.CharField(max_length=13, default="")
   Email=models.CharField(max_length=50, default="")
   Address= models.CharField(max_length=70, default="")
   City= models.CharField(max_length=15, default="")
   Pincode= models.IntegerField(default=0)  
   startdate=models.DateField(datetime.now())
   enddate = models.DateField(datetime)
   status=models.IntegerField(default=0)
   mydate = models.DateTimeField(default=datetime.now())   
   unumber = models.IntegerField(default=0)

   def __str__(self):
          return self.Name

class buyproduct(models.Model):
   B_id=models.AutoField(primary_key=True)
   T_id=models.IntegerField(default=0) 
   F_id=models.IntegerField(default=0) 
   F_name= models.CharField(max_length=40, default="")
   T_name= models.CharField(max_length=40, default="")
   P_name= models.CharField(max_length=40, default="")
   Quantity= models.IntegerField(default=0) 
   email=models.EmailField(max_length=50, default="")   
   Price= models.IntegerField(default="") 
   mydate = models.DateTimeField(default=datetime.now())
   def __str__(self):
          return self.F_name 

class transaction(models.Model):
   Rb_id=models.AutoField(primary_key=True)
   T_id=models.IntegerField(default=0) 
   F_id=models.IntegerField(default=0)
   H_id=models.IntegerField(default=0) 
   B_id=models.IntegerField(default=0)
   R_id=models.IntegerField(default=0)  
   P_id=models.IntegerField(default=0) 
   E_id=models.IntegerField(default=0) 
   F_name= models.CharField(max_length=40, default="")
   T_name= models.CharField(max_length=40, default="")   
   Name= models.CharField(max_length=40, default="")
   H_name= models.CharField(max_length=40, default="")
   Total=models.IntegerField(default=0) 
   status=models.IntegerField(default=0)
   mydate = models.DateTimeField(default=datetime.now())

   def __str__(self):
         return self.Name 
  
