from django.db import models
from django.contrib.auth.models import User
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

import sys
import json
import uuid


class Booking(models.Model):

    id = models.CharField(max_length=200, primary_key=True)
    user_id = models.IntegerField()
    vehicle_model_id = models.IntegerField()

    PACKAGE_TYPE = (
        (1, "4HRS-40KMS"),
        (2, "8HRS-80KMS"),
        (3, "6HRS-60KMS"),
        (4, "10HRS-100KMS"),
        (5, "5HRS-50KMS"),
        (6, "3HRS-30KMS"),
        (7, "12HRS-120KMS")
    )

    package_id = models.IntegerField(
        blank=True, null=True, choices=PACKAGE_TYPE)

    TRAVEL_TYPE = (
        (1, "LONG_DISTANCE"),
        (2, "POINT_TO_POINT"),
        (3, "HOURLY_RENTAL"),
    )

    travel_id = models.IntegerField(blank=True, null=True, choices=TRAVEL_TYPE)
    from_area_id = models.IntegerField()
    to_area_id = models.IntegerField(blank=True, null=True)
    from_city_id = models.IntegerField(blank=True, null=True)
    to_city_id = models.IntegerField(blank=True, null=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField(blank=True, null=True)
    online_booking = models.BooleanField(default=True)
    mobile_booking = models.BooleanField(default=False)
    booking_created = models.DateTimeField()
    from_lat = models.DecimalField(max_digits=9, decimal_places=6)
    from_long = models.DecimalField(max_digits=9, decimal_places=6)
    to_lat = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    to_long = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True)
    car_cancellation = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if self.id == None or self.id == "":
            self.id = str(uuid.uuid4())

        super(Booking, self).save(*args, **kwargs)

# Create your models here.
