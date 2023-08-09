from fastapi import APIRouter

from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_bm import CampaignBM

search_campaign_by_id_controller = APIRouter()


@search_campaign_by_id_controller.get('/')
async def get(campaign_id: str) -> CampaignBM:
    campaign: Campaign = Campaign.from_primitives(
        CampaignBM(
            campaign_id=campaign_id,
            status="ACTIVE",
            name="Default Name",
            year=2023,
            total_list_price=1000,
            total_catalog_price=900,
            total_products=10,
        )
    )
    return campaign.to_primitives()
