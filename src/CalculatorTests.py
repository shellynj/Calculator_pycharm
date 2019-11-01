import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    print('******TEST_ADDITION******')
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

        #   ADDITION TEST
    def test_addition(self):
        test_data = CsvReader('/src/addition.csv').data
        for row in test_data:
                self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

                print(row['Value 1'] + ' + ' + row['Value 2'] + ' = ' + row['Result'] + ', Expect: ', self.calculator.result)


        CsvReader.data.clear()



if __name__ == '__main__':
    unittest.main()