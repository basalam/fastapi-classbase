from inspect import signature
import makefun
from pydantic import BaseModel
from pydantic.main import ModelMetaclass



instantiate_and_call_run = lambda _class: lambda **kwargs: _class(**kwargs).run()


class BaseAPI(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        extra = 'ignore'

    def run(self):
        raise NotImplementedError


class API(ModelMetaclass):
    """
        API is a metaclass that it's goal is
        coverts `__init__` to a function to call `__init__()` and return `obj.run()`
        
    """

    @staticmethod
    def convert__init__to_instantiate_and_call_run_lambda(_class):
        return makefun.create_function(
            signature(_class), instantiate_and_call_run(_class), _class.__name__)

    def __new__(cls, _, bases, dct):
        bases = list(bases)
        if BaseAPI not in bases:
            bases = bases + [BaseAPI]
        class_ = super().__new__(cls, _, tuple(bases), dct)
        return cls.convert__init__to_instantiate_and_call_run_lambda(class_)
