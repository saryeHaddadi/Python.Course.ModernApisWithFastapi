import fastapi
from fastapi.staticfiles import StaticFiles

from starlette.requests import Request
from starlette.responses import HTMLResponse
import uvicorn
from starlette.templating import Jinja2Templates
from pathlib import Path

BASE_PATH = Path(__file__).parent.resolve()

app = fastapi.FastAPI()
templates = Jinja2Templates(directory=f'{BASE_PATH}/templates')
static_dir = f'{BASE_PATH}/static'
app.mount('/static', StaticFiles(directory=static_dir))



@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    print(templates.env)
    return templates.TemplateResponse('home/index.html', {'request': request})

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)










