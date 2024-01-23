
# This class is responsible for counting the syllables in a word. It identifies vowels in a word and applies rules to count syllables,
# which is essential for readability analysis.
class SyllableCounter:
    def __init__(self):
        self.vowels = "aeiouy"

    def count(self, word):
        word = word.lower()
        syllable_count = 0
        if word[0] in self.vowels:
            syllable_count += 1
        for index in range(1, len(word)):
            if word[index] in self.vowels and word[index - 1] not in self.vowels:
                syllable_count += 1
        if word.endswith("e"):
            syllable_count -= 1
        if syllable_count == 0:
            syllable_count += 1
        return syllable_count