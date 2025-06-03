from fastapi import FastAPI
from ddtrace import patch_all
from ddtrace.contrib.asgi import TraceMiddleware
from logger import logger

patch_all()

app = FastAPI()
app.add_middleware(TraceMiddleware, service="fastapi-app")

@app.get("/users")
def get_users():
    logger.info("Getting users list")
    return [{"id": 1, "name": "Alice"}]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    logger.info(f"Getting user with ID: {user_id}")
    return {"id": user_id, "name": "Example"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    logger.info(f"Deleting user with ID: {user_id}")
    return {"status": "deleted", "id": user_id}
