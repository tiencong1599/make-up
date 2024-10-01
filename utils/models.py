from beanie import Document
from pydantic import Field


class Account(Document):
    username: str = Field(max_length=50)
    password: str = Field(max_length=256)
    is_admin: bool = Field(default=False)
    is_active: bool = Field(default=True)

    # class Settings:
    #     collection_name = 'accounts'