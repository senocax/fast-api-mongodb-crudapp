from bson import ObjectId
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity

student_router = APIRouter()


@student_router.get("/Hello")
async def helloWorld():
    return "Hello world"


@student_router.get("/students")
async def findAllStudent():
    return connection.local.student.find()


@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


@student_router.post('/student')
async def createStudent(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())


@student_router.put('/student/{studentId}')
async def update_student(studentId, student: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)},
        {"$set": dict(student)}
    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))


@student_router.delete('/student/{studentId}')
async def delete_student(studentId):
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
