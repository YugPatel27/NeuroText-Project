# NeuroText Summarizer
This desktop application is a simple way to create a summary from existing text. The application is built with the Python Tkinter toolkit and uses a frequency-based algorithm to generate a brief, meaningful summary.

# Key Features
This application has an easy-to-use interface, is fast and processes text efficiently without requiring any outside programs, automatically extracts key sentences, and generates summaries in real-time.

# How the Application Works
After an input of text is received, the application cleans the input of any non-printable characters and excess whitespace before splitting the input into individual sentences and words. The application uses a list of common stop words to discard those words from further processing. It then computes the word frequency for the remaining words in the input. Each sentence is assigned a score based on how important (i.e., high frequency) the words in that sentence are, and the highest scoring sentences are chosen to be included in the final summary.

# User Instructions
After launching the application, the user must copy and paste or type his/her text into the input text box, and once completed, click the "Generate Summary" button to instantly see the Summarized text in the output section below.

# Future Improvements
1. Add ability to upload a text file (TXT/PDF) for your summary.
2. Use advanced NLP (Natural Language Processing) models to improve the accuracy of the Summary.
3. Allow the User to specify how long or short they want the Summary to be.
4. Provide an export or copy option for the new Summary.
5. Image and PDF summarization.


<img width="894" height="726" alt="Capture d&#39;écran 2026-03-26 175251" src="https://github.com/user-attachments/assets/4d6dc5c6-f8de-4516-bb7f-26daedd0a389" />
