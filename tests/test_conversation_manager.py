# tests/test_conversation_manager.py

import unittest
from llm.conversation_manager import ConversationManager

class TestConversationManager(unittest.TestCase):
    def setUp(self):
        # Use a small max_history_chars for testing truncation logic if needed
        self.cm = ConversationManager(max_history_chars=100)

    def test_add_and_get_context(self):
        self.cm.add_turn("Hello", "Hi there!")
        self.cm.add_turn("How are you?", "I'm fine, thanks.")
        context = self.cm.get_context()
        self.assertIn("Hello", context)
        self.assertIn("Hi there!", context)
        self.assertIn("How are you?", context)
        self.assertIn("I'm fine, thanks.", context)

    def test_reset(self):
        self.cm.add_turn("Hello", "Hi there!")
        self.cm.reset()
        context = self.cm.get_context()
        self.assertEqual(context, "")

if __name__ == "__main__":
    unittest.main()
