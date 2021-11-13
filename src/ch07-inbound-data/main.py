import uvicorn
from web.StartupApp import StartupApp

app = StartupApp().create_app()

print(__name__)
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)


