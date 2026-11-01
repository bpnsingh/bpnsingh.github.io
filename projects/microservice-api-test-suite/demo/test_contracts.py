import pytest
from pydantic import ValidationError

from contracts import ErrorBody, OrderList, User


def test_user_response_matches_contract(factory, get):
    user = factory.make_user(name="Asha")

    resp = get(f"/users/{user.id}")

    assert resp.status_code == 200
    assert User.model_validate(resp.json()) == user


def test_unknown_user_returns_documented_404(factory, get):
    resp = get("/users/999999")

    assert resp.status_code == 404
    assert ErrorBody.model_validate(resp.json()).error == "not_found"


@pytest.mark.parametrize("status", ["pending", "paid", "shipped"])
def test_orders_match_contract_for_every_status(factory, get, status):
    user = factory.make_user()
    factory.make_order(user, total_cents=4250, status=status)

    body = OrderList.model_validate(get(f"/users/{user.id}/orders").json())

    assert [(o.total_cents, o.status) for o in body.orders] == [(4250, status)]


def test_user_without_orders_gets_an_empty_list(factory, get):
    user = factory.make_user()

    body = OrderList.model_validate(get(f"/users/{user.id}/orders").json())

    assert body.orders == []


def test_orders_are_scoped_to_their_user(factory, get):
    mine, other = factory.make_user(), factory.make_user()
    factory.make_order(mine, total_cents=100)
    factory.make_order(other, total_cents=999)

    body = OrderList.model_validate(get(f"/users/{mine.id}/orders").json())

    assert [o.total_cents for o in body.orders] == [100]


def test_contract_catches_silent_field_rename(service, factory, get):
    """The point of contract tests: a renamed field must fail loudly, not pass silently."""
    user = factory.make_user()
    factory.make_order(user)
    service.drift = True  # service now returns "total" instead of "total_cents"

    with pytest.raises(ValidationError):
        OrderList.model_validate(get(f"/users/{user.id}/orders").json())
