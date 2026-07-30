def parse_request(payload):
    request = {
        "user_id": str(payload["user_id"]),
        "features": list(payload.get("features", [])),
    }
    if "trace_id" in payload:
        request["trace_id"] = str(payload["trace_id"])
    request["streaming"] = bool(payload.get("streaming", True))
    return request
