def reverse_string(s: list[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        temp_l = s[left]
        temp_r = s[right]
        s[left] = temp_r
        s[right] = temp_l
        left += 1
        right -= 1
    return s


def test_one():
    assert reverse_string(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
