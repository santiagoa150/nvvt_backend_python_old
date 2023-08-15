import logging

from context.campaign.domain.campaign_id import CampaignId
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.domain.exceptions.campaign_not_found_exception import CampaignNotFoundException


class SearchCampaignByIdApp:

    def __init__(self, repository: CampaignRepository):
        self.__logger = logging.getLogger(SearchCampaignByIdApp.__name__)
        self.__repository = repository

    def exec(self, campaign_id: CampaignId, raise_exception_if_not_found: bool = False):
        self.__logger.info(f'INIT :: id:{campaign_id}, raise_exception_if_not_found:{raise_exception_if_not_found}')
        found = self.__repository.find_by_id(campaign_id)
        if not found and raise_exception_if_not_found:
            raise CampaignNotFoundException()
        self.__logger.info('FINISH ::')
        return found
