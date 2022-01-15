from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('prod/', include('product.urls')),
    path('', include('user.urls')),
    path('admin/', admin.site.urls),
]
