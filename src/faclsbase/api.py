from inspect import signature
import makefun
from pydantic import BaseModel
from pydantic.main import ModelMetaclass



class BaseAPI(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        extra = 'ignore'

    def run(self):
        raise NotImplementedError


class API(ModelMetaclass):
    def __new__(cls, _, bases, dct):
        bases = list(bases)
        if BaseAPI not in bases:
            bases = bases + [BaseAPI]
        class_ = super().__new__(cls, _, tuple(bases), dct)
        return makefun.create_function(
            signature(class_), lambda *args, **kwargs: class_(*args, **kwargs).run(), class_.__name__)
