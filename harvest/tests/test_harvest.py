"""Harvest functional tests."""

from harvest import harvest


class TestHarvest:
    def test_answer(self):
        test_data = "test"
        return harvest.test(test_data)
