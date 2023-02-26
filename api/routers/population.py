from fastapi import APIRouter
from database.conexion import db
from bson import json_util
from json import loads

router = APIRouter()

def resultado(res):
     return loads(json_util.dumps(res))
'''
@router.get("/districts/{year}")
def get_district(year):
    population = db.population
    pipeline = [
    {"$match": {"Year": {"$eq":year}}},
    {"$unwind": "$District"},
    {"$project":{"_id":0}}
    ]
    unwind_population = list(population.aggregate(pipeline))
    res = unwind_population
  
    return resultado(res)
'''

@router.get("/districts/{year}")
def get_district(year):
    population = db.population
    pipeline = [
    {"$match": {"Year": {"$eq":year}}},
    {"$project":{"_id":0}}
    ] #Ojo borro el unwind, em principio no lo necesito.
    unwind_population = list(population.aggregate(pipeline))
    res = unwind_population
    return resultado(res)