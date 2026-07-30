import unittest

from app.batch_consumer import consume
from app.parser import parse_request


class ParserTests(unittest.TestCase):
    def test_canonical_shape(self):
        payload = {"user_id": 7, "features": ["a", "b"]}
        self.assertEqual(
            parse_request(payload),
            {"user_id": "7", "features": ["a", "b"]},
        )

    def test_batch_consumer(self):
        self.assertEqual(
            consume({"user_id": "9"}),
            {"user_id": "9", "features": []},
        )


if __name__ == "__main__":
    unittest.main()
