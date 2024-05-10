from secrets import token_urlsafe


class Codec:
    """
    TinyURL is a URL shortening service where you enter a URL such as
    https://leetcode.com/problems/design-tinyurl and it returns a short
    URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL
    and decode a tiny URL.

    There is no restriction on how your encode/decode algorithm should work.
    You just need to ensure that a URL can be encoded to a tiny URL and the
    tiny URL can be decoded to the original URL.

    Implement the Solution class:

    Solution() Initializes the object of the system.
    String encode(String longUrl) Returns a tiny URL for the given longUrl.
    String decode(String shortUrl) Returns the original long URL for the given
    shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
    """

    def __init__(self) -> None:
        self.lookup = dict()

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""

        rand_hash = token_urlsafe(8)
        self.lookup[rand_hash] = longUrl
        # breakpoint()
        return f"https://tinyurl.com/{rand_hash}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""

        url_list = []
        for char in reversed(shortUrl):
            if char != "/":
                url_list.append(char)
            else:
                break
        # breakpoint()
        return self.lookup["".join(url_list[::-1])]


def test_one():
    url_string = "https://leetcode.com/problems/design-tinyurl"
    codec = Codec()
    encoded = codec.encode(url_string)
    assert codec.decode(encoded) == url_string
