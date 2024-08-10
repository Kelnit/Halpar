from fastapi import FastAPI

import config, logits

app = FastAPI(title="Hall Model")

@app.on_event("startup")
def imload():
  if not os.path.isdir("documents"):
    config.unlock("documents")

@app.get("/")
def imroot():
  return {"result":"Hi !"}

@app.get("/logits")
def sentencer(sentence : str):
  sentence = config.runner(sentence)
  result = logits.modelresult(sentence)
  return result