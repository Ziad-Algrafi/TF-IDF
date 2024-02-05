import numpy as np

# Define documents
documents = ["Vaccination Application", "Covid Vaccination Center", "Health of Pilgrims", "Certificate of Vaccination"]

# Define the dictionary mapping terms to indices
dictionary = {"application": 0, "vaccination": 1, "covid": 2, "pilgrims": 3, "health": 4, "certificate": 5, "center": 6}

# Define TF values for each term in each document
tf_matrix = np.array([
    [0.5, 0.5, 0, 0, 0, 0, 0],
    [0, 0.3, 0.3, 0, 0, 0, 0.3],
    [0, 0, 0, 0.3, 0.3, 0, 0],
    [0, 0.3, 0, 0, 0, 0.3, 0]
])

# Define IDF values for each term in the entire document collection
idf_vector = np.array([2, 0.4, 2, 2, 2, 2, 2])

# Calculate the Euclidean norm (magnitude) for each document vector
tfidf_matrix = tf_matrix * idf_vector

# Calculate the Euclidean norm (magnitude) for each document vector
weights = np.sqrt(np.sum(np.square(tfidf_matrix), axis=1))

# Normalize each document vector by dividing by its corresponding weight
normalized_matrix = tfidf_matrix / weights[:, np.newaxis]

# Define the query vector for the given query
query = np.array([0, 0.2, 1, 0, 0, 0, 0])

# Normalize the query vector to have a unit Euclidean norm
query_norm = query / np.linalg.norm(query)

# Compute the cosine similarity between each document and the normalized query vector
dot_product = np.dot(normalized_matrix, query_norm)
query_norm_magnitude = np.linalg.norm(query_norm)
matrix_magnitudes = np.linalg.norm(normalized_matrix, axis=1)
cosine_similarity_formula = dot_product / (query_norm_magnitude * matrix_magnitudes)

# Rank documents in descending order based on cosine similarity values
ranking_formula = np.argsort(cosine_similarity_formula)[::-1]

# Display the ranking of documents along with their cosine similarity scores and text
print("Ranking of Documents:")
for rank, doc_index in enumerate(ranking_formula, 1):
    print(f"Rank {rank}: Document {doc_index + 1} - Cosine Similarity: {cosine_similarity_formula[doc_index]:.5f}")
    print("  Document Text:", documents[doc_index])
    print("  Dictionary:")
    for term, index in dictionary.items():
        print(f"    {term}: {tf_matrix[doc_index, index]}")
    print()

# Print the final statement
print("The documents in decreasing order of ranks are:", ", ".join([f"D{doc + 1}" for doc in ranking_formula]))
