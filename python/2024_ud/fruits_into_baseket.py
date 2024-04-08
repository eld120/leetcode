


def total_fruit(fruits: list[int]) -> int:
    
    left = 0
    right = 0
    longest_stretch = 0
    fruit_quantities = {fruits[right]: 1}
    while right < len(fruits)-1:
        if len(fruit_quantities) < 3:
            right += 1
            try:
                fruit_quantities[fruits[right]] += 1
            except KeyError:
                fruit_quantities[fruits[right]] = 1
            if len(fruit_quantities) == 2:
                longest_stretch = max(right - left + 1, longest_stretch )
        else:
            fruit_quantities[fruits[left]] -= 1
            if fruit_quantities[fruits[left]] == 0:
                del fruit_quantities[fruits[left]]
            left += 1
            
    return longest_stretch



def test_one():
    assert total_fruit([1,2,1]) == 3

def test_two():
    assert total_fruit([0,1,2,2]) == 3


def test_three():
    assert total_fruit([1,2,3,2,2]) == 4