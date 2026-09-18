from dataclasses import dataclass


@dataclass(frozen=True)
class ProfilePB:
    segment: str


@dataclass(frozen=True)
class ItemPB:
    item_id: str
    score: int


@dataclass(frozen=True)
class SpecificationPB:
    request_id: str
    profile: ProfilePB
    items: tuple[ItemPB, ...]


@dataclass(frozen=True)
class ModelRequestPB:
    request_id: str
    profile: ProfilePB
    items: tuple[ItemPB, ...]
