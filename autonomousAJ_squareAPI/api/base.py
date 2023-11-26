# autonomousAJ_squareAPI/autonomousAJ_squareAPI/api/base.py
from autonomousAJ_squareAPI.auth import square_client
import requests

class Square_API_Base:
    def get_square_client(self):
        return square_client()

