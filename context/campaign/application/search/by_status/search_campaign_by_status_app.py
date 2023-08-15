import logging

from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.domain.campaign_status import CampaignStatus
from context.campaign.domain.exceptions.campaign_not_found_exception import CampaignNotFoundException


class SearchCampaignByStatusApp:

    def __init__(self, repository: CampaignRepository):
        self.__logger = logging.getLogger(SearchCampaignByStatusApp.__name__)
        self.__repository = repository

    def exec(self, status: CampaignStatus, raise_exception_if_not_found: bool = False) -> Campaign | None:
        self.__logger.info(f'INIT :: status: {status}, raise_exception_if_not_found: ${raise_exception_if_not_found}')
        found = self.__repository.find_by_status(status)
        if not found and raise_exception_if_not_found:
            raise CampaignNotFoundException()
        self.__logger.info(f'FINISH ::')
        return found

