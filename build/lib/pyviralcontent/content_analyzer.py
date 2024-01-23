from .readability_calculator import ReadabilityCalculator
from .likert_scale import LikertScale
from .visualizer import Visualizer

# This class acts as a high-level interface for content analysis. 
# It utilizes ReadabilityCalculator, LikertScale, and Visualizer to perform a comprehensive readability analysis, including calculating scores,
# determining average scores, calculating virality probability, and visualizing results.
class ContentAnalyzer:
    def __init__(self, text_content, content_type):
        self.text_content = text_content
        self.content_type = content_type
        self.readability_calculator = ReadabilityCalculator()
        self.likert_scale = LikertScale()
        self.visualizer = Visualizer()

    def analyze(self):
        # Calculate readability scores
        df = self.readability_calculator.calculate_scores_by_content_type(self.text_content, self.content_type)
        # Calculate the average score and determine the overall Likert scale and quality
        average_score, overall_likert, overall_quality = self.likert_scale.calculate_average_score(df)
        df.loc[df.shape[0]] = ['OVERALL SCORE', average_score, overall_likert, overall_quality]
        # Calculate the probability of the content going viral
        #viral_probability = self.readability_calculator.calculate_virality_probability(df)
        viral_probability = self.readability_calculator.calculate_virality_probability(df,self.content_type)
        # Visualize the readability scores heatmap
        self.visualizer.plot_scores_heatmap(df, self.content_type)
        return df, viral_probability