from .access import HermesAccess, SpecificationAccess
from .messages import ItemPB, ModelRequestPB, ProfilePB, SpecificationPB


_full_conversion_count = 0


def reset_conversion_count() -> None:
    global _full_conversion_count
    _full_conversion_count = 0


def conversion_count() -> int:
    return _full_conversion_count


def rebuild_specification(request: ModelRequestPB) -> SpecificationPB:
    """Current compatibility path: deep-copy the entire request as a Spec."""
    global _full_conversion_count
    _full_conversion_count += 1
    return SpecificationPB(
        request_id=request.request_id,
        profile=ProfilePB(segment=request.profile.segment),
        items=tuple(ItemPB(item_id=item.item_id, score=item.score) for item in request.items),
    )


def _evaluate(access: HermesAccess) -> tuple[str, ...]:
    prefix = f"{access.request_id}:{access.profile.segment}"
    return tuple(f"{prefix}:{item.item_id}={item.score}" for item in access.items)


def run_spec(specification: SpecificationPB) -> tuple[str, ...]:
    return _evaluate(SpecificationAccess(specification))


def run_model_request(request: ModelRequestPB) -> tuple[str, ...]:
    return run_spec(rebuild_specification(request))
