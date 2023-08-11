from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_bm import CampaignBM
from context.campaign.domain.campaign_id import CampaignId
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.infrastructure.mongodb.mongodb_campaign_collection import get_campaign_collection


class MongoDBCampaignRepository(CampaignRepository):

    def __init__(self):
        self.__campaign_collection = get_campaign_collection()

    def find_by_id(self, campaign_id: CampaignId) -> Campaign | None:
        print("HERE 3", campaign_id.to_string())
        result = self.__campaign_collection.find_one({"campaign_id": campaign_id.to_string()})
        if result:
            return Campaign.from_primitives(CampaignBM(**result))
