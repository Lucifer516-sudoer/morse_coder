from typing import Dict, List

CHAR_TO_MORSE: Dict[str, str] = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
}

MORSE_TO_CHAR: Dict[str, str] = {
    v: k for k, v in CHAR_TO_MORSE.items()
}  # dict comprehension

WORD_SEPARATOR = "/"
CHAR_SEPARATOR = " "


def convert_to_morse(text: str) -> str:
    """Convert a string to Morse code."""
    morse: List[str] = []
    for word in text.upper().split():
        morse_word = []
        for char in word:
            if char in CHAR_TO_MORSE:
                morse_word.append(CHAR_TO_MORSE[char])
        morse.append(CHAR_SEPARATOR.join(morse_word))
    return WORD_SEPARATOR.join(morse)


def convert_to_text(morse: str) -> str:
    """Convert Morse code to text."""
    text: List[str] = []
    for word in morse.split(WORD_SEPARATOR):
        decoded_word = []
        for char in word.split(CHAR_SEPARATOR):
            if char in MORSE_TO_CHAR:
                decoded_word.append(MORSE_TO_CHAR[char])
        text.append("".join(decoded_word))
    return " ".join(text)


if __name__ == "__main__":
    original_text = "Hello, World!"
    morse_code = convert_to_morse(original_text)
    decoded_text = convert_to_text(morse_code)

    print(f"Original: {original_text}")
    print(f"Morse: {morse_code}")
    print(f"Decoded: {decoded_text}")
