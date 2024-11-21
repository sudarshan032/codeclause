# **Plagiarism Checker - Python Programs**

This repository contains Python programs that implement a simple plagiarism checker. The plagiarism checker can check for similarities between two texts, between a text and a text file, or between two text files. Additionally, it includes a Tkinter-based graphical user interface (GUI) to make it user-friendly.

## **Programs Overview**

`plagiarism_checker.py`
This Python program implements a plagiarism checker that compares two input texts for similarity using the cosine similarity method. It takes two strings of text as input and calculates the similarity score between them. The similarity score is then compared against a default threshold of 0.85 to determine if potential plagiarism exists.

`plagiarism_checker_with_files.py`
This Python program extends the plagiarism checker to accept input from text files. It takes the file paths of two text files as input, reads the contents of the files, and calculates the similarity score between them using the same cosine similarity method. The plagiarism detection result is displayed based on the default threshold of 0.85.

## **Tkinter GUI**

`plagiarism_checker_gui.py`
This Python program utilizes Tkinter to create a GUI for the plagiarism checker. The graphical interface allows the user to select two text files using file dialogs. When the "Check Plagiarism" button is clicked, the program reads the contents of the selected files and displays the similarity result in the GUI. The threshold for plagiarism detection remains at 0.85 (85%), and the result will indicate whether potential plagiarism is detected or not.

## **Dependencies**

The programs require the following dependencies:

* `Python 3.x`
* `NLTK `(Natural Language Toolkit) - Used for text preprocessing and stopwords removal.

You can install NLTK using pip:

`pip install nltk`

## **Usage**

#### **Program Execution**

To use the plagiarism checker programs without the GUI, you can simply run the Python scripts and follow the prompts for input text or file paths.

##### **Note**

Please note that these programs are meant for educational and basic plagiarism detection purposes. For more robust and comprehensive plagiarism detection, consider using specialized tools and algorithms designed for plagiarism detection in real-world scenarios.

Feel free to use, modify, and improve these Python programs for your needs. If you have any questions or suggestions, feel free to reach out. Happy coding!