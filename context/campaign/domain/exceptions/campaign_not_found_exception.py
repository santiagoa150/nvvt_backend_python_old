from context.shared.domain.constants.error_constants import ErrorConstants
from context.shared.domain.exceptions.base_exception import BaseException


class CampaignNotFoundException(BaseException):

    def __init__(self, *args):
        super().__init__(status_code=404, message=ErrorConstants.CAMPAIGN_NOT_FOUND_ERROR, *args)
