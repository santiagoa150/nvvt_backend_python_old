from context.shared.domain.constants.error_constants import ErrorConstants
from context.shared.domain.exceptions.base_exception import BaseException


class ActiveCampaignAlreadyExistsException(BaseException):

    def __init__(self, *args):
        super().__init__(status_code=409, message=ErrorConstants.ACTIVE_CAMPAIGN_ALREADY_EXISTS_ERROR, *args)
