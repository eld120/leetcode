from typing import List


def bubbles_being_sorted(please_sort_me: List) -> List:
    '''
    implementing bubble sort I guess
    '''
    is_sorted = False
    counter = 0
    while not is_sorted:
        try:
            if please_sort_me[counter] <= please_sort_me[counter + 1]:
                counter += 1
            else:
                lower_value = please_sort_me[counter + 1]
                higher_value = please_sort_me[counter]
                please_sort_me[counter] = lower_value
                please_sort_me[counter + 1] = higher_value
                bubbles_being_sorted(please_sort_me)
        except IndexError:
            return please_sort_me

    



def test_one():
    assert bubbles_being_sorted([3,2,1]) == [1,2,3]

def test_two():
    assert bubbles_being_sorted([2,1]) ==  [1,2]
        
def test_three():
    assert bubbles_being_sorted([3,4,1231,23,35,5251,231,53,2344,634,5124,1,56,46,3573,7,51,421,42,14,13,63,46,1,4,31,4,4,56,3,46,7,7,6,6,4,3,22,21,2,6,26,35,4,34,5,43,9]) == [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 9, 13, 14, 21, 22, 23, 26, 31, 34, 35, 35, 42, 43, 46, 46, 46, 51, 53, 56, 56, 63, 231, 421, 634, 1231, 2344, 3573, 5124, 5251]       