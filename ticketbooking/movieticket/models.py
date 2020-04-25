"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 25 14:26:18 2020"
__copyright__ = "©2020 rahul_kumar"

"""

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime


class Theatre(models.Model):
    city_choice=(
        ('Delhi','Delhi'),
        ('Kolkata','Kolkata'),
        ('Mumbai','Mumbai'),
        ('Chennai','Chennai'),
        ('Bangalore','Bangalore'),
        ('Hyderabad','Hyderabad'),
    )
    name = models.CharField(max_length=50,null=False,default="VIP")
    city = models.CharField(max_length=9,choices=city_choice,null=False)
    address = models.TextField()
    no_of_screen = models.IntegerField()


class Movie(models.Model):
    lang_choice = (
        ('English', 'English'),
        ('Bengali', 'Bengali'),
        ('Hindi', 'Hindi'),
        ('Tamil', 'Tamil'),
        ('Telugu', 'Telugu'),
    )
    name = models.CharField(max_length=20)
    cast = models.CharField(max_length=100,null=True,blank=True)
    director = models.CharField(max_length=20,null=True,blank=True)
    language = models.CharField(max_length=10, choices=lang_choice)
    run_length = models.IntegerField(help_text="Enter run length in minutes",null=True,blank=True)

    class Meta:
        unique_together = ('name', 'language')


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE,null=True,blank=True)
    screen = models.IntegerField(default=1)
    show_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        unique_together = ('screen', 'show_time')


class Seat(models.Model):
    seat_choice = (
        ('', 'Select'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Platinum', 'Platinum'),
    )
    total_seats = models.IntegerField()
    seat_type = models.CharField(max_length=8, choices=seat_choice, blank=False)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('show', 'seat_type')


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="booked_seat")
    selected_seat = models.IntegerField()
    booked_date = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        unique_together = ('seat', 'booked_by')