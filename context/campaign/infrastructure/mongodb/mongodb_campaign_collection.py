from context.shared.infrastructure.mongodb.mongodb_connection import MongoDBClient
from context.shared.infrastructure.mongodb.mongodb_constants import MongoDBConstants
from context.campaign.infrastructure.mongodb.mongodb_campaign_schema import campaign_schema


def get_campaign_collection():
    db_client = MongoDBClient()
    db = db_client.get_database()

    try:
        db.create_collection(MongoDBConstants.CAMPAIGN_COLLECTION)
    except (Exception,):
        pass

    db.command("collMod", MongoDBConstants.CAMPAIGN_COLLECTION, validator=campaign_schema)
    ct = db[MongoDBConstants.CAMPAIGN_COLLECTION]
    ct.create_index("campaign_id", unique=True)
    return ct
