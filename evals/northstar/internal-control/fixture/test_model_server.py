import unittest

from model_server import QServer, Request, predict


class ExistingBehavior(unittest.TestCase):
    def test_default_calls_qserver(self):
        server = QServer()
        result = predict(Request(["a", "bb"]), server)
        self.assertEqual(server.calls, 1)
        self.assertEqual(result.embedding, [1.0, 2.0])
        self.assertEqual(result.feasign, [])

    def test_debug_returns_signatures(self):
        result = predict(Request(["a", "bb"], debug=True), QServer())
        self.assertEqual(result.feasign, [97, 196])
