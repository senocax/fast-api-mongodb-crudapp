from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

clients_app = ['http://localhost/3000']

app = FastAPI()
app.include_router(student_router)

app.add_middleware(CORSMiddleware,
                   allow_origins=clients_app,
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*']
                   )