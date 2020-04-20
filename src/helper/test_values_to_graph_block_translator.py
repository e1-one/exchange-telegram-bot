from unittest import TestCase

from helper.values_to_graph_block_translator import ValuesToGraphBlockTranslator


class TestVTG(TestCase):

    def test_happy_path(self):
        vtg = ValuesToGraphBlockTranslator([1, 2, 3, 4, 5, 6])
        self.assertEqual(vtg.get(1), "▏")
        self.assertEqual(vtg.get(2), "▎")
        self.assertEqual(vtg.get(3), "▍")
        self.assertEqual(vtg.get(4), "▋")
        self.assertEqual(vtg.get(5), "▊")
        self.assertEqual(vtg.get(6), "▉")
    pass

    def test_mixed_order(self):
        vtg = ValuesToGraphBlockTranslator([5, 1, 2.5])
        self.assertEqual(vtg.get(1), "▏")
        self.assertEqual(vtg.get(5), "▉")
        self.assertEqual(vtg.get(4.5), "▊")
    pass

    def test_list_with_zero(self):
        vtg = ValuesToGraphBlockTranslator([0, 1, 10, 0])
        self.assertEqual(vtg.get(1), "▏")
        self.assertEqual(vtg.get(10), "▉")
        self.assertEqual(vtg.get(0), '▁')
    pass
