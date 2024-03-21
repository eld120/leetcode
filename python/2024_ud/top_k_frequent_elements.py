from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k:int)-> List[int]:
    count = Counter(nums)
    return [x[0] for x in count.most_common(k)]

