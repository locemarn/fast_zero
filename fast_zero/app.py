"""Module"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    """hello world function"""
    return {'message': 'Hello World!'}
