"""Module"""

from http import HTTPStatus

from fastapi import FastAPI  # type: ignore

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """hello world function"""
    return {'message': 'Hello World!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    print('user_with_id ---->', user_with_id)
    database.append(user_with_id)
    return user_with_id
