from fastapi import APIRouter
from database.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def resultado(res):
     return loads(json_util.dumps(res))


@router.get("/districts/{year}")
def get_district(year):
    population = db.population
    pipeline = [
    {"$match": {"Year": {"$eq":year}}},
    {"$project":{"_id":0, "Year":1, "District":1, "Neighborhood":1, "Gender":1, "Number":1,}}
    ] 
    res= list(population.aggregate(pipeline))
    return resultado(res)

@router.get("/neighborhood/{year}")
def get_neighborhood(year):
    population = db.population
    pipeline = [
    {"$match": {"Year": {"$eq":year}}},
    {"$project":{"_id":0, "Year":1,"District":1, "Neighborhood":1, "Gender":1, "Number":1,}}
    ] 
    res= list(population.aggregate(pipeline))
    return resultado(res)