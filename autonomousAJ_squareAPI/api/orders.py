# autonomousAJ_squareAPI/autonomousAJ_squareAPI/api/orders.py
# Endpoint: orders
# URL: {'proper_name': 'Orders', 'url': 'https://connect.squareup.com/v2/orders'}
from .base import Square_API_Base

class orders(Square_API_Base):
    def get_orders(self):
        url = "{'proper_name': 'Orders', 'url': 'https://connect.squareup.com/v2/orders'}"
