from typing import Protocol

from .messages import ItemPB, ProfilePB, SpecificationPB


class HermesAccess(Protocol):
    @property
    def request_id(self) -> str: ...

    @property
    def profile(self) -> ProfilePB: ...

    @property
    def items(self) -> tuple[ItemPB, ...]: ...


class SpecificationAccess:
    """Established access path for the original Specification message."""

    def __init__(self, specification: SpecificationPB):
        self._specification = specification

    @property
    def request_id(self) -> str:
        return self._specification.request_id

    @property
    def profile(self) -> ProfilePB:
        return self._specification.profile

    @property
    def items(self) -> tuple[ItemPB, ...]:
        return self._specification.items
