import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


# Download necessary NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# Define a function to identify important words using TF-IDF
def identify_important_words_tfidf(text):
  """
  Identifies potentially important words in a text using TF-IDF from NLTK.

  Args:
      text: The input text string.

  Returns:
      A list of identified important words.
  """
  sentences = nltk.sent_tokenize(text)
  words = [nltk.word_tokenize(sentence) for sentence in sentences]

  # Calculate TF-IDF scores
  tfidf = TfidfVectorizer().fit_transform(words)
  feature_names = tfidf.get_feature_names_out()

  # Get top words based on TF-IDF score
  top_indices = np.argsort(tfidf.toarray().ravel())[::-1][:10]  # Get top 10 words
  important_words = [feature_names[i] for i in top_indices]

  return important_words