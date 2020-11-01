from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect

urlpatterns = [
    url(r'^add-booking/$',views.AddBooking),
]