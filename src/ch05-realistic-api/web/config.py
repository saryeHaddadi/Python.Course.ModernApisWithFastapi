from pathlib import Path

BASE_PATH = Path(Path(__file__).parent.resolve())

PAGE_PATH = Path(BASE_PATH, 'pages')
TEMPLATE_PATH = Path(PAGE_PATH, 'templates')
STATIC_PATH = Path(PAGE_PATH, 'static')

SETTINGS_FILEPATH = Path(BASE_PATH, 'settings.json')



