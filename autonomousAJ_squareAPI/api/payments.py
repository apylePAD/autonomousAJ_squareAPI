# autonomousAJ_squareAPI/autonomousAJ_squareAPI/api/payments.py
# Endpoint: payments
# URL: {'proper_name': 'Payments', 'url': 'https://connect.squareup.com/v2/payments'}
from .base import Square_API_Base

class payments(Square_API_Base):
    def get_payments(self):
        url = "{'proper_name': 'Payments', 'url': 'https://connect.squareup.com/v2/payments'}"
