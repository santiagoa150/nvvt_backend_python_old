from fastapi import APIRouter
from context.shared.domain.string_value_object import StringValueObject

search_campaign_by_id_controller = APIRouter()


@search_campaign_by_id_controller.get('/')
async def get(campaign_id: str):
    print(campaign_id)
    id = StringValueObject(1)
