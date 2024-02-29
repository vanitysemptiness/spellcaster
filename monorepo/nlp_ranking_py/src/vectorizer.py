from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

# Read text files
file_contents = []
file_paths = []

for root, dirs, files in os.walk("your_directory_path"):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                file_contents.append(content)
                file_paths.append(file_path)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(file_contents)

# Cosine Similarity
search_query = "your search query"
query_vector = vectorizer.transform([search_query])

cosine_similarities = linear_kernel(query_vector, tfidf_matrix).flatten()
document_scores = list(zip(file_paths, cosine_similarities))

# Sort by relevance
sorted_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)

# Print or display the results
for doc_path, score in sorted_documents:
    print(f"File: {doc_path}, Relevance Score: {score}")
