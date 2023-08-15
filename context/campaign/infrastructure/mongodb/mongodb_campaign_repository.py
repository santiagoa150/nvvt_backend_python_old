import logging

from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_bm import CampaignBM
from context.campaign.domain.campaign_id import CampaignId
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.domain.campaign_status import CampaignStatus
from context.campaign.infrastructure.mongodb.mongodb_campaign_collection import get_campaign_collection


class MongoDBCampaignRepository(CampaignRepository):

    def __init__(self):
        self.__logger = logging.getLogger(MongoDBCampaignRepository.__name__)
        self.__campaign_collection = get_campaign_collection()

    def create(self, campaign_bm: CampaignBM) -> Campaign:
        self.__logger.info(f'INIT :: Creating campaign_bm: {campaign_bm}')
        inserted = self.__campaign_collection.insert_one(dict(campaign_bm))
        result = self.__campaign_collection.find_one({"_id": inserted.inserted_id})
        mapped = Campaign.from_primitives(CampaignBM(**result))
        self.__logger.info('FINISH ::')
        return mapped

    def find_by_status(self, status: CampaignStatus) -> Campaign | None:
        self.__logger.info(f'INIT :: status: ${status.to_string()}')
        mapped = None
        result = self.__campaign_collection.find_one({"status": status.to_string()})
        if result:
            mapped = Campaign.from_primitives(CampaignBM(**result))
        self.__logger.info('FINISH ::')
        return mapped

    def find_by_id(self, campaign_id: CampaignId) -> Campaign | None:
        self.__logger.info(f'INIT :: campaign_id: ${campaign_id.to_string()}')
        mapped = None
        result = self.__campaign_collection.find_one({"campaign_id": campaign_id.to_string()})
        if result:
            mapped = Campaign.from_primitives(CampaignBM(**result))
        self.__logger.info('FINISH ::')
        return mapped
