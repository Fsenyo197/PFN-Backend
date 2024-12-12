from django.urls import path
from blog.two_factor.views import generate_otp, verify_otp

app_name = "two_factor"

urlpatterns = [
    path('generate/', generate_otp, name='generate_otp'),
    path('verify/', verify_otp, name='verify_otp'),
]
