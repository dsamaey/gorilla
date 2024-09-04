from pydantic import BaseModel


class Hobby(BaseModel):
    name: str


class Skill(BaseModel):
    name: str
    description: str
    category: str
