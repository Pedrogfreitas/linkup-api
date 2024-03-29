from fastapi import FastAPI
from api.routes import post_routes, user_routes

app = FastAPI()

app.include_router(post_routes.router)
app.include_router(user_routes.router)
