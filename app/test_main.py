import pytest
import app.main


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_age",
    [
        (0, 0, [0, 0],
        id="Test with age equal to zero"),
        (14, 14, [0, 0],
        id="Not yet 1 human year"),
        (15, 15, [1, 1],
        id="First year should start from 15"),
        (23, 23, [1, 1],
        id="Not yet 2 human years"),
        (24, 24, [2, 2],
        id="Second year should start from 24"),
        (27, 27, [2, 2],
        id="Not yet 3 human years"),
        (28, 28, [3, 2],
        id="Cat years are going faster then dog years"),
        (100, 100, [22, 17],
        id="Test with high age"),
        (234, 356, [57, 70],
        id="Test with different high age")
    ])
def test_age(cat_age: int, dog_age: int, expected: list) -> None:
    assert app.main.get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 1),
        (1, -1)
    ])
def test_negative_age_raises_value_error(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        app.main.get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15.5, 15),
        (15, "15"),
        (15, 15.5),
        (None, 15),
        (15, None)
    ],
)
def test_invalid_type_raises_type_error(
    cat_age: str | int | float | None,
    dog_age: str | int | float | None,
) -> None:
    with pytest.raises(TypeError):
        app.main.get_human_age(cat_age, dog_age)
