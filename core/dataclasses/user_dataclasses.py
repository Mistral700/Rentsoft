from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    id: int
    name: str
    surname: str
    age: int
    avatar: str
    created_at: datetime
    updated_at: datetime


@dataclass
class User:
    id: int
    email: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    is_staff: bool
    created_at: datetime
    updated_at: datetime
    profile: ProfileDataClass
