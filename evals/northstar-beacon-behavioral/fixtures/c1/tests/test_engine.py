import unittest

from hermes.engine import (
    conversion_count,
    reset_conversion_count,
    run_model_request,
    run_spec,
)
from hermes.messages import ItemPB, ModelRequestPB, ProfilePB, SpecificationPB


class HermesEngineTest(unittest.TestCase):
    def setUp(self) -> None:
        reset_conversion_count()
        self.profile = ProfilePB(segment="premium")
        self.items = (ItemPB("first", 7), ItemPB("second", 11))

    def test_existing_spec_behavior_and_order_are_preserved(self) -> None:
        result = run_spec(SpecificationPB("req-1", self.profile, self.items))

        self.assertEqual(
            result,
            ("req-1:premium:first=7", "req-1:premium:second=11"),
        )
        self.assertEqual(conversion_count(), 0)

    def test_model_request_matches_specification_behavior(self) -> None:
        spec_result = run_spec(SpecificationPB("req-2", self.profile, self.items))
        model_result = run_model_request(ModelRequestPB("req-2", self.profile, self.items))

        self.assertEqual(model_result, spec_result)

    def test_model_request_currently_uses_one_full_conversion(self) -> None:
        run_model_request(ModelRequestPB("req-3", self.profile, self.items))

        self.assertEqual(conversion_count(), 1)


if __name__ == "__main__":
    unittest.main()
