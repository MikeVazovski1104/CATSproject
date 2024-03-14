
from django.contrib import admin
from django.urls import include, path

from cats.views import GuestAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homecats/', include('cats.urls')),
    path('api/v1/guestlist', GuestAPIView.as_view()),

]
