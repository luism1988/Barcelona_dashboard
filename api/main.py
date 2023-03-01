from fastapi import FastAPI
from routers import coordinates,population

app = FastAPI()

app.include_router(population.router)
app.include_router(coordinates.router)

@app.get("/")
def principal():
    return{
        "API Status" : "Working"
    }