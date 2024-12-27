from pydantic import BaseModel

class CreateUser:
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser:
    firstname: str
    lastname: str
    age: int

class CreateTask:
    titl: str
    content: str
    age: int

class UpdateTask:
    titl: str
    content: str
    age: int
