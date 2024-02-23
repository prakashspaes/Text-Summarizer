from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from TextSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, text: str = Form(...)):
    try:
        print("Received text:", text)
        summarizer = PredictionPipeline()
        summary = summarizer.predict(text)
        print("Summary:", summary)
        return templates.TemplateResponse("summary.html", {"request": request, "text": text, "summary": summary})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing text: {e}")


    

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)