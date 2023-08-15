from enum import Enum


class CampaignConstants(str, Enum):
    PREFIX = '/campaign'
    TAG = 'Campaigns',
    BASE_OPERATION = '/'
    SEARCH_BY_ID = '/{campaign_id}'
