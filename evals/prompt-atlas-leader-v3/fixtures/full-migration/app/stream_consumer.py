from app.stream_parser import parse_request


def consume(payload):
    return parse_request(payload)
