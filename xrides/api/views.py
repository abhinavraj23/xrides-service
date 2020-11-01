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

            uuid = data["uuid"]
            user_id = data["user_id"]
            vehicle_model_id = data["vehicle_model_id"]
            package_id = data["package_id"]
            travel_id = data["travel_id"]
            from_area_id = data["from_area_id"]
            to_area_id = data["to_area_id"]
            from_city_id = data["from_city_id"]
            to_city_id = data["to_city_id"]
            from_date = data["from_date"]
            to_date = data["to_date"]
            online_booking = data["online_booking"]
            mobile_booking = data["mobile_booking"]
            from_lat = data["from_lat"]
            from_long = data["from_long"]
            to_lat = data["to_lat"]
            to_long = data["to_long"]
            car_cancelation = data["car_cancelation"]

            booking_obj = Booking.objects.update_or_create(
                uuid=uuid,
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
                mobile_booking=mobile_booking,
                booking_created=booking_created,
                from_lat=from_lat,
                from_long=from_long,
                to_lat=to_lat,
                to_long=to_long,
                car_cancelation=car_cancelation,
            )

            response['uuid'] = str(booking_obj.uuid)
            resp_status = status.HTTP_201_CREATED

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error("AddBookingAPI: %s at %s", e, str(exc_tb.tb_lineno))

        return Response(data=response,status=resp_status)

AddBooking = AddBookingAPI.as_view()
