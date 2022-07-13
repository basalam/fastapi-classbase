# FastAPI ClassBase API


## Usage
```py
from fastapi import FastAPI
from faclassbase import API
from typing import Literal


app = FastAPI()


@app.get('/simple-calc')
class TestAPI(metaclass=API):
    a: float
    b: float
    op: Literal['+', '-', '*', '/']
    ops: ClassVar[dict] = {
        '+': lambda a,b:a+b, '-': lambda a,b:a-b,
        '/': lambda a,b:a/b, '*': lambda a,b:a*b}

    def run(self):
        return f'={self.ops[self.op](a, b)}'


app.run()
```
