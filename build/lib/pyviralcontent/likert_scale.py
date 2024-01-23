
# This class manages the Likert scale interpretation and qualitative descriptors for readability scores. 
# It provides methods to determine the Likert scale based on scores and to get qualitative descriptors for Likert scores.
class LikertScale:
    def __init__(self):
        self.likert_scale_interpretation = {
            'flesch_reading_ease': [
                (lambda score: self.in_range(score, 90, float('inf')), 5),  # Very Easy
                (lambda score: self.in_range(score, 70, 90), 4),            # Easy
                (lambda score: self.in_range(score, 50, 70), 3),            # Fairly Easy
                (lambda score: self.in_range(score, 30, 50), 2),            # Difficult
                (lambda score: self.in_range(score, 0, 30), 1),             # Very Confusing
            ],
            'flesch_kincaid': [
                (lambda score: score <= 5, 5),     # Very Easy
                (lambda score: self.in_range(score, 5, 6), 4),   # Easy
                (lambda score: self.in_range(score, 6, 7), 3),   # Fairly Easy
                (lambda score: self.in_range(score, 7, 9), 2),   # Difficult
                (lambda score: score >= 9, 1),     # Very Confusing
            ],
            'gunning_fog': [
                (lambda score: score <= 6, 5),     # Very Easy
                (lambda score: self.in_range(score, 6, 8), 4),   # Easy
                (lambda score: self.in_range(score, 8, 12), 3),  # Fairly Easy
                (lambda score: self.in_range(score, 12, 17), 2), # Difficult
                (lambda score: score >= 17, 1),    # Very Confusing
            ],
            'smog': [
                (lambda score: score <= 6, 5),     # Very Easy
                (lambda score: self.in_range(score, 6, 8), 4),   # Easy
                (lambda score: self.in_range(score, 8, 12), 3),  # Fairly Easy
                (lambda score: self.in_range(score, 12, 14), 2), # Difficult
                (lambda score: score >= 14, 1),    # Very Confusing
            ],
            'linsear_write': [
                (lambda score: score <= 5, 5),    # Very Easy
                (lambda score: self.in_range(score, 5, 8), 4),  # Easy
                (lambda score: self.in_range(score, 8, 12), 3), # Fairly Easy
                (lambda score: self.in_range(score, 12, 15), 2),# Difficult
                (lambda score: score >= 15, 1),   # Very Confusing
            ],
            'coleman_liau': [
                (lambda score: score <= 5, 5),    # Very Easy
                (lambda score: self.in_range(score, 5, 8), 4),  # Easy
                (lambda score: self.in_range(score, 8, 12), 3), # Fairly Easy
                (lambda score: self.in_range(score, 12, 15), 2),# Difficult
                (lambda score: score >= 15, 1),   # Very Confusing
            ],
            'ari': [
                (lambda score: score <= 2, 5),    # Very Easy
                (lambda score: self.in_range(score, 2, 4), 4),  # Easy
                (lambda score: self.in_range(score, 4, 7), 3),  # Fairly Easy
                (lambda score: self.in_range(score, 7, 10), 2), # Difficult
                (lambda score: score >= 10, 1),   # Very Confusing
            ],
            'default': [
                (lambda score: score <= 2, 5),    # Very Easy
                (lambda score: self.in_range(score, 2, 4), 4),  # Easy
                (lambda score: self.in_range(score, 4, 6), 3),  # Fairly Easy
                (lambda score: self.in_range(score, 6, 8), 2),  # Difficult
                (lambda score: score >= 8, 1),    # Very Confusing
            ]
        }
        
        self.qualitative_descriptors = {
            5: 'Excellent/Very Clear',
            4: 'Good/Clear',
            3: 'Average/Somewhat Clear',
            2: 'Below Average/Confusing',
            1: 'Poor/Unclear',
            0: 'Very Poor/Very Unclear'
        }

    @staticmethod
    def in_range(score, start, end):
        return start <= score < end

    def determine_likert_scale(self, score, test_name):
        scale_ranges = self.likert_scale_interpretation.get(test_name, self.likert_scale_interpretation['default'])
        for check_func, likert_value in scale_ranges:
            if check_func(score):
                return likert_value
        return 0
    
    def max_scale(self, test_name):
        if test_name in self.likert_scale_interpretation: 
            # Find the max Likert scale value for the test
            return max(value for _, value in self.likert_scale_interpretation[test_name])
        else:
            # Default max Likert scale value
            return max(value for _, value in self.likert_scale_interpretation['default'])

    def get_qualitative_descriptor(self, likert_score):
        return self.qualitative_descriptors.get(likert_score, 'Undefined')
    
    def calculate_average_score(self, df):
      average_score = df['Score'].mean()
      overall_likert = self.determine_likert_scale(average_score, 'default')
      overall_quality = self.get_qualitative_descriptor(overall_likert)
      return average_score, overall_likert, overall_quality