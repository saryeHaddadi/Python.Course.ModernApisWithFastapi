import fastapi
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from web.config import TEMPLATE_PATH

router = fastapi.APIRouter()
templates = Jinja2Templates(TEMPLATE_PATH)

@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})

@router.get('/favicon.ico')
def favicon():
    # /static should be mounted
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
         
