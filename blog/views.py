# blog/views.py

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from cloudinary.uploader import upload as cloudinary_upload
from django.conf import settings

@csrf_exempt
def tinymce_image_upload(request):
    if request.method == 'POST':
        try:
            image = request.FILES.get('file')
            if not image:
                return JsonResponse({'error': 'No image provided.'}, status=400)
            
            upload_result = cloudinary_upload(image)
            return JsonResponse({'location': upload_result.get('secure_url')})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
