from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Web Service Agent Valorant", description="Web Service untuk Tugas Praktikum Provis")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Valo(BaseModel):
    id: str
    name: str
    realname: str
    role:str
    creature:str
    image:str

# Data dummy Valo
valo_data = {"data":[
    {"id": "1", "name": "Brimstone", "realname": "Liam Byrne","role": "Controller", "creature": "Human", "image": "brim.png"},
    {"id": "2", "name": "Iso", "realname": "Li Zhaoyu","role": "Duelist", "creature": "Radiant", "image": "iso.png"},
    {"id": "3", "name": "Chamber", "realname": "Vincent Fabron","role": "Sentinel", "creature": "Human", "image": "chamber.png"},
    {"id": "4", "name": "Gekko", "realname": "Mateo Armendáriz De la Fuente","role": "Initiator", "creature": "Unconfirmed", "image": "gekko.png"},
    {"id": "5", "name": "Clove", "realname": "Unknown","role": "Controller", "creature": "Radiant", "image": "clove.png"},
    {"id": "6", "name": "Reyna", "realname": "Zyanya Mondragon","role": "Duelist", "creature": "Radiant", "image": "reyna.png"},
    {"id": "7", "name": "Viper", "realname": "Sabine Callas","role": "Controller", "creature": "Human", "image": "viper.png"},
    {"id": "8", "name": "Omen", "realname": "Unknown","role": "Controller", "creature": "Radiant", "image": "omen.png"},
    {"id": "9", "name": "Killjoy", "realname": "Klara Bohringer","role": "Sentinel", "creature": "Human", "image": "killjoy.png"},
    {"id": "10", "name": "Cypher", "realname": "Amir El Amari","role": "Sentinel", "creature": "Human", "image": "cypher.png"},
    {"id": "11", "name": "Sova", "realname": "Sasha Novikov","role": "Initiator", "creature": "Human", "image": "sova.png"},
    {"id": "12", "name": "Sage", "realname": "Wei Lingying","role": "Sentinel", "creature": "Radiant", "image": "sage.png"},
    {"id": "13", "name": "Phoenix", "realname": "Jamie Ayademi","role": "Duelist", "creature": "Radiant", "image": "phoenix.png"},
    {"id": "14", "name": "Jett", "realname": "Han Sunwoo","role": "Duelist", "creature": "Radiant", "image": "jett.png"},
    {"id": "15", "name": "Raze", "realname": "Tayane Alves","role": "Duelist", "creature": "Tech User", "image": "raze.png"},
    {"id": "16", "name": "Breach", "realname": "Erik Torsten","role": "Initiator", "creature": "Human", "image": "breach.png"},
    {"id": "17", "name": "Skye", "realname": "Kirra Foster","role": "Initiator", "creature": "Radiant", "image": "skye.png"},
    {"id": "18", "name": "Yoru", "realname": "Kiritani Ryo","role": "Duelist", "creature": "Radiant", "image": "yoru.png"},
    {"id": "19", "name": "Astra", "realname": "Efia Danso","role": "Controller", "creature": "Radiant", "image": "astra.png"},
    {"id": "20", "name": "Kayo", "realname": "Unknown","role": "Initiator", "creature": "Cybernetic", "image": "kayo.png"},
    {"id": "21", "name": "Neon", "realname": "Tala Nicole Dimaapi Valdez","role": "Duelist", "creature": "Radiant", "image": "neon.png"},
    {"id": "22", "name": "Fade", "realname": "Hazal Eyletmez","role": "Initiator", "creature": "Radiant", "image": "fade.png"},
    {"id": "23", "name": "Harbor", "realname": "Varun Batra","role": "Controller", "creature": "Human", "image": "harbor.png"},
    {"id": "24", "name": "Deadlock", "realname": "Iselin","role": "Sentinel", "creature": "Human", "image": "deadlock.png"},
], "message":"success", "error":"false"}

@app.get("/")
async def root():
    return {"message": "Welcome to Valo API"}

@app.get("/daftar_agent_valo")
async def get_valo():
    return valo_data

@app.get("/detail_agent_valo/{valo_id}", response_model=Valo)
async def get_valo_detail(valo_id: str):
    for valo in valo_data["data"]:
        if valo["id"] == valo_id:
            return valo
    return {"message": "Data Valo not found"}
