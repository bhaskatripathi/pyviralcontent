import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# This class provides visualization functionality. It can plot a heatmap of readability scores for each test, providing a visual representation of the analysis results.
class Visualizer:
    @staticmethod
    def plot_scores_heatmap(df, content_type):
        fig, ax = plt.subplots(figsize=(8, 1), dpi=300)
        heatmap_data = pd.pivot_table(data=df, values='Score', index=['Test'], aggfunc=np.mean)
        sns.heatmap(heatmap_data, annot=True, fmt=".1f", linewidths=.5, ax=ax)
        plt.title(f'Readability Scores for {content_type.capitalize()} Content')
        plt.show()