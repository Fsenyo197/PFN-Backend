from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from cloudinary.uploader import upload as cloudinary_upload

@csrf_exempt
def summernote_image_upload(request):
    """
    Handle Summernote image uploads with Cloudinary.
    """
    if request.method == 'POST':
        try:
            # Get the uploaded image from the request
            image = request.FILES.get('file')
            if not image:
                return JsonResponse({'error': 'No image provided.'}, status=400)
            
            # Upload the image to Cloudinary
            upload_result = cloudinary_upload(image)
            
            # Return the secure Cloudinary URL for Summernote to use
            return JsonResponse({'url': upload_result.get('secure_url')})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
