"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 25 12:48:15 2020"
__copyright__ = "©2020 rahul_kumar"

"""

from django.urls import path, include
from movieticket.views import *

urlpatterns = [
        path('user/registration/', include('rest_auth.registration.urls')),
        path('user/', include('rest_auth.urls')),
        path('movie/', MovieView.as_view(), name="movie"),
        path('theatre/', TheatreView.as_view(), name="theatre"),
        path('show/', ShowView.as_view(), name="show"),
        path('seat/', SeatView.as_view(), name="seat"),
        path('get_movie_by_city/', MovieByCity.as_view(), name="moviesincity"),
        path('movie_show_info/', SearchAMovie.as_view(), name="search_a_movie"),
        path('seat_availability/', GetSeatAvailability.as_view(), name="seat_availability"),
        path('booked_ticked/', BookedTicked.as_view(), name="booked_ticked"),
    ]