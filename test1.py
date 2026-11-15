from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Harshi!!, Let's wake up at 7 am tomorrow"}


print("zhello")
