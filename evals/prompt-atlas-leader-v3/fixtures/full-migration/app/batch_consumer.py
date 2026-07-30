from app.parser import parse_request


def consume(payload):
    return parse_request(payload)
