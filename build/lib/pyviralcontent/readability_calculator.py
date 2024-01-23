import numpy as np
import pandas as pd
from .text_analyzer import TextAnalyzer
from .likert_scale import LikertScale

# This class is responsible for calculating readability scores for a given text based on content type. 
# It uses TextAnalyzer to compute scores and LikertScale for interpreting scores. 
# It also provides functionality to calculate the probability of content going viral.
class ReadabilityCalculator:
    def __init__(self):
        self.content_type_formulas = {
            'scientific': ['gunning_fog', 'coleman_liau', 'ari'],
            'blog': ['flesch_reading_ease', 'flesch_kincaid'],
            'video': ['smog', 'flesch_reading_ease'],
            'technical': ['linsear_write', 'ari'],
            'fictional': ['flesch_kincaid', 'coleman_liau'],
            'legal': ['gunning_fog', 'smog'],
            'educational': ['flesch_kincaid', 'linsear_write'],
            'news': ['flesch_reading_ease', 'gunning_fog'],
            'advertising': ['flesch_reading_ease', 'coleman_liau'],
            'social_media': ['flesch_reading_ease', 'linsear_write']
        }
        self.text_analyzer = TextAnalyzer()
        self.likert_scale = LikertScale()

    def calculate_scores_by_content_type(self, text, content_type):
        scores = self.text_analyzer.calculate_readability_scores(text)
        selected_scores = {test: score for test, score in scores.items() if test in self.content_type_formulas[content_type]}
        
        df = pd.DataFrame(list(selected_scores.items()), columns=['Test', 'Score'])
        df['Likert_Scale'] = df.apply(lambda row: self.likert_scale.determine_likert_scale(row['Score'], row['Test']), axis=1)
        df['Qualitative_Descriptors'] = df['Likert_Scale'].apply(lambda x: self.likert_scale.get_qualitative_descriptor(x))
        return df

    def calculate_virality_probability(self, df):
      virality_weights = {'flesch_reading_ease': 0.15,'flesch_kincaid': 0.15,'gunning_fog': 0.1,'smog': 0.1,'linsear_write': 0.1,'coleman_liau': 0.2,'ari': 0.2}
      df['Weighted_Likert'] = df['Test'].map(virality_weights).fillna(0) * df['Likert_Scale']
      virality_score = df['Weighted_Likert'].sum() / df['Test'].map(virality_weights).fillna(0).sum()
      probability_of_going_viral = virality_score / 5  # Assuming 5 is the max Likert scale value
      return probability_of_going_viral

    def calculate_scores_by_content_type_keener(self, text, content_type):
        scores_dict = self.text_analyzer.calculate_readability_scores(text)
        selected_scores_dict = {test: score for test, score in scores_dict.items() if test in self.content_type_formulas[content_type]}
        
        scores = list(selected_scores_dict.values())
        keener_scores = self.keener_method(scores)
        
        keener_df = pd.DataFrame(list(selected_scores_dict.keys()), columns=['Test'])
        keener_df['Score'] = keener_scores
        keener_df['Likert_Scale'] = keener_df['Score'].apply(lambda x: self.likert_scale.determine_likert_scale(x, 'default'))
        keener_df['Qualitative_Descriptors'] = keener_df['Likert_Scale'].apply(lambda x: self.likert_scale.get_qualitative_descriptor(x))
        
        overall_score = np.dot(keener_scores, scores)
        overall_likert = self.likert_scale.determine_likert_scale(overall_score, 'default')
        overall_quality = self.likert_scale.get_qualitative_descriptor(overall_likert)
        
        overall_df = pd.DataFrame([['OVERALL SCORE', overall_score, overall_likert, overall_quality]], columns=['Test', 'Score', 'Likert_Scale', 'Qualitative_Descriptors'])
        
        return pd.concat([keener_df, overall_df], ignore_index=True)
    
    # def calculate_virality_probability(self, df):
    #   virality_weights = {
    #       'flesch_reading_ease': 0.15,
    #       'flesch_kincaid': 0.15,
    #       'gunning_fog': 0.1,
    #       'smog': 0.1,
    #       'linsear_write': 0.1,
    #       'coleman_liau': 0.2,
    #       'ari': 0.2
    #       }
    #   df['Weighted_Likert'] = df['Test'].map(virality_weights).fillna(0) * df['Likert_Scale']
    #   virality_score = df['Weighted_Likert'].sum() / df['Test'].map(virality_weights).fillna(0).sum()
    #   probability_of_going_viral = virality_score / 5  # Assuming 5 is the max Likert scale value
    #   return probability_of_going_viral
  
    def calculate_virality_probability(self, df, content_type):
        virality_weights = {'flesch_reading_ease': 0.15,'flesch_kincaid': 0.15,'gunning_fog': 0.1,
                          'smog': 0.1,'linsear_write': 0.1,'coleman_liau': 0.2,'ari': 0.2}
        df['Weighted_Likert'] = df['Test'].map(virality_weights).fillna(0) * df['Likert_Scale']
        virality_score = df['Weighted_Likert'].sum()
        # Get the tests relevant for the content type
        relevant_tests = self.content_type_formulas[content_type]
        # Calculate the sum of the maximum possible weighted scores for the relevant tests
        max_weighted_score = sum(virality_weights[test] * self.likert_scale.max_scale(test) for test in relevant_tests if test in virality_weights)
        # Normalize the virality score by the maximum possible weighted score
        probability_of_going_viral = virality_score / max_weighted_score if max_weighted_score else 0
        return probability_of_going_viral

    @staticmethod
    def kappa(x):
        return 0.5 + 0.5 * np.sign(x - 0.5) * np.sqrt(abs(2 * x - 1))

    def keener_method(self, scores):
        N = len(scores)
        S = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                if i != j:
                    S[i, j] = 1 / scores[i] if scores[i] > 0 else 0

        K = np.zeros((N, N))
        for i in range(N):
            for j in range(N):
                if i != j:
                    K[i, j] = self.kappa((1 + S[i, j]) / (2 + S[i, j] + S[j, i]))
                else:
                    K[i, j] = 0

        eigenvalues, eigenvectors = np.linalg.eig(K)
        max_eigenvalue_index = np.argmax(eigenvalues.real)
        ratings = eigenvectors[:, max_eigenvalue_index].real
        normalized_ratings = ratings / np.sum(ratings)
        
        return normalized_ratings