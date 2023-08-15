from context.campaign.infrastructure.mongodb.mongodb_campaign_repository import MongoDBCampaignRepository


def mongodb_campaign_repository_provider():
    return MongoDBCampaignRepository()
