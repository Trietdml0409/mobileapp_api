from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello world"}


#Getting the current user, this is the fixed path
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


#Return an Id with {user_id} passed in
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}