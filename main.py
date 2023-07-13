import uvicorn
from fastapi import FastAPI
from typing import Dict
from models import AudioRequest, AudioResponse
from helper import get_analysis, convert_url
from starlette.responses import HTMLResponse


app = FastAPI(
    title="EchoSensai",
    description="An advanced AI-powered call analysis API designed to provide comprehensive insights and intelligent recommendations for your conversations.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Call Analysis", "description": "Endpoints for call analysis"},
    ],
)


@app.get("/", tags=["Index"])
def index():
    html_content = """
    <html>
        <head>
            <style>
                body {
                    background-color: black;
                    color: white;
                    font-family: Verdana, sans-serif;
                    overflow: hidden
                }
                .center {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="center">
                <h1>EchoSensai</h1>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.post("/get_call_analysis", tags=["Call Analysis"], response_model=AudioResponse)
def process(audio_url: AudioRequest) -> Dict[str, str]:
    print(f"Using audio file at: {audio_url.mp3_url}")
    analysis = get_analysis(convert_url(audio_url.mp3_url))
    return analysis


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
