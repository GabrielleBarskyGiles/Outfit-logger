import sqlite3
from typing import Union
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    Button : int

origins = [
	"http://localhost:8000",
	"http://gabrielles-air.lan:8000",
]

#app.add_middleware(
#	CORSMiddleware,
#	allow_origins=origins,
#	allow_credentials=True,
#	allow_methods=["*"],
#	allow_headers=["*"],
#)

app.mount("/static", StaticFiles(directory="/Users/gabriellebarsky-giles/Website-project/static"), name="static")

@app.post("/")
async def read_root(item: Item):
  con = sqlite3.connect("practice.db")
  #cur.execute("CREATE TABLE test(button1, button2)")
  if item.Button==1:
     cur = con.cursor()
     cur.execute("INSERT INTO test VALUES (1,0)")
     con.commit()
     res = cur.execute("SELECT COUNT(button1) FROM test WHERE button1=1")
     count = res.fetchone()
     return{"button1": count}
  elif item.Button==2:
     cur = con.cursor()
     cur.execute("INSERT INTO test VALUES (0,1)")
     con.commit()
     res = cur.execute("SELECT COUNT(button2) FROM test WHERE button2=1")
     count = res.fetchone()
     return{"button2": count}
  else:
     return{"faied":"sad"}
