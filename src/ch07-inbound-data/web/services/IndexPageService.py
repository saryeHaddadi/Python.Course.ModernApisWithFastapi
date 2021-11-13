import fastapi
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from http import HTTPStatus
from web.config import TEMPLATE_PATH
from web.services import ReportWebService

router = fastapi.APIRouter()
templates = Jinja2Templates(TEMPLATE_PATH)

@router.get('/', response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    events = await ReportWebService.GetReports()
    data = {'request': request, 'events': events}
    return templates.TemplateResponse('home/index.html', data)

@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    # /static should be mounted
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico',
                                              status_code=HTTPStatus.PERMANENT_REDIRECT)
         
