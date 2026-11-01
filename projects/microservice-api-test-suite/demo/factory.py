"""Test-data factory: every test creates the rows it needs, so no manual data setup."""
import itertools

from contracts import User
from service import Db

_seq = itertools.count(1)


class DataFactory:
    def __init__(self, db: Db):
        self.db = db

    def make_user(self, name: str = "Test User") -> User:
        n = next(_seq)
        email = f"user{n}@example.test"
        uid = self.db.execute("INSERT INTO users(name, email) VALUES (?, ?)", (name, email))
        return User(id=uid, name=name, email=email)

    def make_order(self, user: User, total_cents: int = 1999, status: str = "pending") -> int:
        return self.db.execute(
            "INSERT INTO orders(user_id, total_cents, status) VALUES (?, ?, ?)", (user.id, total_cents, status)
        )
