from django.http import JsonResponse
from blog.models.apikeys_model import APIKey
from django.utils.deprecation import MiddlewareMixin

class APIKeyAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        api_key = request.headers.get('X-API-Key')
        api_secret = request.headers.get('X-API-Secret')

        if not api_key or not api_secret:
            return JsonResponse({"error": "Missing API key or secret."}, status=400)

        try:
            # Check if the API key and secret are valid and active
            api_key_obj = APIKey.objects.get(key=api_key, secret=api_secret, is_active=True)
        except APIKey.DoesNotExist:
            return JsonResponse({"error": "Invalid or inactive API key or secret."}, status=401)

        request.user = api_key_obj.user 
        return None 

