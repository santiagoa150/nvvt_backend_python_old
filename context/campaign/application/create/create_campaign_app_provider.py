from fastapi import Depends
from typing_extensions import Annotated

from context.campaign.application.create.create_campaign_app import CreateCampaignApp
from context.campaign.application.search.by_status.search_campaign_by_status_app import SearchCampaignByStatusApp
from context.campaign.application.search.by_status.search_campaign_by_status_app_provider import \
    search_campaign_by_status_app_provider
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.infrastructure.mongodb.mongodb_campaign_repository_provider import \
    mongodb_campaign_repository_provider


def create_campaign_app_provider(
        search_campaign_by_status_app: Annotated[
            SearchCampaignByStatusApp, Depends(search_campaign_by_status_app_provider)],
        repository: Annotated[CampaignRepository, Depends(mongodb_campaign_repository_provider)]
):
    return CreateCampaignApp(
        search_campaign_by_status_app,
        repository
    )
