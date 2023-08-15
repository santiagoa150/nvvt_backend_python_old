import logging

from context.campaign.application.search.by_status.search_campaign_by_status_app import SearchCampaignByStatusApp
from context.campaign.domain.campaign import Campaign
from context.campaign.domain.campaign_bm import CampaignBM
from context.campaign.domain.campaign_repository import CampaignRepository
from context.campaign.domain.campaign_status import CampaignStatus
from context.campaign.domain.constants.campaign_status_constants import CampaignStatusConstants
from context.campaign.domain.exceptions.active_campaign_already_exists_exception import \
    ActiveCampaignAlreadyExistsException
from context.shared.domain.value_objects.id_value_object import IdValueObject


class CreateCampaignApp:
    def __init__(self,
                 search_campaign_by_status_app: SearchCampaignByStatusApp,
                 repository: CampaignRepository):
        self.__logger = logging.getLogger(CreateCampaignApp.__name__)
        self.__repository = repository
        self.__search_campaign_by_status_app = search_campaign_by_status_app

    def exec(self, name: str, year: int) -> Campaign:
        self.__logger.info('INIT ::')
        self.__validate_if_active_campaign_exists()
        campaign_bm = CampaignBM(
            name=name,
            year=year,
            campaign_id=IdValueObject.generate(),
            status=CampaignStatusConstants.ACTIVE,
            total_list_price=0,
            total_catalog_price=0,
            total_products=0,
        )
        created = self.__repository.create(campaign_bm)
        self.__logger.info('FINISH ::')
        return created

    def __validate_if_active_campaign_exists(self) -> None:
        self.__logger.info('INIT ::')
        active_status = CampaignStatus(CampaignStatusConstants.ACTIVE)
        active_campaign = self.__search_campaign_by_status_app.exec(active_status)
        if active_campaign:
            raise ActiveCampaignAlreadyExistsException()
        self.__logger.info('FINISH ::')
