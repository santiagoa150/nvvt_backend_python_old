from abc import ABC, abstractmethod

from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_bm import CampaignBM
from context.campaign.domain.campaign_id import CampaignId
from context.campaign.domain.campaign_status import CampaignStatus


class CampaignRepository(ABC):

    @abstractmethod
    def find_by_id(self, campaign_id: CampaignId) -> Campaign | None:
        pass

    @abstractmethod
    def find_by_status(self, status: CampaignStatus) -> Campaign | None:
        pass

    @abstractmethod
    def create(self, campaign_bm: CampaignBM) -> Campaign:
        pass
