from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import subprocess
import os

app = FastAPI()

LATEX_DIR = "latex_files"
os.makedirs(LATEX_DIR, exist_ok=True)

@app.post("/compile/")
async def compile_latex(file: UploadFile = File(...)):
    tex_path = os.path.join(LATEX_DIR, "document.tex")
    pdf_path = os.path.join(LATEX_DIR, "document.pdf")

    with open(tex_path, "wb") as f:
        f.write(await file.read())

    subprocess.run(["pdflatex", "-output-directory", LATEX_DIR, tex_path], check=True)

    return FileResponse(pdf_path, media_type="application/pdf", filename="document.pdf")
