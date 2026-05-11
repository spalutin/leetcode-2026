from block_3_hare_tortoise.problem_202_happy_number import Solution


def test_is_happy():
    print()
    assert Solution().isHappy(19) == True
    assert Solution().isHappy(2) == False
