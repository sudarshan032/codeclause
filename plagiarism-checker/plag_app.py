#libraries
import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.corpus import stopwords
from collections import Counter
import re
import math

# Download stopwords data from NLTK
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


def plagiarism_checker(file1_path, file2_path, threshold=0.85):
    # Read the content from the files
    with open(file1_path, 'r', encoding='utf-8') as file1:
        text1 = file1.read()
    with open(file2_path, 'r', encoding='utf-8') as file2:
        text2 = file2.read()

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


def browse_file(entry):
    # Function to open a file dialog and get the selected file path
    filepath = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)


def check_plagiarism():
    # Function to check plagiarism between the selected files
    file1_path = entry_file1.get()
    file2_path = entry_file2.get()

    if file1_path and file2_path:
        result = plagiarism_checker(file1_path, file2_path)
        result_label.config(text=result)
    else:
        result_label.config(text="Please select both files.")


# Create the Tkinter GUI
root = tk.Tk()
root.title("Plagiarism Checker")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_file1 = tk.Label(frame, text="File 1:")
label_file1.grid(row=0, column=0, padx=5, pady=5)

entry_file1 = tk.Entry(frame, width=40)
entry_file1.grid(row=0, column=1, padx=5, pady=5)

button_browse_file1 = tk.Button(frame, text="Browse", command=lambda: browse_file(entry_file1))
button_browse_file1.grid(row=0, column=2, padx=5, pady=5)

label_file2 = tk.Label(frame, text="File 2:")
label_file2.grid(row=1, column=0, padx=5, pady=5)

entry_file2 = tk.Entry(frame, width=40)
entry_file2.grid(row=1, column=1, padx=5, pady=5)

button_browse_file2 = tk.Button(frame, text="Browse", command=lambda: browse_file(entry_file2))
button_browse_file2.grid(row=1, column=2, padx=5, pady=5)

button_check_plagiarism = tk.Button(frame, text="Check Plagiarism", command=check_plagiarism)
button_check_plagiarism.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

result_label = tk.Label(frame, text="", wraplength=400)
result_label.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

root.mainloop()
