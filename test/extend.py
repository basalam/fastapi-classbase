from unittest import TestCase, main
from pydantic import BaseModel
from api import API


class ExtendTest(TestCase):
    def test_e1(self):
        class t1(BaseModel):
            name: str
            def run(self): return self.name
        class t2(t1, metaclass=API):
            age: int = 20
        self.assertEqual(t1(name='omid').name, 'omid')
        self.assertEqual(t2(name='omid'), 'omid')


if __name__ == '__main__':
    main()
