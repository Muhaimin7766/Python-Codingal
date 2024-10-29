class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words

text = "Hello World from Python"
reverser = StringReverser(text)
print("Original:", text)
print("Reversed:", reverser.reverse_words())
