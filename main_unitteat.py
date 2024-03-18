import unittest
import unit_test


class Testing(unittest.TestCase):
    def setUp(self) -> None:
        print('do some stuff')

    def test_do_stuff(self):
        pram = 10
        hi = unit_test.add_num(pram)
        self.assertEqual(hi, 15)

    def test_do_stuff2(self):
        pram = 'sjfg'
        hi = unit_test.add_num(pram)
        self.assertIsInstance(hi, ValueError)

    def test_do_stuff3(self):
        pram = None
        hi = unit_test.add_num(pram)
        self.assertEqual(hi, 'please enter a value')


if __name__ == '__main__':
    unittest.main()
