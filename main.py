from transformers import pipeline
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

# Load the translation pipeline
translator = pipeline('translation_en_to_de', model='Helsinki-NLP/opus-mt-en-de')

@app.post("/translate/")
def translate(text: str):
    try:
        translation = translator(text)
        return {"translation": translation[0]['translation_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
