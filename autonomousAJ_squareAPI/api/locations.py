# autonomousAJ_squareAPI/autonomousAJ_squareAPI/api/locations.py
# Endpoint: locations
# URL: {'proper_name': 'Locations', 'url': 'https://connect.squareup.com/v2/locations'}
from .base import Square_API_Base

class locations(Square_API_Base):
    def get_locations(self):
        url = "{'proper_name': 'Locations', 'url': 'https://connect.squareup.com/v2/locations'}"
