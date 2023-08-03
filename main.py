from fastapi import FastAPI
from app.campaign.campaign_router import campaign_router

app = FastAPI()

app.include_router(campaign_router)
