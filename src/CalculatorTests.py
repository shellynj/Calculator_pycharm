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


        #   SUBTRACTION TEST
    def test_subtraction(self):
        test_data_sub = CsvReader('/src/subtraction.csv').data
        print('')
        print('******TEST_SUBTRACTION******')

        for row in test_data_sub:
                self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))
                print(row['Value 2'] + ' - ' + row['Value 1'] + ' = ' + row['Result'] + ', Expect: ', self.calculator.result)

        CsvReader.data.clear()






       #   DIVISION TEST
    def test_division(self):
        test_data_div = CsvReader('/src/division.csv').data
        print('')
        print('******TEST_DIVISION******')
        for row in test_data_div:
                 self.assertAlmostEqual(self.calculator.divide(float(row['Value 1']),float(row['Value 2'])), float(row['Result']),places=8)
                 self.assertAlmostEqual(float(self.calculator.result), float(row['Result']))

                 print(row['Value 2'] + ' / ' + row['Value 1'] + ' = ' + row['Result'] + ', Expect: ', float(self.calculator.result))

        CsvReader.data.clear()



if __name__ == '__main__':
    unittest.main()