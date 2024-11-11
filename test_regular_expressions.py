import re, unittest


class TestRegularExpressions(unittest.TestCase):

    def test_has_used_default_constructor(self):
        class_name = 'Parallelogram'
        pattern = f'\\b\\w+\\s*=\\s*{class_name}\\s*\\(\\s*\\)'
        text_to_test = self.__get_default_construtor_test_string()
        self.assertIsNotNone(re.search(pattern, text_to_test))

    def test_has_correct_area_formula(self):
        pattern = r"\s*self\.side1\s*\*\s*self\.side2\s*\*\s*sin\s*\(\s*radians\s*\(\s*self\.angle\s*\)\s*\)"
        text_to_test = self.__get_area_formula_test_string()
        self.assertIsNotNone(re.search(pattern, text_to_test))

    def __get_default_construtor_test_string(self) -> str:
        return 'p = Parallelogram()'

    def __get_area_formula_test_string(self) -> str:
        return 'self.side1 * self.side2 * sin ( radians (self.angle))'


if __name__ == '__main__':
    unittest.main()
