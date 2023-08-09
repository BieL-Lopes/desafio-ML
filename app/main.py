from fastapi import FastAPI, HTTPException, Form, File, UploadFile
from . import suporteAnalise

app = FastAPI(title="Análise de Sentimento")

@app.post("/analise", tags=["Analisar"])
def analise_sentimento(text: str = Form(None, media_type="text/plain"), img: UploadFile = File(None)):

    if text is None and img is None:
        raise HTTPException(status_code=400, detail="Texto ou imagem não fornecido")

    if img:
        image_bytes = img.file.read()
        sentiment = suporteAnalise.analisar_imagem(image_bytes)
    if text:
        sentiment = suporteAnalise.analisar_texto(text)
    
    response_data = {"Sentimento": sentiment}
    return response_data
