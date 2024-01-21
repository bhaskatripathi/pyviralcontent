# PyViralContent

`pyviralcontent` is a Python package designed to assess the readability of various types of content and predict their potential to go viral. It employs multiple readability tests and translates numerical scores into qualitative descriptors based on the Likert scale. This tool is useful for optimizing content for clarity and engagement across various domains.

## Installation

```bash
pip install pyviralcontent
```

## Usage

```python
from pyviralcontent import ContentAnalyzer

# Define the type of content and the actual content
content_type = 'educational'  # options: 'scientific', 'blog', 'video', 'technical', 'fictional', 'legal', 'educational', 'news','advertising', 'social_media'. 
text_content = "Your text content here."

# Create an instance of ContentAnalyzer
analyzer = ContentAnalyzer(text_content, content_type)

# Perform the analysis
df, viral_probability = analyzer.analyze()

# Print the results
print(f"Readability Scores Summary for {content_type.capitalize()} Content:")
print(df)
print(f"The probability of the content going viral is: {viral_probability * 100:.2f}%")
```

## Features

- Multiple readability tests for different content types.
- Qualitative descriptors based on the Likert scale.
- Estimation of content's virality potential.
- Supported content types include: scientific, blog, video, technical, fictional, legal, educational, news, advertising, social_media.

## Contributing

Contributions to `pyviralcontent` are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Bhaskar Tripathi - bhaskar.tripathi@gmail.com
GitHub: https://github.com/bhaskatripathi/pyviralcontent
