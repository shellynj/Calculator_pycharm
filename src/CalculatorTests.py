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


        #   MULTIPLICATION TEST
    def test_multiplication(self):
        test_data_multi = CsvReader('/src/multiplication.csv').data
        print('')
        print('******TEST_MULTIPLICATION******')
        for row in test_data_multi:
                self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

                print(row['Value 2'] + ' * ' + row['Value 1'] + ' = ' + row['Result'] + ', Expect: ', self.calculator.result)

        CsvReader.data.clear()



       #   DIVISION TEST
    def test_division(self):
        test_data_div = CsvReader('/src/division.csv').data
        print('')
        print('******TEST_DIVISION******')
        for row in test_data_div:
                 self.assertEqual(self.calculator.divide(float(row['Value 1']),float(row['Value 2'])), float(row['Result']))
                 self.assertEqual(float(self.calculator.result), float(row['Result']))
                 print(row['Value 2'] + ' / ' + row['Value 1'] + ' = ' + row['Result'] + ', Expect: ', float(round(self.calculator.result,9)))

        CsvReader.data.clear()


        #   SQUARE TEST
    def test_square(self):
        test_data_square = CsvReader('/src/square.csv').data
        print('')
        print('******TEST_SQUARE******')
        for row in test_data_square:
                 self.assertEqual(self.calculator.squ(int(row['Value 1'])),int(row['Result']))
                 self.assertEqual(self.calculator.result, int(row['Result']))
                 print( 'Square of:', row['Value 1'] + ' = ' + row['Result'] + ', Expect: ', self.calculator.result)

        CsvReader.data.clear()


    def test_square_root(self):
        test_data_square = CsvReader('/src/square_root.csv').data
        print('')
        print('******TEST_SQUARE_ROOT******')
        for row in test_data_square:
                 self.assertAlmostEqual(self.calculator.squ_root(float(row['Value 1'])), float(row['Result']),places=8)

                # self.assertEqual(self.calculator.squ_root(float(row['Value 1'])), float(row['Result']))
                # self.assertEqual(self.calculator.result, float(row['Result']))
                 self.assertAlmostEqual(self.calculator.result, float(row['Result']))
                 print( 'Square Root of:', row['Value 1'] + ' = ' + row['Result'] + ', Expect: ', float(self.calculator.result))


        CsvReader.data.clear()


    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()