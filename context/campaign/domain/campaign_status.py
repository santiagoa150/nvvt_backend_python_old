from context.campaign.domain.constants.campaign_status_constants import CampaignStatusConstants
from context.campaign.domain.exceptions.invalid_campaign_status_exception import InvalidCampaignStatusException
from context.shared.domain.value_objects.status_value_object import StatusValueObject


class CampaignStatus(StatusValueObject):

    def __init__(self, value: str):
        self._validate_status(value)
        super().__init__(value)

    def _validate_status(self, value: str) -> None:
        allowed_values = [status for status in CampaignStatusConstants]
        if value not in allowed_values:
            raise InvalidCampaignStatusException()
