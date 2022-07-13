from unittest import TestCase, main

from pydantic import BaseModel
from api import API
from fastapi import FastAPI
import uvicorn


class ExtendTest(TestCase):
    def e1_test(self):
        app = FastAPI()
        class t1(BaseModel):
            name: str
            def run(self): return self.name
        @app.get('/e1')
        class t2(t1, metaclass=API):
            age: int = 20
        self.assertEqual(t1(name='omid').name, 'omid')
        self.assertEqual(t2(name='omid'), 'omid')
        uvicorn.run(app)


if __name__ == '__main__':
    main()
