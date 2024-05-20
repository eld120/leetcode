


class EncodeDecoder:


    def __init__(self) -> None:
        self.something = list()

    def encode(self, strs: list[str]) -> str:
        for index, string, in enumerate(strs):
            self.something.append((index, string))
        return "".join([f'{x[1]} ' for x in self.something]).rstrip()

    def decode(self, s: str) -> list[str]:
        return [x[1] for x in self.something]