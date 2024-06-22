


def rever_words(s: str) -> str:
    return "".join([f"{word[::-1]} " for word in s.split()]).strip()
