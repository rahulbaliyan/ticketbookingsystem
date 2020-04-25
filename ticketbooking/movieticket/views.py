from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import generics
from movieticket.models import Movie, Theatre, Show, Seat
from movieticket.serializer import MovieSerializer, TheatreSerializer, SeatSerializer, ShowSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
import logging
from movieticket.query import Query
from rest_framework import status
logger = logging.getLogger(__name__)
# Create your views here.


class MovieView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class TheatreView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Theatre.objects.all()
    serializer_class = TheatreSerializer


class ShowView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class SeatView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


@permission_classes((AllowAny, ))
class MovieByCity(APIView):
    def get(self, request):
        show_list = []
        try:
            city = request.GET["city"]
            show_list = Query.get_movie_by_cityname(city)
            if not show_list:
                show_list = "Sorry! Currently no show is running in your city!"
        except Exception as e:
            logger.error(str(e))
        return Response(show_list)


@permission_classes((AllowAny, ))
class SearchAMovie(APIView):
    def get(self, request):
        try:
            movie = request.GET["movie_id"]
            show_list = Query.search_a_movie(movie)
            if not show_list:
                show_list = "Sorry! No movie found!"
        except Exception as e:
            logger.error(str(e))
            show_list = "Invalid request!"
        return Response(show_list)


@permission_classes((AllowAny, ))
class MovieByCity(APIView):
    def get(self, request):
        try:
            city = request.GET["city"]
            movie_info = Query.get_movie_by_cityname(city)
            if not movie_info:
                movie_info = "Sorry! Currently no show is running in your city!"
        except Exception as e:
            logger.error(str(e))
            movie_info = "Invalid request!"
        return Response(movie_info)


@permission_classes((AllowAny, ))
class GetSeatAvailability(APIView):
    def get(self, request):
        try:
            city = request.GET["show_id"]
            seat_availability = Query.get_seat_availability(city)
            if not seat_availability:
                seat_availability = "Sorry! No Show or seat available!"
        except Exception as e:
            logger.error(str(e))
            seat_availability = "Invalid request!"
        return Response(seat_availability)


class BookedTicked(APIView):
    def post(self, request):
        try:
            data = request.data
            user = request.user
            no_of_seats = data["no_of_seats"]
            seat_id = data["show_id"]
            seat_type = data["seat_type"]
            status = Query.seat_book(no_of_seats, seat_id, seat_type, user)
        except Exception as e:
            logger.error(str(e))
            status = "Invalid request!"
        return Response(status)

