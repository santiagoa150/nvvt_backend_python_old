import logging

from fastapi import APIRouter, Depends
from typing_extensions import Annotated
from app.campaign.config.campaign_constants import CampaignConstants
from app.campaign.controller.create.create_campaign_con_req import CreateCampaignControllerRequest
from app.campaign.controller.create.create_campaign_con_res import CreateCampaignControllerResponse
from context.campaign.application.create.create_campaign_app import CreateCampaignApp
from context.campaign.application.create.create_campaign_app_provider import create_campaign_app_provider

CreateCampaignController = APIRouter()

logger = logging.getLogger('CreateCampaignController')


@CreateCampaignController.post(CampaignConstants.BASE_OPERATION)
async def post(
        request: CreateCampaignControllerRequest,
        create_campaign_app: Annotated[CreateCampaignApp, Depends(create_campaign_app_provider)]
) -> CreateCampaignControllerResponse:
    logger.info('INIT ::')
    response = CreateCampaignControllerResponse()
    created = create_campaign_app.exec(request.name, request.year)
    response.data = created.to_primitives()
    logger.info('FINISH ::')
    return response
