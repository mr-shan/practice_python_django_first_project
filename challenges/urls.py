from django.urls import path
from . import views

urlpatterns = [
    # these are static URLs.
    # path("january", views.january),

    # for all blank URLs this will be called.
    path("", views.hello_world),

    # These are dynamic URLs, the dynamic parameter is linked to month
    # <month> acts like a keyword arguments
    # The type conversion plays the role of taking care of dynamic paramters datatypes.
    # if it's number, first will be called
    # if it's a string, second will be called.
    # the order here matters since all the numbers can be strings
    # other types supported: slug, uuid, path (https://docs.djangoproject.com/en/3.1/topics/http/urls/#path-converters)
    path("<int:month_index>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge),
]
