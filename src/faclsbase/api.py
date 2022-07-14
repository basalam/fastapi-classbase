import inspect
import makefun
from pydantic.main import ModelMetaclass
try:
    from .base_api import BaseAPI
except:
    from base_api import BaseAPI


class API(ModelMetaclass):
    """
        API is a metaclass that it's goal is
        coverts `__init__` to a function to call `__init__()` and return `obj.run()`

    """

    @staticmethod
    def convert__init__to_instantiate_and_call_run(_class):
        generic_instantiate_and_call_run = lambda **kwargs: _class(**kwargs).run()
        return makefun.create_function(
            func_signature=inspect.signature(_class),
            func_impl=generic_instantiate_and_call_run,
            func_name=_class.__name__)

    def __new__(cls, _, bases, dct):
        if BaseAPI not in bases:
            bases = (*bases, BaseAPI)
        class_ = super().__new__(cls, _, bases, dct)
        return cls.convert__init__to_instantiate_and_call_run(class_)
