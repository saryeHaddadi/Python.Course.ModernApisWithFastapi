import fastapi
from fastapi.staticfiles import StaticFiles
from web.services import IndexPageService, WeatherWebService
from web.config import STATIC_PATH

def create_app():
    app = fastapi.FastAPI()
    app.include_router(IndexPageService.router)
    app.mount('/static', StaticFiles(directory=STATIC_PATH))
    app.include_router(WeatherWebService.router)
    
    return app
