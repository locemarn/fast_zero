"""Module"""
from http import HTTPStatus

from fastapi import FastAPI # type: ignore

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """hello world function"""
    return {'message': 'Hello World!'}
