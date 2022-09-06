from fastapi import FastAPI
from src.routers import users


app = FastAPI()
# app.include_router(users.router)
app.include_router(
    users.router,
    prefix="/v1/users",
    tags=["v1 users"],
    responses={418: {"description": "MY ERROR"}},
)

if __name__ == "__main__":
    #TODO
    uvicorn.run(app='src.main:app', host='0.0.0.0',reload='True', debug=True)