# FastAPI ClassBase API

## install

`pip install git+https://github.com/omidekz/fastapi-classbase`

## Usage

```py
from fastapi import FastAPI, Query
from faclsbase import API
from typing import List
from pydantic import Field

app = FastAPI()


@app.get('/simple-calc')
class SumAPI(metaclass=API):
    numbers: List[int] = Field(Query(None))

    def run(self):
        return f'={sum(self.numbers)}'
```

## inheritance

```py
from faclsbase import API, BaseAPI as _BaseAPI
from typing import ClassVar


app = ...


class BaseAPI(_BaseAPI):
    repo: ClassVar[object] = None


@app.get('...')
class XAPI(BaseAPI, metaclass=API):
    pass
```

## or

```py

```