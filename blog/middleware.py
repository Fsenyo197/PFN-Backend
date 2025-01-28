from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from blog.models.apikeys_model import APIKey
from django.contrib.auth import logout
from django.utils import timezone
from django.conf import settings
from datetime import timedelta


class SessionTimeoutMiddleware:
    """
    Middleware to ensure the session expires after a specific inactivity period.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Retrieve last activity timestamp from the session
        last_activity = request.session.get('last_activity')

        if last_activity:
            try:
                last_activity = timezone.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S')
                inactivity_duration = timezone.now() - timezone.make_aware(last_activity)

                if inactivity_duration > timedelta(seconds=settings.SESSION_COOKIE_AGE):
                    # Session has expired, force logout
                    if request.user.is_authenticated:
                        logout(request)
                    request.session.flush()
            except ValueError:
                # Handle invalid or missing last_activity value
                request.session.flush()

        # Update the last activity timestamp if the user is authenticated
        if request.user.is_authenticated:
            request.session['last_activity'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')

        return self.get_response(request)


class APIKeyAuthMiddleware(MiddlewareMixin):
    """
    Middleware for authenticating requests using API keys and secrets.
    """

    def process_request(self, request):
        # Resolve the current URL to skip admin and Summernote routes
        resolved_url = resolve(request.path_info)

        # Skip authentication for admin and Summernote routes
        if 'summernote' in resolved_url.route or 'admin' in resolved_url.route:
            return None

        # Retrieve API key and secret from request headers
        api_key = request.headers.get("X-API-Key")
        api_secret = request.headers.get("X-API-Secret")

        if not api_key or not api_secret:
            return JsonResponse({"error": "Missing API key or secret."}, status=400)

        try:
            # Validate the API key and secret
            api_key_obj = APIKey.objects.get(key=api_key, secret=api_secret, is_active=True)
        except APIKey.DoesNotExist:
            return JsonResponse({"error": "Invalid or inactive API key or secret."}, status=401)

        # Attach the authenticated user to the request object
        request.user = api_key_obj.user
        return None
