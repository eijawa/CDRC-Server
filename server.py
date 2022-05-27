from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

clients = {}

class Client(BaseModel):
  name: str
  address: str
  tvs_count: int
  ip: str

@app.put("/register")
async def register_client(client: Client):
  print(client)
  return 1