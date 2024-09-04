from typing import List

from fastapi import FastAPI, Form, Request, status
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

import data
from model import Skill, Hobby

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get('/favicon.ico')
async def favicon():
    file_name = 'favicon.ico'
    file_path = './static/' + file_name
    return FileResponse(path=file_path, headers={'mimetype': 'image/vnd.microsoft.icon'})


def stream_image(name):
    with open('./static/images/' + name, mode="rb") as the_file:
        yield from the_file


@app.get('/photo', response_model=List[str])
async def photo():
    return StreamingResponse(stream_image('ds.jpg'), media_type="image/jpeg")


@app.get('/skills', response_model=List[Skill])
async def skills(request: Request):
    return data.skills


@app.get('/hobbies', response_model=List[Hobby])
async def hobbies(request: Request):
    return data.hobbies


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000)
