from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from TextSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict_route(request: Request, text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return templates.TemplateResponse("result.html", {"request": request, "summary": summary, "text": text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
