from django.contrib import admin
from django.urls import path, include, re_path
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from backend import settings
from django.conf.urls.static import static
from backend.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns+=[
    re_path(r'^(?:.*)/?$',index,name='index')
]