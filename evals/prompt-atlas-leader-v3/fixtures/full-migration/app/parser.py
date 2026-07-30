def parse_request(payload):
    return {
        "user_id": str(payload["user_id"]),
        "features": list(payload.get("features", [])),
    }
