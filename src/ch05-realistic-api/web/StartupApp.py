import fastapi
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import json
from app.services import OpenWeatherMapService
from web.services import IndexPageService, WeatherWebService
from web.config import STATIC_PATH, SETTINGS_FILEPATH


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
        self.configure_apikey()

    def configure_routing(self):
        self.app.include_router(IndexPageService.router)
        self.app.include_router(WeatherWebService.router)

    def configure_mount(self):
        self.app.mount('/static', StaticFiles(directory=STATIC_PATH))

    def configure_apikey(self):
        if not SETTINGS_FILEPATH.exists():
            print(f'WARNING: {SETTINGS_FILEPATH} file not found.')
            raise Exception('settings.json not found.')
        
        with open(SETTINGS_FILEPATH) as f:
            settings = json.load(f)
            # TODO: revoir reference OpenWeatherMapService
            OpenWeatherMapService.apiKey = settings.get('apiKey')



         