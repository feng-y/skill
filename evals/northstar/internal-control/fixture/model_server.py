from dataclasses import dataclass, field


@dataclass
class Request:
    items: list[str]
    only_return_fea_sign: bool = False
    debug: bool = False


@dataclass
class FeatureResult:
    signatures: list[int]


@dataclass
class Score:
    is_hit: bool = True
    features: FeatureResult | None = None


@dataclass
class Response:
    feasign: list[int] = field(default_factory=list)
    embedding: list[float] = field(default_factory=list)


class QServer:
    def __init__(self):
        self.calls = 0

    def predict(self, items):
        self.calls += 1
        return [float(len(item)) for item in items]


def observe(request, features, score):
    if request.debug:
        score.features = features


def fill_response(score, response):
    if score.is_hit and score.features is not None:
        response.feasign.extend(score.features.signatures)


def predict(request, qserver):
    features = FeatureResult([sum(item.encode()) for item in request.items])
    score = Score()
    observe(request, features, score)
    response = Response(embedding=qserver.predict(request.items))
    fill_response(score, response)
    return response
