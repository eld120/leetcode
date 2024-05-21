from string import ascii_lowercase, ascii_uppercase


def encode_string(sentence: str, right_shift: int) -> str:
    """

    rot("Hello, Rick", 1) -> "Ifmmp, Sjdl" # Preserve case and punctuation
    rot(rot("Hello, Rick", 1), -1) -> "Hello, Rick"
    """
    answer = []
    # loop through sentence, preserve anything that is not ascii letters
    for char in sentence:
        # char in uppercase/lowercase and ord(char) + shift in range 65/97 + 26
        if char in ascii_lowercase:
            if (ord(char) + right_shift) in range(97, 124):
                # go ahead with the shift
                answer.append(chr(ord(char) + right_shift))
            else:
                answer.append(chr(((ord(char) + right_shift - 97) % 26) + 97))
        elif char in ascii_uppercase:
            if (ord(char) + right_shift) in range(65, 92):
                # go ahead with the shift
                answer.append(chr(ord(char) + right_shift))
            else:
                answer.append(chr(((ord(char) + right_shift - 65) % 26) + 65))
            # else character = ord(char) + shift - 26
            # answer.append(chr())
        else:
            answer.append(char)
    # return "".join(answer)
    return "".join(answer)


def test_given_example():
    assert encode_string("Hello, Rick", 1) == "Ifmmp, Sjdl"
    assert encode_string(encode_string("Hello, Rick", 1), -1)  == "Hello, Rick"
    assert encode_string("HELLO", 27) == "IFMMP"

def test_unexpected_input():
    assert encode_string("HELLO", -1) == "GDKKN"
