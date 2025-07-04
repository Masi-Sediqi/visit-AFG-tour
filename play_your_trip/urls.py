from django.urls import path
from .import views


app_name = 'plan_your_trip'

urlpatterns = [
    path('visa_guide', views.visa_guide, name="visa_guide"),
    path('essentials', views.essentials, name="essentials"),
    path('flight', views.flight, name="flight"),
    path('Accommodation', views.Accommodation, name="Accommodation"),
    path('Getting_to_around_afg', views.Getting_to_around_afg, name="Getting_to_around_afg"),
    path('safety', views.safety, name="safety"),
    path('weather', views.weather, name="weather"),
    path('currency', views.currency, name="currency"),
    path('accessibility', views.accessibility, name="accessibility"),
    path('afghanistan_attractions_passes', views.afghanistan_attractions_passes, name="afghanistan_attractions_passes"),
]