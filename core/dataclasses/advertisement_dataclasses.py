from dataclasses import dataclass
from datetime import datetime
from typing import List
import decimal

from core.dataclasses.user_dataclasses import User


@dataclass
class FuelType:
    id: int
    name: str


@dataclass
class Transmission:
    id: int
    name: str


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Status:
    id: int
    name: str


@dataclass
class Advertisement:
    id: int
    car_brand: str
    car_model: str
    engine: decimal.Decimal
    vin: str
    insurance: str
    price: float
    price_period: str
    mileage: str
    pledge: bool
    purpose: str
    driver: bool
    comment: str
    location: str
    fuel_type: List[FuelType]
    transmission: Transmission
    category: Category
    user: User
    status: Status
    photos: List[str]
    created_at: datetime
    updated_at: datetime
