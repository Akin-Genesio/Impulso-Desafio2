
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/time")
def read_local_time():
    current_time = time.ctime()
    return current_time
