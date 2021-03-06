from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone

from datetime import datetime

from api.models import *
from api.documents import BookingDocument

import sys
import logging
import json
import requests
import hashlib
import threading
import math
import random

logger = logging.getLogger(__name__)

class AddBookingAPI(APIView):

    def post(self, request, *args, **kwargs):
        response = {}
        resp_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        try:

            data = request.data
            logger.info("AddBookingAPI: %s", str(data))
            if not isinstance(data, dict):
                data = json.loads(data)

            id = data["id"]
            user_id = data["user_id"]
            vehicle_model_id = data["vehicle_model_id"]

            package_id = data.get("package_id")
            if package_id is not None:
                package_id = int(float(package_id))

            travel_id = data.get("travel_id")
            if travel_id is not None:
                travel_id = int(float(travel_id))

            from_area_id = int(float(data["from_area_id"]))

            to_area_id = data.get("to_area_id")
            if to_area_id is not None:
                to_area_id = int(float(to_area_id))

            from_city_id = data.get("from_city_id")
            if from_city_id is not None:
                from_city_id = int(float(from_city_id))

            to_city_id = data.get("to_city_id")
            if to_city_id is not None:
                to_city_id = int(float(to_city_id))

            from_date = datetime.strptime(data["from_date"], '%m/%d/%Y %H:%M')

            to_date = data.get("to_date")
            if to_date is not None:
                to_date = datetime.strptime(to_date, '%m/%d/%Y %H:%M')

            online_booking = bool(data["online_booking"])
            mobile_site_booking = bool(data["mobile_site_booking"])

            booking_created = datetime.strptime(
                data["booking_created"], '%m/%d/%Y %H:%M')

            from_lat = float(data["from_lat"])
            from_long = float(data["from_long"])

            to_lat = data.get("to_lat")
            if to_lat is not None:
                to_long = float(to_lat)

            to_long = data.get("to_long")
            if to_long is not None:
                to_lat = float(to_long)

            car_cancellation = bool(data["Car_Cancellation"])

            created = Booking.objects.filter(pk=id).exists()

            if created == False:
                booking_obj = Booking.objects.create(
                    id=id,
                    user_id=user_id,
                    vehicle_model_id=vehicle_model_id,
                    package_id=package_id,
                    travel_id=travel_id,
                    from_area_id=from_area_id,
                    to_area_id=to_area_id,
                    from_city_id=from_city_id,
                    to_city_id=to_city_id,
                    from_date=from_date,
                    to_date=to_date,
                    online_booking=online_booking,
                    mobile_booking=mobile_site_booking,
                    booking_created=booking_created,
                    from_lat=from_lat,
                    from_long=from_long,
                    to_lat=to_lat,
                    to_long=to_long,
                    car_cancellation=car_cancellation,
                )

                resp_status = status.HTTP_201_CREATED
                response['id'] = str(booking_obj.id)

            else:
                response["message"] = "RESOURCE ALREADY EXISTS"
                resp_status = status.HTTP_403_FORBIDDEN

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error("AddBookingAPI: %s at %s", e, str(exc_tb.tb_lineno))

        return Response(data=response, status=resp_status)

class DeleteBookingAPI(APIView):

    def post(self, request, *args, **kwargs):
        response = {}
        resp_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        try:

            data = request.data
            logger.info("DeleteBookingAPI: %s", str(data))
            if not isinstance(data, dict):
                data = json.loads(data)

            id = data["id"]
            created = Booking.objects.filter(pk=id).exists()
            if created == True:
                booking_obj = Booking.objects.get(pk=id)
                booking_obj.delete()
                resp_status = status.HTTP_200_OK

            else:
                resp_status = status.HTTP_400_BAD

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error("DeleteBookingAPI: %s at %s", e, str(exc_tb.tb_lineno))

        return Response(data=response, status=resp_status)

AddBooking = AddBookingAPI.as_view()

DeleteBooking = DeleteBookingAPI.as_view()
