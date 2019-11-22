from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from . import views
from .forms import *

urlpatterns=[    
    # home,Product show all
    path("",views.home, name='home'),  
    path("home.html",views.home, name='home'), 
    path('tractors<int:id>',views.tractors, name='tractors'),
    path('quikview<int:id>', views.quikview, name="Farmer show all equipment details"),

    # Logins, forgotpassword  
    path("hlogin",views.hlogin, name='holderlogin'),
    path("forgotpassword",views.forgotpass, name='forgot password'), 
   
    # Registrations    
    path("fregis",views.farmerregis, name='fregister'),
    path("holderregister",views.holderregis, name='Hregister'),
    path("traderregis",views.traderegis, name='Tregister'),

    # about, contact,logout,profile
    path("about",views.about, name='about'),
    path("contact.html",views.contact, name='contact'),
    path('logout',views.logout,name='Logout'),
    path('profile',views.edit_profile, name='edit_profile'), 

    # Farmer upload product, show,show trader price, show equipmentlist,
    # rent in equipments,list equipments, rate in equipments

    path('productupload<int:id>', views.productupload, name = 'farmer upload farm product'), 
    path('pricelist',views.pricelist, name='trader upload pricelist'),
    path('productlist.html',views.productlist, name='farmer upload productlist'), 
    path('equipmentlist.html',views.equipmentlist, name='equipment holder upload equipment list'),
    path('rent<int:id>',views.rent, name='farmer rent in equipments'), 
    path('rentlist.html',views.rentlist, name='farmer rent in equipments list'),
    path('rprice.html', views.equipmentbill, name="Farmer rent in equipment then its give Bill"),   
    path('rentconfirm<int:id>',views.rentconfirm, name='farmer delete rent in equipments'),  
    path('rate<int:id>',views.rat, name='rat Product'),
    path('rentfarmlist<int:id>',views.rentfarmlist, name='rent bill print(PDF),trader buy product bill PDF'),
    path('delrentequip<int:id>',views.delrentequip, name='rent Equipment delete'),
    path('transaction<int:id>.html',views.transactionlist, name='rent bill list,trader buy product price list'),
    path('editproduct<int:id>',views.editproduct, name="edit Farm product by Farmer"),

    # Trader upload Price, show, show Farmer Product, Buy product,edit

    path('priceupload', views.priceupload, name = 'Trader upload price'),
    path('tpricelistt.html',views.tpricelistt, name='Tpricelist particular Trader'),
    path('tpricelist',views.tpricelist, name='Tpricelist'),     
    path('buy<int:id>',views.buyprod, name='Buy Product'),
    path('GeneratePDF<int:id>',views.GeneratePDF, name='rent bill generate'),
    path('editprice<int:id>',views.editprice, name="edit product price by Trader"), 

    # Equipmentholder upload equipment,edit,list,give bill
     
    path("uploadequipment", views.equipmentupload, name = 'image_upload'),
    path('equiplist<int:id>',views.equipmentlisth, name='equipmentlist particular Holder'),    
    path('equiplist.html<int:id>',views.equipmentlisth, name='equipmentlist particular Holder'), 
    path('editequipment<int:id>',views.edit_profiles, name="edit upload equipments by Holder"), 
    path('rentbill',views.rentprolist, name='farmer rent in equipments list'),
      

    # Admin upload Districts, and Show all list,accepr/reject all
    path('list<int:id>',views.listall),
    path('districtupld.html',views.updisttrict, name='Admin upload Districts'),
    path('deletedis<int:id>',views.deletedis),
    path('delprc<int:id>',views.delprc),
    path('authorized.html',views.authorized, name='Authorized'),
    path('accept<int:F_id>',views.accept, name='accept'),
    path('authorized<int:F_id>',views.reject, name='reject'), 
] #+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
