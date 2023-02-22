from fastapi import FastAPI
from routers import population 

app = FastAPI()

app.include_router(population.router)
