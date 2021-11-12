from typing import Optional
import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get('/')
def index():
    body = """<html>
           <body style='padding: 10px;'>
           <h1>Welcome to the API</h1>
           <div>
           Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>
           </div>
           </body>
           </html>"""
    
    return fastapi.responses.HTMLResponse(content=body)
           
@app.get('/api/calculate')
# ?x=2&y=3
def calculate(x: int, y: int, z:Optional[int] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content= {"error": "ERROR: z cannot be zero."},
            status_code=400
        )
    
    value = (x + y)
    
    if z is not None:
        value = value / z
    
    return {
        'x': x,
        'y': y,
        'z': z,
        'values': value
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)








