from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from . import views
from .forms import *

urlpatterns=[    
    # home
    path("",views.home, name='home'),  
    path("home.html",views.home, name='home'), 
    
    # Logins, forgotpassword  
    path("hlogin",views.hlogin, name='holderlogin'),
    path("forgotpassword",views.forgotpass, name='forgot password'), 

    # Registrations    
    path("fregis",views.farmerregis, name='fregister'),
    path("holderregister",views.holderregis, name='Hregister'),
    path("traderregis",views.traderegis, name='Tregister'),

    # about, contact,logout
    path("about.html",views.about, name='about'),
    path("contact.html",views.contact, name='contact'),
    path('logout',views.logout,name='Logout'),  

    # Farmer upload products,Trader upload prices, Holder upload equipments
    path("uploadequipment", views.equipmentupload, name = 'image_upload'),    
    path('productupload<int:id>', views.productupload, name = 'productupload'), 
    path('priceupload', views.priceupload, name = 'priceupload'), 

    # Profile   
    path('profile',views.edit_profile, name='edit_profile'),     

    # Accept/reject via admin and trader
    path('authorized.html',views.authorized, name='Authorized'),
    path('accept<int:F_id>',views.accept, name='accept'),
    path('authorized<int:F_id>',views.reject, name='reject'),    

    # List of prices and admin show all list
    path('pricelist',views.pricelist, name='pricelist'), 
    path('productlist',views.productlist, name='productlist'), 
    path('equipmentlist',views.equipmentlist, name='equipmentlist'),
    path('equiplist<int:id>',views.equipmentlisth, name='equipmentlist particular Holder'),    
    path('equiplist.html<int:id>',views.equipmentlisth, name='equipmentlist particular Holder'), 
    path('tpricelist',views.tpricelist, name='Tpricelist'),     
    path('tpricelistt',views.tpricelistt, name='Tpricelist particular Trader'), 

    # list of all categorywise products and rent
    path('tractors<int:id>',views.tractors, name='tractors'), 
    path('rent<int:id>',views.rent, name='Rent'), 
    path('rentlist.html',views.rentlist, name='Rent1'), 
    path('acpt<int:id>',views.acptrent, name='acceptrent'),
    path('rjct<int:id>',views.rjctrent, name='rejectrent'),     
    path('list<int:id>',views.listall),

    # Buy Product, bill generate
    path('buy<int:id>',views.buyprod, name='Buy Product'),
    path('rentbill',views.rentprolist, name='rent bill generate'),
    path('transaction<int:id>',views.transactionlist, name='rent bill list'),
    path('pdff',views.send_pdf, name='rent bill generate'),
    path('pdf',views.pdf, name='rent bill generate'),
    path('GeneratePDF<int:id>',views.GeneratePDF, name='rent bill generate'),
    path('rentbill<int:id>',views.rentbill, name='rent bill print(PDF)'),
] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
