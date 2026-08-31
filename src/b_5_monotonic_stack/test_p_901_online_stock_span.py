from b_5_monotonic_stack.p_901_online_stock_span import StockSpanner

fixtures: list[tuple[list[int], list[int]]] = [
    ([100, 80, 60, 70, 60, 75, 85], [1, 1, 1, 2, 1, 4, 6])
]


def test_next():
    for nums, expected in fixtures:
        spanner = StockSpanner()
        actual = [spanner.next(num) for num in nums]
        assert actual == expected
