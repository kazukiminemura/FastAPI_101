from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    is_active: bool
    
users = [
  User(username="alice", is_active=True),
  User(username="bob", is_active=False),
  User(username="charlie", is_active=True)
]

def get_active_users():
    active_users = [user for user in users if user.is_active]
    print("Active users fetched")
    return activate_users

@app.get("/active")
async def list_active_users(active_users: list[User] = Depends(get_active_users)):
    print("Endpoint /active called")
    return active_users