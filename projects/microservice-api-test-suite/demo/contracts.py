"""Response contracts. Strict + extra="forbid" so silent API drift fails the tests."""
from typing import Literal

from pydantic import BaseModel, ConfigDict


class Contract(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")


class User(Contract):
    id: int
    name: str
    email: str


class Order(Contract):
    id: int
    total_cents: int
    status: Literal["pending", "paid", "shipped"]


class OrderList(Contract):
    orders: list[Order]


class ErrorBody(Contract):
    error: str
