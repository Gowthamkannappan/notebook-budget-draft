from django.urls import path

urlpatterns =[
    path('signin/',name="Signin"),                          #. Sign In Page
    path('signup/',name='Signup'),                          #. Sign UP Page
    path('update-profile/',name='Update Profile')           #. Update Profile Page
]