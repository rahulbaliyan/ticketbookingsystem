Movieticket Django Application(Django version 2.0)
====


Building
=========

Requirements:
======================
python 3.6

To run this project at your env please follow the steps:
=======================================================
Note:- Recommended OS is linux
1.Go to in project dir
2.Create a virtual env or conda env at your system to install packages(It will not effect your whole system env.)
3.Install requirements.txt for installation dependency packages($ pip install -r requirements.txt)
4.see the .env file and set the logpath, logpath is required to maintain errors and information.
And in this project I am using default django database sqlite , You can configure a new database in settings.py file in database section.

5. Run the command ($ python manage.py migrate) to create django auth tables and installed app tables in db.
6. Run the command ($ python manage.py makemigrations movieticket) to be create schema of the application models.
7. Run the command ($ python manage.py migrate movieticket) to be chnages in database
8. create a admin account(python manage.py createsuperuser)
9.After create a admin account follow these step--
-- go to terminal in your project dir.
Note:It just a manual steps , we can modify later.
These step required to create a token of admin profile-
-- $python manage.py shell
--from rest_framework.authtoken.models import Token
--from django.contrib.auth.models import User
--user = User.objects.get(username=your_admin_username)
--Token.objects.create(user=user)

Great!!! all are set Now you can play with the apis-
===========================================================================
Important Note:- I configure all the models of movieticket application in admin panel. So you can perform CURD operation by admin panel
Admin url - /admin/
===========================================================================
Api Urls:
=================================
Note: Look into the excel for request and response json and header.
===========================================================
1./user/login/   (this url uses for login a user it will return a token_id which is useful for apis)
2./user/registration/  (if user not exists you can create a new user)
3./show/ (to add and get show details) only admin can do this operation.
4./seat/ (to add and get seat details) only admin can do this operation.
5./movie/ (to add and get movie details) only admin can do this operation.
6./theatre/ (to add and get theatre details) only admin can do this operation.
7./get_movie_by_city/?city=delhi (to get all movies in a selected city.) This api anyone can hit.
8./movie_show_info/?movie_id=1 (to get a selected movie information like show detatils.)  This api anyone can hit.
9./seat_availability/?show_id=1 (to get seat_availability of a selected show)  This api anyone can hit.
10./booked_ticked/ (to book a movieticket) This operation only perform by authenticated user.movieticket.movieticket
=============================================================
Licensing
========
*****