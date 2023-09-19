from fastapi import Body, FastAPI, Path
from starlette.requests import Request
from typing import Optional
from pydantic import BaseModel
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import dbConnect as db
import getnewsquery as gnq

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

class User(BaseModel):
    username : str
    userEmail : str
    userPassword : str

app = FastAPI(middleware=middleware)

@app.get("/")
def index():
    return

@app.get("/get-all-records/")
def get_all_records():
    return db.getAllRecords()

@app.post("/get-user-info/")
def get_user_info(userId : str = Body(..., description="The user ID of the user whose data you want to retrieve")):
    return db.getUserInfo(userId)

@app.post("/create-record/")
def create_record(userDetails : User):
    jsonData = {"username": userDetails.username, "userEmail": userDetails.userEmail, "userPassword": userDetails.userPassword}
    return db.createRecord(jsonData)

@app.post("/update-record/")
def update_record(userDetails : User, userID: str = Body(..., description="The user ID of the user you want to update")):
    jsonData = {"userID": userID, "username": userDetails.username, "userEmail": userDetails.userEmail, "userPassword": userDetails.userPassword}
    return db.updateRecord(jsonData)

@app.post("/delete-record/")
def delete_record(userID: str = Body(..., description="The user ID of the user you want to delete")):
    return db.deleteRecord(userID)

@app.post("/login/")
def login(username: str = Body(..., description="The username of the user you want to login"), userPassword: str = Body(..., description="The password of the user you want to login")):
    return db.verifyUser(username, userPassword)


#API to return criminal news from a given latitude and longitude
@app.post("/get-news/")
def get_news(latitude: float = Body(..., description="The latitude of the location you want to get news for"), longitude: float = Body(..., description="The longitude of the location you want to get news for")):
    return gnq.return_news(latitude, longitude)



