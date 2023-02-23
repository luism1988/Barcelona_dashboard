import re
import requests
def get_district(year):
    return requests.get(f"http://127.0.0.1:8000/district/{year}").json()

def get_district_coordinates():
    return requests.get(f"http://127.0.0.1:8000//district/map").json()
