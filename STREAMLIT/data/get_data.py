import re
import requests

def get_district(year):
    return requests.get(f"http://127.0.0.1:8000/districts/{year}").json()

def get_district_coordinates():
    return requests.get(f"http://127.0.0.1:8000//district/map").json()

def get_district2(year):
    return requests.get(f"http://127.0.0.1:8000/districts2/{year}").json()
