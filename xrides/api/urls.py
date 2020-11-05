from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

from rest_framework.routers import SimpleRouter

from . import views
from . import views_es

router = SimpleRouter()

router.register(
    prefix=r'^bookings',
    basename='bookings',
    viewset=views_es.BookingViewSet
)


urlpatterns = [
    url(r'^add-booking/$',views.AddBooking),
    url(r'^delete-booking/$',views.DeleteBooking),
]

urlpatterns.extend(router.urls)