from pydantic import BaseModel


class BaseAPI(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        extra = 'ignore'

    def run(self):
        raise NotImplementedError
