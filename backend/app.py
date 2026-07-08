from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.ai import analyze_issue

app = FastAPI()

app.mount("/static", StaticFiles(directory="FrontEnd/static"), name="static")

templates = Jinja2Templates(directory="FrontEnd/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/analyze")
async def analyze(
    issue: str = Form(""),
    logs: str = Form(""),
    image: UploadFile = File(None)
):

    response = analyze_issue(
        issue,
        logs,
        image
    )

    return {
        "analysis": response
    }