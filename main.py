from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import webbrowser
import threading
import time

app = FastAPI()

def open_browser():
    time.sleep(1)
    webbrowser.open_new("http://127.0.0.1:8000")

@app.on_event("startup")
async def startup_event():
    threading.Thread(target=open_browser).start()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    subprocess.Popen(["streamlit", "run", "app.py"])
    return """
    <html>
        <head>
            <title>RAG Pipeline</title>
        </head>
        <body>
            <h1>RAG Pipeline with GPT-4 Turbo</h1>
            <p>Streamlit app is running at <a href="http://localhost:8501">http://localhost:8501</a></p>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
