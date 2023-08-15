import logging

from fastapi import APIRouter, Depends
from typing_extensions import Annotated

from app.campaign.config.campaign_constants import CampaignConstants
from app.campaign.controller.search.by_id.search_campaign_by_id_con_res import SearchCampaignByIdControllerResponse
from context.campaign.application.search.by_id.search_campaign_by_id_app import SearchCampaignByIdApp
from context.campaign.application.search.by_id.search_campaign_by_id_app_provider import \
    search_campaign_by_id_app_provider
from context.campaign.domain.campaign_id import CampaignId

SearchCampaignByIdController = APIRouter()

logger = logging.getLogger('SearchCampaignByIdController')


@SearchCampaignByIdController.get(CampaignConstants.SEARCH_BY_ID)
async def get(
        campaign_id: str,
        search_campaign_by_id_app: Annotated[SearchCampaignByIdApp, Depends(search_campaign_by_id_app_provider)]
) -> SearchCampaignByIdControllerResponse:
    logger.info(f'INIT :: campaign_id: {campaign_id}')
    response = SearchCampaignByIdControllerResponse()
    found = search_campaign_by_id_app.exec(CampaignId(campaign_id), True)
    response.data = found.to_primitives()
    logger.info('FINISH ::')
    return response
