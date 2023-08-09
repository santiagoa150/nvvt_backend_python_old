from context.shared.domain.constants.error_constants import ErrorConstants
from context.shared.domain.exceptions.base_exception import BaseException


class InvalidCampaignStatusException(BaseException):

    def __init__(self, *args):
        super().__init__(status_code=400, message=ErrorConstants.INVALID_CAMPAIGN_STATUS, *args)
