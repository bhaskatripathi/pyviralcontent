#from pyviralcontent import ContentAnalyzer
from pyviralcontent.content_analyzer import ContentAnalyzer

def main():
    # Mapping of content type numbers to content type names
    content_type_map = {
        0: 'scientific',
        1: 'blog',
        2: 'video',
        3: 'technical',
        4: 'fictional',
        5: 'legal',
        6: 'educational',
        7: 'news',
        8: 'advertising',
        9: 'social_media'
    }

    # Prompt user for a content type number
    content_type_number = int(input("Enter a number for the content type (0 for scientific, 1 for blog, ..., 9 for social_media): "))
    
    # Get the content type name from the content_type_map
    content_type_name = content_type_map.get(content_type_number)
    
    if content_type_name is None:
        print("Invalid content type number.")
    else:
        # User to input the text content
        text_content = input("Enter the text content for analysis:\n")
        
        # Create instance of ContentAnalyzer with the chosen content type
        analyzer = ContentAnalyzer(text_content, content_type_name)

        # Perform the analysis
        df, viral_probability = analyzer.analyze()

        # Print the results
        print(f"Readability Scores Summary for {content_type_name.capitalize()} Content:")
        print(df)
        print(f"The probability of the content going viral is: {viral_probability * 100:.2f}%")

if __name__ == "__main__":
    main()
