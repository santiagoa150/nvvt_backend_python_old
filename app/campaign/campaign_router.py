from fastapi import APIRouter
from .config.campaign_constants import CampaignConstants
from .controller.create.create_campaign_con import CreateCampaignController
from .controller.search.by_id.search_campaign_by_id_con import SearchCampaignByIdController

campaign_router = APIRouter(
    prefix=CampaignConstants.PREFIX,
    tags=[CampaignConstants.TAG]
)

campaign_router.include_router(CreateCampaignController)
campaign_router.include_router(SearchCampaignByIdController)
