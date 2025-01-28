from django.contrib import admin
from django.urls import include, path
from blog.views import summernote_image_upload

urlpatterns = [
    path('api/v1/', include('blog.api.v1.routers.routers')),
    path('admin/', admin.site.urls),
    path('summernote/upload_image/', summernote_image_upload, name='summernote_image_upload'),
    path('summernote/', include('django_summernote.urls')),
]


# Customize Django admin interface
admin.site.site_header = "PFN Admin"
admin.site.site_title = "PFN Admin Portal"
admin.site.index_title = "Welcome to Prop Firm News Portal"
