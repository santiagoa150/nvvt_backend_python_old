from fastapi import Body
from pydantic import BaseModel
from typing_extensions import Annotated


class CreateCampaignControllerRequest(BaseModel):
    name: str
    year:  Annotated[int, Body(gt=0)]
