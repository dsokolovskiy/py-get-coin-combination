from app.main import get_coin_combination
import pytest


@pytest.mark.parametrize(
    "cents, result_coins",
    [
        (1, [1, 0, 0, 0]),
        (6, [1, 1, 0, 0]),
        (17, [2, 1, 1, 0]),
        (50, [0, 0, 0, 2])
    ]
)
def test_get_coin_combination(cents: int,
                              result_coins: list[int]
                              ) -> None:
    assert get_coin_combination(cents) == result_coins
