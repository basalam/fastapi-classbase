from unittest import TestCase, main
from api import API, BaseAPI


class UnitTests(TestCase):
    def test_api_deco(self):
        @API.decorator
        class t1:
            def __init__(self, name: str):self.name = name
            def run(self): return self.name
        self.assertEqual(t1(name='omid'), 'omid')

    def test_essentials(self):
        class t1(metaclass=API):
            name: str
        self.assertRaises(NotImplementedError, t1, name='omid')
        self.assertRaises(TypeError, t1, age=13)
        class t1(metaclass=API):
            name: str
            def run(self): return self.name
        self.assertEqual(t1(name='omid'), 'omid')

    def test_extend(self):
        class t1(BaseAPI):
            name: str
            def run(self): return self.name
        class t2(t1, metaclass=API):
            age: int = 20
        self.assertEqual(t1(name='omid').name, 'omid')
        self.assertEqual(t2(name='omid'), 'omid')


if __name__ == '__main__':
    main()
