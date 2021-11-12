import fastapi
import uvicorn


app = fastapi.FastAPI()

@app.get('/')
def index():
    return "Hello Weather app!"

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)










