"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("photo.urls")),
    path("accounts/", include("accounts.urls")),
    # path("__debug__/", include("debug_toolbar.urls")),
]

# Debug 모드를 사용하므로 static 기능을 사용한다. 실제로 서버작업을 할 때는 불필요한 작업
# 실제 작업:
# 1. 미디어 파일 서버를 별도로 두고 사용한다.
# 2. 웹서버(nginx, apache 등)에서 별도로 서빙 설정을 한다.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
