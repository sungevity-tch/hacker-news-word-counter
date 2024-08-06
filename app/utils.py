import nltk
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def count_n_most_common_words(text, n=10):

    # Tokenize words
    words = word_tokenize(text)

    # Convert to lower case and remove punctuation
    words = [word.lower() for word in words if word.isalpha()]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Count frequency of each word
    word_counts = Counter(words)
    
    # Get n most common words
    most_common_words = word_counts.most_common(n)
    
    return most_common_words
