from __future__ import annotations

import unittest

from src.prompt_merge import merge_prompts


class PromptMergeTests(unittest.TestCase):
    def test_negative_tags_receive_negative_weights(self):
        self.assertEqual(
            merge_prompts("sharp portrait", "blurry, (text:1.3)"),
            "sharp portrait, (blurry:-1), (text:-1.3)",
        )

    def test_existing_positive_weight_is_preserved(self):
        self.assertEqual(merge_prompts("(detail:1.2)", "noise"), "(detail:1.2), (noise:-1)")


if __name__ == "__main__":
    unittest.main()
