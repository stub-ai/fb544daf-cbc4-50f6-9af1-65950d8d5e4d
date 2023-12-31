from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schools/', include('schools.urls')),
    path('products/', include('products.urls')),
]