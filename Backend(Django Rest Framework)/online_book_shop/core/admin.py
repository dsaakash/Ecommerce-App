from django.contrib import admin

from .models import User

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import  CustomUserCreationForm
# Register your models here.

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#      add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username','email' 'password1', 'password2'),
#         }),
#     )
     
     
     
     
     
     
    
     
     
   # what we got errror
   
  
#    FieldError at /admin/core/user/add/
# Unknown field(s) (emailpassword1) specified for User. Check fields/fieldsets/exclude attributes of class UserAdmin.
# Request Method:	GET
# Request URL:	http://127.0.0.1:8000/admin/core/user/add/
# Django Version:	3.1.4
# Exception Type:	FieldError
# Exception Value:	
# Unknown field(s) (emailpassword1) specified for User. Check fields/fieldsets/exclude attributes of class UserAdmin.
# Exception Location:	D:\Projects\Flutter_Projects\ecom_flutter_django\Ecommerce-App\Backend(Django Rest Framework)\env_django\Lib\site-packages\django\contrib\admin\options.py, line 711, in get_form
# Python Executable:	D:\Projects\Flutter_Projects\ecom_flutter_django\Ecommerce-App\Backend(Django Rest Framework)\env_django\Scripts\python.exe
# Python Version:	3.11.8
# Python Path:	
# ['D:\\Projects\\Flutter_Projects\\ecom_flutter_django\\Ecommerce-App\\Backend(Django '
#  'Rest Framework)\\online_book_shop',
#  'D:\\python3.11.5\\python311.zip',
#  'D:\\python3.11.5\\DLLs',
#  'D:\\python3.11.5\\Lib',
#  'D:\\python3.11.5',
#  'D:\\Projects\\Flutter_Projects\\ecom_flutter_django\\Ecommerce-App\\Backend(Django '
#  'Rest Framework)\\env_django',
#  'D:\\Projects\\Flutter_Projects\\ecom_flutter_django\\Ecommerce-App\\Backend(Django '
#  'Rest Framework)\\env_django\\Lib\\site-packages']
# Server time:	Wed, 29 May 2024 10:53:47 +0000
   
   
   
   
    
    #  In order to solvw this issue 
    
    
    # create an forms.py 
    
    
    # add  it in admin.py
    
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    
    
    
    
    
    #  then make  migrations command
    # then  migrate
    