# FastAPI ClassBase API


### install
    pip install git+https://github.com/omidekz/fastapi-classbase

## Usage
```py
from fastapi import FastAPI
from faclsbase import API
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
```

# inheritance
````py
from faclsbase import API, BaseAPI as _BaseAPI
from typing import ClassVar


app = ...


class BaseAPI(_BaseAPI):
    repo: ClassVar[object] = None


@app.get('...')
class XAPI(BaseAPI, metaclass=API):
    ...
