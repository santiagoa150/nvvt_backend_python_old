from context.campaign.domain.campaign_bm import CampaignBM
from context.campaign.domain.campaign_id import CampaignId
from context.campaign.domain.campaign_status import CampaignStatus
from context.shared.domain.domain_root import DomainRoot


class Campaign(DomainRoot):
    campaign_id: CampaignId
    status: CampaignStatus
    name: str
    year: int
    total_list_price: float
    total_catalog_price: float
    total_products: float

    def __init__(self,
                 campaign_id: CampaignId,
                 status: CampaignStatus,
                 name: str,
                 year: int,
                 total_list_price: float,
                 total_catalog_price: float,
                 total_products: float
                 ):
        self.campaign_id = campaign_id
        self.status = status
        self.name = name
        self.year = year
        self.total_list_price = total_list_price
        self.total_catalog_price = total_catalog_price
        self.total_products = total_products

    @staticmethod
    def from_primitives(campaign_bm: CampaignBM) -> 'Campaign':
        return Campaign(
            CampaignId(campaign_bm.campaign_id),
            CampaignStatus(campaign_bm.status),
            campaign_bm.name,
            campaign_bm.year,
            campaign_bm.total_list_price,
            campaign_bm.total_catalog_price,
            campaign_bm.total_products
        )

    def to_primitives(self) -> CampaignBM:
        return CampaignBM(
            campaign_id=self.campaign_id.to_string(),
            status=self.status.to_string(),
            name=self.name,
            year=self.year,
            total_list_price=self.total_list_price,
            total_catalog_price=self.total_catalog_price,
            total_products=self.total_products,
        )
