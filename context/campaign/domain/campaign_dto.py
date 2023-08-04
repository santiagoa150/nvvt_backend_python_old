from pydantic import BaseModel


class CampaignDto(BaseModel):
    campaign_id: str
    status: str
    name: str
    year: int
    total_list_price: float
    total_catalog_price: float
    total_products: float
    