from unittest import TestCase

from helper.values_to_graph_block_translator import ValuesToGraphBlockTranslator


class TestVTG(TestCase):

    def test_zero_and_one_are_different(self):
        self.assertNotEqual(ValuesToGraphBlockTranslator.squares[0], ValuesToGraphBlockTranslator.squares[1], "0 and 1 looks almost the same in the code but are different")
    pass

    def test_add(self):
        vtg = ValuesToGraphBlockTranslator([0, 1, 2, 3, 4, 5])
        self.assertEqual(vtg.get(0), "▏")
        self.assertEqual(vtg.get(1), "▎")
        self.assertEqual(vtg.get(2), "▍")
        self.assertEqual(vtg.get(3), "▋")
        self.assertEqual(vtg.get(4), "▊")
        self.assertEqual(vtg.get(5), "▉")
    pass

    def test_add2(self):
        vtg = ValuesToGraphBlockTranslator([5, 1, 2.5])
        self.assertEqual(vtg.get(1), "▏")
        self.assertEqual(vtg.get(5), "▉")
        self.assertEqual(vtg.get(4.5), "▊")
    pass
