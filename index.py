# Task 1 - Alpahabet

class Alphabet:

    ua_lang = "UA"
    ua_letters = list("абвгґдеєжзиіїйклмнопрстуфхцчшщьюя")

    def __init__(self, lang=ua_lang, letters=ua_letters):
        if not isinstance(letters, (list, str)):
            raise TypeError("Letters must be list or string")

        self.lang = lang
        self.letters = list(letters)

    def print_alphabet(self):
        print(" ".join(self.letters))

    def letters_num(self):
        return len(self.letters)

    def is_ua_lang(self, text):
        if not isinstance(text, str):
            return False
        text = text.lower()
        return all(char in self.ua_letters or not char.isalpha() for char in text)


class EngAlphabet(Alphabet):
    __en_letters_num = 26

    def __init__(self):
        super().__init__("EN", "abcdefghijklmnopqrstuvwxyz")

    def is_en_letter(self, letter):
        if not isinstance(letter, str) or len(letter) != 1:
            return False
        return letter.lower() in self.letters

    def letters_num(self):
        return self.__en_letters_num

    @staticmethod
    def example():
        return "Jack was hungry. He walked to the kitchen. He got out some eggs. He took out some oil. He placed a skillet on the stove. Next, he turned on the heat. He poured the oil into the skillet. He cracked the eggs into a bowl. He stirred the eggs. Then, he poured them into the hot skillet. He waited while the eggs cooked. They cooked for two minutes. He heard them cooking. They popped in the oil."


#  --- TESTS ---
print("\n--- PART 1 TESTS ---")
eng = EngAlphabet()
eng.print_alphabet()
print("Letters count:", eng.letters_num())
print("Is 'J' English?", eng.is_en_letter("J"))

ua = Alphabet()
print("Is 'Щ' Ukrainian?", ua.is_ua_lang("Щ"))
print("Example:", EngAlphabet.example())
