"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 25 13:40:10 2020"
__copyright__ = "©2020 rahul_kumar"

"""

from rest_framework import serializers
from movieticket.models import Movie, Theatre, BookedSeat, Seat, Show


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class BookedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = "__all__"


