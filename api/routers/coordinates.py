from fastapi import APIRouter
from database.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def resultado(res):
     return loads(json_util.dumps(res))

@router.get("/map/districts")
def get_coordinates_districts():
    coordinates_districts = db.coordinates_districts
    filt = {}
    project ={"_id":0}
    res = list(coordinates_districts.find(filt,project))
    return resultado(res)

@router.get("/map/neighborhood")
def get_coordinates_neighborhood():
    coordinates_Neighborhood = db.coordenadas_Neighborhood 
    filt = {}
    project ={"_id":0}
    res = list(coordinates_Neighborhood.find(filt,project))
    return resultado(res)

