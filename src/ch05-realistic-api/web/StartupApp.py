import fastapi
from fastapi.staticfiles import StaticFiles
from web.services import IndexPageService, WeatherWebService
from web.config import STATIC_PATH


class StartupApp:
    def __init__(self):
        self.app = None
    
    def create_app(self):
        self.app = fastapi.FastAPI()
        self.configure_app()
        return self.app

    def configure_app(self):
        self.configure_routing()
        self.configure_mount()

    def configure_routing(self):
        self.app.include_router(IndexPageService.router)
        self.app.include_router(WeatherWebService.router)

    def configure_mount(self):
        self.app.mount('/static', StaticFiles(directory=STATIC_PATH))


