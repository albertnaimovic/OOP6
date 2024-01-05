# Create a class method to return the reversed string of a given string.


class Word:
    @classmethod
    def reverse_word(cls, word: str) -> str:
        return word[::-1]


print(Word.reverse_word("Laba diena")) # aneid abaL
