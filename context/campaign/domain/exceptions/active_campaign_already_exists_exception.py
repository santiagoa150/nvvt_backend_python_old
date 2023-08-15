from fastapi import status

from context.shared.domain.constants.error_constants import ErrorConstants
from context.shared.domain.exceptions.base_exception import BaseException


class ActiveCampaignAlreadyExistsException(BaseException):

    def __init__(self, *args):
        super().__init__(status_code=status.HTTP_409_CONFLICT, message=ErrorConstants.ACTIVE_CAMPAIGN_ALREADY_EXISTS_ERROR, *args)
