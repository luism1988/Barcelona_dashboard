import re
import requests


def get_all(year):
    return requests.get(f"http://127.0.0.1:8000/all/{year}").json()


def get_district_coordinates():
    return requests.get(f"http://127.0.0.1:8000/map/districts").json()


def get_neighborhood_coordinates():
    return requests.get(f"http://127.0.0.1:8000/map/neighborhood").json()
