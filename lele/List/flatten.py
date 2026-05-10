def flatten(items):
    for x in items:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x


def test_usage():
    nested = [1, [2, [3, 4], 5], 6, [7, 8]]
    result = list(flatten(nested))
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert result == expected, f"Expected {expected}, got {result}"
    
def test_already_flat_list():
    flat_list = [1, 2, 3, 4, 5]
    result = list(flatten(flat_list))
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Expected {expected}, got {result}"
    
def test_empty_list():
    empty = []
    result = list(flatten(empty))
    expected = []
    assert result == expected, f"Expected {expected}, got {result}"
    
def test_deeply_nested_list():
    deep = [1, [2, [3, [4, [5]]]]]
    result = list(flatten(deep))
    expected = [1, 2, 3, 4, 5]
    assert result == expected, f"Expected {expected}, got {result}"
