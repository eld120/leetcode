"""
list of transactions: id: int, amount: int, memo: str, date - dd/mm/yyyy: iso formatted string (types?)
pt 1: go through the list, ret list of lists of transactios where they are grouped where their date/amount/memo are the same (looking for dups, memo case insensitive), just need id's returned
pt 2: 
"""
from typing import List


def return_duplicates(transactions: List):
    # init answer list, set - duplicates
    answer = dict()

    # for every transaction (concat amount, memo, date)
    for transaction in transactions:
        # separate the memo             {str: {'memo': [a;lskjf;sldkjaf], 'id': [1,2,3] }}
        # compare lengths then determine if shorter prefix of longer
        # if true then it's duplicate
        memo = f"{transaction['memo'].lower()}"
        hashable = f"{transaction['amount']}{transaction['date']}"
        # if amount/memo/date in set duplicates
        if hashable in answer:
            shortest_len = len(memo)
            shortest_memo = memo

            for m in answer[hashable]["memo"]:
                # split inc and existing memos and compare values index 0 then 1 , etc

                if len(m) < shortest_len:
                    shortest_len = len(m)
                    shortest_memo = m
                if (
                    shortest_memo == memo[: shortest_len + 1]
                ):  # what if memo is not in dict of memos
                    answer[hashable]["memo"] += [memo]
                    answer[hashable]["id"] += [transaction["id"]]
        else:
            answer[hashable] = {"memo": [memo], "id": [transaction["id"]]}
        # append answer list

    # return answer list
    return [x for x in answer.values() if len(x) >= 2]


def test_one():
    assert return_duplicates(
        [
            {
                "id": 0,
                "date": "2021-05-22",
                "memo": "Blue Bottle Coffee",
                "amount": 522,
            },
            {
                "id": 1,
                "date": "2021-05-22",
                "memo": "Blue Bottle San Jose",
                "amount": 522,
            },
            {"id": 2, "date": "2021-05-22", "memo": "Blue Bottle", "amount": 522},
            {
                "id": 3,
                "date": "2021-05-22",
                "memo": "BLUE BOTTLE COFFEE",
                "amount": 522,
            },
            {
                "id": 4,
                "date": "2021-05-22",
                "memo": "Blue Bottle Coffee",
                "amount": 699,
            },
            {"id": 5, "date": "2021-05-22", "memo": "Lyft", "amount": 522},
            {
                "id": 6,
                "date": "2021-05-22",
                "memo": "Blue Bottle Coffee ON CC (x8725)",
                "amount": 522,
            },
            {
                "id": 7,
                "date": "2021-05-23",
                "memo": "Blue Bottle Coffee",
                "amount": 522,
            },
            {"id": 8, "date": "2021-05-24", "memo": "Lyft", "amount": 522},
            {
                "id": 9,
                "date": "2021-05-25",
                "memo": "Blue Bottle Coffee ON CC (x8725)",
                "amount": 522,
            },
            {"id": 10, "date": "2021-05-26", "memo": "Uber", "amount": 522},
            {
                "id": 11,
                "date": "2021-05-29",
                "memo": "Blue Bottle San Jose",
                "amount": 522,
            },
            {"id": 12, "date": "2021-05-29", "memo": "Lyft", "amount": 522},
            {"id": 13, "date": "2021-05-29", "memo": "Lyft 2PM", "amount": 522},
            {
                "id": 14,
                "date": "2021-06-01",
                "memo": "Blue Bottle Coffee ON CC (x8725)",
                "amount": 522,
            },
            {"id": 15, "date": "2021-06-04", "memo": "BLUE BOTTLE", "amount": 522},
            {"id": 16, "date": "2021-06-04", "memo": "BLUE BOTTLE", "amount": 522},
        ]
    ) == [[0, 3], [15, 16]]


# if __name__ == '__main__':
#     print(return_duplicates([
#   {"id": 0, "date": "2021-05-22", "memo": "Blue Bottle Coffee", "amount": 522},
#   {"id": 1, "date": "2021-05-22", "memo": "Blue Bottle San Jose", "amount": 522},
#   {"id": 2, "date": "2021-05-22", "memo": "Blue Bottle", "amount": 522},
#   {"id": 3, "date": "2021-05-22", "memo": "BLUE BOTTLE COFFEE", "amount": 522},
#   {"id": 4, "date": "2021-05-22", "memo": "Blue Bottle Coffee", "amount": 699},
#   {"id": 5, "date": "2021-05-22", "memo": "Lyft", "amount": 522},
#   {"id": 6, "date": "2021-05-22", "memo": "Blue Bottle Coffee ON CC (x8725)", "amount": 522},
#   {"id": 7, "date": "2021-05-23", "memo": "Blue Bottle Coffee", "amount": 522},
#   {"id": 8, "date": "2021-05-24", "memo": "Lyft", "amount": 522},
#   {"id": 9, "date": "2021-05-25", "memo": "Blue Bottle Coffee ON CC (x8725)", "amount": 522},
#   {"id": 10, "date": "2021-05-26", "memo": "Uber", "amount": 522},
#   {"id": 11, "date": "2021-05-29", "memo": "Blue Bottle San Jose", "amount": 522},
#   {"id": 12, "date": "2021-05-29", "memo": "Lyft", "amount": 522},
#   {"id": 13, "date": "2021-05-29", "memo": "Lyft 2PM", "amount": 522},
#   {"id": 14, "date": "2021-06-01", "memo": "Blue Bottle Coffee ON CC (x8725)", "amount": 522},
#   {"id": 15, "date": "2021-06-04", "memo": "BLUE BOTTLE", "amount": 522}
# ])


# )
