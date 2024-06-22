


def rever_words(s: str) -> str:
    arr = s.split()
    return "".join([f"{word[::-1]} " for word in arr]).strip()
