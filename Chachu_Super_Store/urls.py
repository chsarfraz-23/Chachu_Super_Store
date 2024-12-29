from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Chachu_Super_Store import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
    path("", include("rest_framework.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
