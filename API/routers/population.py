from fastapi import APIRouter
from database.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def resultado(res):
     return loads(json_util.dumps(res))

@router.get("/district/{year}")
def get_district(year):
    population = db.population
    pipeline = [
    {"$match": {"Year": {"$eq":year}}},
    {"$unwind": "$District"},
    {"$project":{"_id":0, "District.Name":1, "Number":1}}
    ]
    unwind_population = list(population.aggregate(pipeline))
    res = unwind_population
    return resultado(res)
