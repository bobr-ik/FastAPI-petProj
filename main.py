from fastapi import FastAPI, Body
from pydantic import EmailStr, BaseModel
import uvicorn

app = FastAPI()

class Create_user(BaseModel):
    email: EmailStr


@app.get('/path')
def greet():
    return 'Hello, World'



@app.get('/check_email')
def check_email(user: Create_user):
    return 'Всё ок, ваш email: ' + user.email



if  __name__ == '__main__':
    uvicorn.run('main:app', reload=True)