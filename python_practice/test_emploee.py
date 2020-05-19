# c11_雇员
import unittest
from employment import Employee


class EmployeeTestCase(unittest.TestCase):
    """测试默认涨薪和任意给定涨薪"""

    def setUp(self):
        self.my_employee = Employee('hao', 'lang', 10000)

    def test_give_defalut_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(15000, self.my_employee.salary)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(20000, self.my_employee.salary)


unittest.main()