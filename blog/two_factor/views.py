from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from django.conf import settings
from blog.two_factor.OTP_model import OTP
from django.contrib.auth.models import User
import random


def generate_otp(request):
    """
    Generate a One-Time Password (OTP) for 2FA and send it to the user's email.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

    # Get the username from the request
    username = request.POST.get("username")
    user = get_object_or_404(User, username=username)

    # Generate a random 6-digit OTP
    otp_code = f"{random.randint(100000, 999999)}"

    # Create or update the OTP object for the user
    otp, created = OTP.objects.update_or_create(
        user=user,
        defaults={
            "code": otp_code,
            "created_at": now(),
        }
    )

    # Send OTP to the user's email
    send_mail(
        subject="Your Two-Factor Authentication Code",
        message=f"Your OTP code is {otp_code}. It will expire in 10 minutes.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

    return JsonResponse({"message": "OTP has been sent to your email."})


def verify_otp(request):
    """
    Verify the OTP provided by the user.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

    # Get username and OTP from the request
    username = request.POST.get("username")
    otp_code = request.POST.get("otp")

    if not username or not otp_code:
        return JsonResponse({"error": "Username and OTP are required."}, status=400)

    # Fetch the user and their OTP
    user = get_object_or_404(User, username=username)
    try:
        otp = OTP.objects.get(user=user)
    except OTP.DoesNotExist:
        return JsonResponse({"error": "OTP has expired or does not exist."}, status=401)

    # Check if the provided OTP matches and is not expired
    if otp.code != otp_code:
        return JsonResponse({"error": "Invalid OTP."}, status=401)
    if otp.is_expired():
        return JsonResponse({"error": "OTP has expired."}, status=401)

    # OTP is valid, proceed to the next step (e.g., log the user in)
    otp.delete()
    return JsonResponse({"message": "OTP verified successfully."})
