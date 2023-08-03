from fastapi import APIRouter
from .config.campaign_constants import CampaignConstants
from .controller.search.by_id.search_campaign_by_id_con import search_campaign_by_id_controller

campaign_router = APIRouter(
    prefix=CampaignConstants.PREFIX,
    tags=[CampaignConstants.TAG]
)

campaign_router.include_router(search_campaign_by_id_controller)
