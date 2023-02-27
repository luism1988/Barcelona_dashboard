from fastapi import APIRouter
from database.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def resultado(res):
     return loads(json_util.dumps(res))

@router.get("/district/map")
def get_coordinates_districts():
    coordinates_districts = db.coordinates_districts
    #filt = {}
    #project ={"_id":0,"Name":1,"latitude":1,"Longitude":1}
    res = list(coordinates_districts.find({}))
    resultado(res)


