from fastapi import FastAPI
from routers import population, district_coordinates

app = FastAPI()

app.include_router(population.router)
app.include_router(district_coordinates.router)
