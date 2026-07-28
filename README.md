# NeuroText Summarizer

NeuroText Summarizer is a lightweight desktop application designed to help users quickly generate a concise summary from any block of text. Rather than requiring an internet connection, cloud API, or heavy machine learning model, the application runs entirely on the user's local machine. It is built using Python's Tkinter toolkit, which provides the graphical user interface, and it relies on a frequency-based text summarization algorithm to identify and extract the most meaningful sentences from the input text. The result is a fast, private, and dependency-free summarization tool suitable for students, writers, researchers, and professionals who need quick summaries without installing complex software.

# Key Features

- **Easy-to-Use Interface**  
  The application features a clean and minimal graphical interface built with Tkinter. Users are presented with a straightforward input area, a single action button, and a clearly labeled output section, making the tool approachable even for users with no technical background.

- **Fast and Efficient Processing**  
  Because the summarization method is based on simple statistical word-frequency calculations rather than large neural network models, the application processes text almost instantly. There is no need to download or load large model files, which keeps memory usage low and startup time minimal.

- **No External Dependencies or Programs Required**  
  The application does not require an internet connection, external API calls, or third-party summarization services. All processing happens locally within the Python environment, ensuring that user data never leaves their computer.

- **Automatic Key Sentence Extraction**  
  The application automatically analyzes the entire input text and determines which sentences carry the most meaningful or "important" information, based on word repetition and relevance. Users do not need to manually highlight or select important sections themselves.

- **Real-Time Summary Generation**  
  Summaries are generated immediately after the user clicks the "Generate Summary" button, with no noticeable delay, allowing for quick iteration if the user wants to try different input text.

# How the Application Works

The summarization process follows a clear, step-by-step pipeline:

1. **Text Cleaning**  
   When text is first submitted, the application removes any non-printable characters (such as hidden formatting symbols or encoding artifacts) and eliminates excess whitespace, including extra spaces, tabs, and unnecessary line breaks. This ensures the text is standardized and ready for accurate processing.

2. **Sentence and Word Splitting (Tokenization)**  
   The cleaned text is broken down into individual sentences, and each sentence is further broken down into individual words. This two-level breakdown is necessary because word frequency is calculated at the word level, while summary selection happens at the sentence level.

3. **Stop Word Removal**  
   Common English words that carry little meaningful content on their own—such as "the," "is," "and," "of," and "to"—are filtered out using a predefined list of stop words. Removing these words ensures that the frequency analysis focuses only on words that meaningfully contribute to the text's topic.

4. **Word Frequency Calculation**  
   After stop words are removed, the application calculates how often each remaining word appears throughout the entire input text. Words that appear more frequently are treated as more central or important to the overall meaning of the text.

5. **Sentence Scoring**  
   Each sentence is assigned a numerical score based on the combined frequency values of the significant words it contains. Sentences that contain a higher number of frequently occurring, meaningful words receive higher scores, indicating they are more likely to represent key ideas in the text.

6. **Summary Generation**  
   The sentences with the highest scores are selected and combined, generally in their original order of appearance, to form the final summary. This ensures the summary remains coherent and reflects the natural flow of the original text while significantly reducing its length.

# User Instructions

1. Launch the NeuroText Summarizer application on your desktop.
2. In the input text box, either type your text manually or copy and paste an existing block of text that you would like to summarize.
3. Once your text has been entered, click the **"Generate Summary"** button.
4. The application will process the text instantly and display the generated summary in the output section located below the input box.
5. Review the summary, and if desired, repeat the process with new or edited text to generate additional summaries.

# Future Improvements

1. **File Upload Support** — Add the ability to upload and summarize text directly from TXT and PDF files, rather than requiring manual copy-pasting.
2. **Advanced NLP Integration** — Incorporate modern Natural Language Processing (NLP) models to improve the contextual accuracy and readability of generated summaries beyond simple frequency-based scoring.
3. **Custom Summary Length** — Allow users to specify how long or short they would like their summary to be, offering more control over the level of detail retained.
4. **Export and Copy Functionality** — Provide a built-in option to export the generated summary to a file or copy it directly to the clipboard for easy use elsewhere.
5. **Image and PDF Summarization** — Expand the application's capabilities to support summarizing text extracted from images (via OCR) and PDF documents directly within the interface.
<img width="894" height="726" alt="Capture d&#39;écran 2026-03-26 175251" src="https://github.com/user-attachments/assets/4d6dc5c6-f8de-4516-bb7f-26daedd0a389" />
