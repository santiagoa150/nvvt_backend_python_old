from context.campaign.domain.campaign_bm import CampaignBM
from context.shared.domain.responses.default_response import DefaultResponse


class SearchCampaignByIdControllerResponse(DefaultResponse):
    data: CampaignBM = None
