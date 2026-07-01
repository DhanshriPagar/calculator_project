import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ✅ THIS LINE IS THE KEY FIX
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request, num1: float = Form(...), num2: float = Form(...), operation: str = Form(...)):
    
    if operation == "add":
        result = num1 + num2
    elif operation == "sub":
        result = num1 - num2
    elif operation == "mul":
        result = num1 * num2
    elif operation == "div":
        result = "Cannot divide by zero" if num2 == 0 else num1 / num2
    else:
        result = "Invalid"

    return templates.TemplateResponse("index.html", {"request": request, "result": result})