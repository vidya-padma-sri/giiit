from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Harshi!!, Let's wake up at 7 am tomorrow"}


print("zhello")

print("ok")
print("second line")

print("changing in remote")

print("which branch is this")

print("this is the new line added in second branch")

print("channging in remote second")
