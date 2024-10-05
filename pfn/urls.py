from django.contrib import admin
from django.urls import include, path
from blog.views import tinymce_image_upload  # Import the view

urlpatterns = [
    path('api/v1/', include('blog.api.v1.routers.routers')),
    path('admin/', admin.site.urls),
    path('tinymce/upload_image/', tinymce_image_upload, name='tinymce_image_upload'),  # Map the URL to the view
]

# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "PFN Admin"
admin.site.site_title = "PFN Admin Portal"
admin.site.index_title = "Welcome to Prop Firm News Portal"
