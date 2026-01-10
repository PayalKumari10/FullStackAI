from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id=1,
    name="Payal",
    email="Pa@3456",
    createAt=datetime(2024, 3, 11, 18, 40),
    address=Address(
        street="Something",
        city="Bihar",
        zip_code="25478"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.model_dump()
print(user)
print("="*30)
print(python_dict)


json_str = user.model_dump_json()
print("="*30)
print(json_str)

