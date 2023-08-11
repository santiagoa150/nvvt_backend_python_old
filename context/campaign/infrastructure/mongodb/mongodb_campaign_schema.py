campaign_schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["campaign_id", "status", "name", "year", "total_list_price", "total_catalog_price",
                     "total_products"],
        "additionalProperties": True,
        "properties": {
            "campaign_id": {
                "bsonType": "string",
                "description": "Must be a string and is required"
            },
            "status": {
                "bsonType": "string",
                "description": "Must be a string and is required"
            },
            "name": {
                "bsonType": "string",
                "description": "Must be a string and is required"
            },
            "year": {
                "bsonType": "int",
                "description": "Must be a integer and is required"
            },
            "total_list_price": {
                "bsonType": "double",
                "description": "Must be a double and is required"
            },
            "total_catalog_price": {
                "bsonType": "double",
                "description": "Must be a double and is required"
            },
            "total_products": {
                "bsonType": "double",
                "description": "Must be a double and is required"
            }
        }
    }
}
