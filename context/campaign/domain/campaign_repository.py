from abc import ABC, abstractmethod

from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_id import CampaignId


class CampaignRepository(ABC):

    @abstractmethod
    def find_by_id(self, campaign_id: CampaignId) -> Campaign | None:
        pass
