from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
  return {'data':"random"}

@app.get("/about")
def about():
  return {'data':{"ths is the about page"}}