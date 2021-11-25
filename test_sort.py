import unittest
from unittest import result
import sort
import yaml


class TestSort(unittest.TestCase):

    def test_check_file_1(self):
        file = './files/data.csv'
        result = sort.sortFile(file)
        expected = yaml.dump({'records': [{'name': 'Zelma Ivatt', 'details': 'In division 1 from 2018-01-02 performing Offensive Duties'}, {'name': 'Terza Lowton', 'details': 'In division 1 from 2017-09-15 performing Defensive Duties'}, {'name': 'Zedekiah Miller', 'details': 'In division 3 from 2018-04-09 performing Offensive Duties'}]})
        self.assertEqual(result,expected)

    def test_check_file_2(self):
        file = './files/test_data1.csv'
        result = sort.sortFile(file)
        expected = yaml.dump({'records': [{'name': 'Max Ivatt', 'details': 'In division 1 from 2018-01-02 performing Offensive Duties'}, {'name': 'Tony Rube', 'details': 'In division 1 from 2017-09-15 performing Defensive Duties'}, {'name': 'Zeke Miller', 'details': 'In division 3 from 2018-04-09 performing Offensive Duties'}]})
        self.assertEqual(result,expected)
    
    def test_check_file_3(self):
        file = './files/test_data2.csv'
        result = sort.sortFile(file)
        expected = yaml.dump({'records': [{'name': 'Lucy Ruben', 'details': 'In division 1 from 2017-09-15 performing Defensive Duties'}, {'name': 'Miley Brown', 'details': 'In division 1 from 2018-01-02 performing Offensive Duties'}, {'name': 'Zebedy Mills', 'details': 'In division 3 from 2018-04-09 performing Offensive Duties'}]})
        self.assertEqual(result,expected)

    



if __name__ == '__main__':
    unittest.main()
