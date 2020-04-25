"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 25 14:26:18 2020"
__copyright__ = "©2020 rahul_kumar"

"""

import logging
from movieticket.models import *


class Query:
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_movie_by_cityname(city):
        """
        This function returns movie list of dict

        :param city:
        :return:
        """
        try:
            show_list = Show.objects.filter(theatre__city__iexact=city).values("theatre__city",
                                                                               "movie__name",
                                                                               "movie__cast",
                                                                               "movie__language",
                                                                               "screen",
                                                                               "theatre__name",
                                                                               "theatre__address")
            for data in show_list:
                data["city"] = data.pop("theatre__city")
                data["movie"] = data.pop("movie__name")
                data["cast"] = data.pop("movie__cast")
                data["language"] = data.pop("movie__language")
                data["address"] = data.pop("theatre__address")
                data["theatre"] = data.pop("theatre__name")
            return show_list
        except Exception as e:
            Query.logger.error(str(e))

    @staticmethod
    def search_a_movie(movie):
        """
        This function returns a movie info

        :param movie:
        :return:
        """
        movie_show_details = []
        try:
            movie_show_details = Show.objects.filter(movie=int(movie)).values("show_time", "id",
                                                                              "movie__name", "movie__cast",
                                                                              "movie__language", "movie__run_length",
                                                                              "theatre__name", "theatre__address",
                                                                              "screen", "movie__id", "theatre__id")
            for data in movie_show_details:
                data["theatre_name"] = data.pop("theatre__name")
                data["movie_name"] = data.pop("movie__name")
                data["language"] = data.pop("movie__language")
                data["movie_length"] = data.pop("movie__run_length")
                data["address"] = data.pop("theatre__address")
                data["cast"] = data.pop("movie__cast")
                data["movie_id"] = data.pop("movie__id")
                data["theatre_id"] = data.pop("theatre__id")
                data["show_id"] = data.pop("id")
        except Exception as e:
            Query.logger.error(str(e))
        return movie_show_details

    @staticmethod
    def get_seat_availability(show):
        """
        This funtion returns seat availability info

        :param show:
        :return:
        """
        try:
            seat_availability = Seat.objects.filter(show=int(show)).values("show",
                                                                      "seat_type",
                                                                      "total_seats")
            for data in seat_availability:
                data["available_seat"] = data.pop("total_seats")
        except Exception as e:
            seat_availability = []
            Query.logger.error(str(e))
        return seat_availability

    @staticmethod
    def seat_book(no_of_seats, show, seat_type, user):
        """
        This function book a seat

        :param no_of_seats:
        :param show:
        :param seat_type:
        :return:
        """
        try:
            no_of_seats = int(no_of_seats)
            seat_total = Seat.objects.filter(show=show, seat_type=seat_type).values("total_seats", "id")
            seat_id = int(seat_total[0]["id"])
            remaining_seats = seat_total[0]["total_seats"]
            if no_of_seats > remaining_seats:
                status = "Sorry! seats are not available!"
            else:
               try:
                       BookedSeat.objects.get(seat=seat_id)
                       status = "Selected seat already booked!"
               except BookedSeat.DoesNotExist:
                   seat = Seat.objects.get(pk=seat_id)
                   BookedSeat.objects.create(booked_by=user, selected_seat=no_of_seats, seat=seat)
                   pending_seats = remaining_seats - no_of_seats
                   Seat.objects.filter(pk=seat_id).update(total_seats=pending_seats)
                   show_details = Show.objects.filter(pk=show).values("show_time",
                                                                        "movie__name",
                                                                        "theatre__name",
                                                                        "theatre__address",
                                                                        "screen")
                   show_details[0]["movie_name"] = show_details[0].pop("movie__name")
                   show_details[0]["theatre_name"] = show_details[0].pop("theatre__name")
                   show_details[0]["address"] = show_details[0].pop("theatre__address")
                   show_details[0]["seat_id"] = seat_id
                   show_details[0]["booked_by"] = user.username
                   show_details[0]["no_of_seats"] = no_of_seats
                   status = show_details
        except Exception as e:
            status = "Requested seat or show does not exists!"
            Query.logger.info(str(e))
        return status