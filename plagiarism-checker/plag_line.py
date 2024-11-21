import nltk
from nltk.corpus import stopwords
from collections import Counter
import re
import math

nltk.download("stopwords")


def preprocess_text(text):
    # Remove special characters and digits, convert to lowercase
    text = re.sub(r"[^a-zA-Z]", " ", text).lower()
    return text


def calculate_term_frequency(text):
    # Tokenize the text into words
    words = text.split()

    # Remove common English stop words
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]

    # Count the frequency of each word
    word_frequency = Counter(words)

    return word_frequency


def calculate_cosine_similarity(tf1, tf2):
    # Calculate the dot product of the two term frequency vectors
    dot_product = sum(tf1[word] * tf2[word] for word in tf1 if word in tf2)

    # Calculate the magnitude of each vector
    magnitude_tf1 = math.sqrt(sum(tf1[word] ** 2 for word in tf1))
    magnitude_tf2 = math.sqrt(sum(tf2[word] ** 2 for word in tf2))

    # Calculate the cosine similarity
    cosine_similarity = dot_product / (magnitude_tf1 * magnitude_tf2)

    return cosine_similarity


def plagiarism_checker(text1, text2, threshold=0.8):
    # Preprocess the texts
    text1 = preprocess_text(text1)
    text2 = preprocess_text(text2)

    # Calculate term frequency for both texts
    tf1 = calculate_term_frequency(text1)
    tf2 = calculate_term_frequency(text2)

    # Calculate cosine similarity
    similarity = calculate_cosine_similarity(tf1, tf2)

    if similarity >= threshold:
        return "Similarity Score: {:.2f}% - Potential Plagiarism Detected!".format(similarity * 100)
    else:
        return "Similarity Score: {:.2f}% - No Plagiarism Detected.".format(similarity * 100)


# Example usage:
text1 = "This is a sample text for testing the plagiarism checker."
text2 = "A sample text for testing the plagiarism detection functionality."
result = plagiarism_checker(text1, text2)
print(result)
