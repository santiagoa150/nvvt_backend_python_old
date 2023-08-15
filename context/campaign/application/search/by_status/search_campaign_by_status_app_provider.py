from fastapi import Depends
from typing_extensions import Annotated

from context.campaign.application.search.by_status.search_campaign_by_status_app import SearchCampaignByStatusApp
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.infrastructure.mongodb.mongodb_campaign_repository_provider import \
    mongodb_campaign_repository_provider


def search_campaign_by_status_app_provider(
        repository: Annotated[CampaignRepository, Depends(mongodb_campaign_repository_provider)]
):
    return SearchCampaignByStatusApp(repository)