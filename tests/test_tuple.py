import pytest


@pytest.mark.parametrize("a, b, expected", [
    ((1, 2), (1, 2), True),
    ((1, 2), (2, 3), False)
], ids=('True', 'False'))
def test_tuple_comparison(a, b, expected):
    assert (a == b) == expected


def test_tuple_access_out_of_indexes():
    c = (1, 2, 3)
    try:
        c[4]
    except IndexError:
        assert True
    else:
        assert False


def test_list_to_tuple_conversion():
    lst = [1, 2, 3]
    d = tuple(lst)
    assert type(d) == tuple

