from .syllable_counter import SyllableCounter

# This class performs various text analysis operations. It utilizes the SyllableCounter to perform syllable-related computations
# and calculates different readability scores such as Flesch Reading Ease, Gunning Fog Index, etc.
class TextAnalyzer:
    def __init__(self):
        self.syllable_counter = SyllableCounter()

    def complex_word_count(self, text):
        words = text.split()
        complex_words = [word for word in words if self.syllable_counter.count(word) >= 3]
        return len(complex_words)

    def flesch_reading_ease(self, total_sentences, total_words, total_syllables):
        return 206.835 - 1.015 * (total_words / total_sentences) - 84.6 * (total_syllables / total_words)

    def flesch_kincaid(self, total_sentences, total_words, total_syllables):
        return 0.39 * (total_words / total_sentences) + 11.8 * (total_syllables / total_words) - 15.59

    def gunning_fog(self, total_sentences, total_words, total_complex_words):
        return 0.4 * ((total_words / total_sentences) + 100 * (total_complex_words / total_words))

    def smog(self, total_sentences, total_complex_words):
        return 1.0430 * (30 * (total_complex_words / total_sentences)) ** 0.5 + 3.1291

    def linsear_write(self, text, total_sentences):
        sample = text.split()[:100]
        easy_word = len([word for word in sample if self.syllable_counter.count(word) < 3])
        hard_word = len(sample) - easy_word
        return (easy_word + (hard_word * 3)) / total_sentences

    def coleman_liau(self, total_sentences, total_words, total_characters):
        return 0.0588 * (total_characters / total_words * 100) - 0.296 * (total_sentences / total_words * 100) - 15.8

    def ari(self, total_sentences, total_words, total_characters):
        return 4.71 * (total_characters / total_words) + 0.5 * (total_words / total_sentences) - 21.43

    def calculate_readability_scores(self, text):
        sentences = text.split('.')
        words = text.split()
        characters = ''.join(words)
        syllables = sum(self.syllable_counter.count(word) for word in words)
        complex_words = self.complex_word_count(text)

        # Total counts
        total_sentences = len(sentences)
        total_words = len(words)
        total_characters = len(characters)
        total_syllables = syllables
        total_complex_words = complex_words

        return {
            'flesch_reading_ease': self.flesch_reading_ease(total_sentences, total_words, total_syllables),
            'flesch_kincaid': self.flesch_kincaid(total_sentences, total_words, total_syllables),
            'gunning_fog': self.gunning_fog(total_sentences, total_words, total_complex_words),
            'smog': self.smog(total_sentences, total_complex_words),
            'linsear_write': self.linsear_write(text, total_sentences),
            'coleman_liau': self.coleman_liau(total_sentences, total_words, total_characters),
            'ari': self.ari(total_sentences, total_words, total_characters)
        }
