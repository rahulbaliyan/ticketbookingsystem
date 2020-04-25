"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 25 14:26:18 2020"
__copyright__ = "©2020 rahul_kumar"

"""

from django.apps import apps
from django.contrib import admin

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass