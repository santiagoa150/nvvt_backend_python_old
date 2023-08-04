from fastapi import APIRouter

search_campaign_by_id_controller = APIRouter()


@search_campaign_by_id_controller.get('/')
async def get(campaign_id: int):
    return ""
