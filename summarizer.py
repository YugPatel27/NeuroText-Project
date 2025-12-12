import tkinter as tk
import re, heapq, time

# Simple Text Summarization Logic
def summarize_text(text):
    stopwords = set("a an the and are as at be by for from has he in is it its of on that this to was were will with".split())
    clean = re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\.!? ]', '', text))
    sentences = re.split(r'(?<=[.!?]) +', clean)
    words = re.findall(r'\b[a-zA-Z]+\b', clean.lower())

    if not sentences or not words:
        return "⚠️ Not enough valid text to summarize."

    freq = {}
    for w in words:
        if w not in stopwords:
            freq[w] = freq.get(w, 0) + 1

    scores = {}
    for s in sentences:
        ws = re.findall(r'\b[a-zA-Z]+\b', s.lower())
        if not ws: 
            continue
        scores[s] = sum(freq.get(w, 0) for w in ws) / len(ws)

    top_sentences = heapq.nlargest(max(1, len(sentences)//3), scores, key=scores.get)
    return ' '.join(top_sentences)

# GUI Design
class NeuroTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 NeuroText Summarizer")
        self.root.geometry("900x700")
        self.root.configure(bg="#f2f8ff")  # light sky tone

        # Header Frame
        header = tk.Frame(root, bg="#5dade2", height=80)
        header.pack(fill="x")
        tk.Label(header, text="🧠 NEUROTEXT", bg="#5dade2",
                 font=("Helvetica", 22, "bold"), fg="white").pack(pady=10)
        tk.Label(header, text="Simple & Smart Text Summarization Tool",
                 bg="#5dade2", font=("Arial", 12, "italic"), fg="white").pack()

        # Input Frame
        input_frame = tk.Frame(root, bg="white", bd=2)
        input_frame.place(x=30, y=120, width=840, height=250)
        tk.Label(input_frame, text="Enter Your Text Below :",
                 bg="white", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

        self.text_input = tk.Text(input_frame, font=("Consolas", 11), height=10, bd=0)
        self.text_input.pack(fill="both", expand=True, padx=10, pady=5)

        # Button Frame
        button_frame = tk.Frame(root, bg="#f2f8ff")
        button_frame.place(x=0, y=390, width=900)
        tk.Button(button_frame, text=" Generate Summary ", bg="#5dade2",
                  font=("Arial", 12, "bold"), fg="white",
                  padx=20, pady=10, command=self.generate_summary).pack(pady=5)

        # Output Frame
        output_frame = tk.Frame(root, bg="white", bd=2)
        output_frame.place(x=30, y=470, width=840, height=200)
        tk.Label(output_frame, text="Generated Summary : ",
                 bg="white", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

        self.text_output = tk.Text(output_frame, font=("Consolas", 11),
                                   height=8, bd=0)
        self.text_output.pack(fill="both", expand=True, padx=10, pady=5)

    # Generate Summary Function
    def generate_summary(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, "Please enter text to summarize.")
            return

        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, "Processing your text...")
        self.root.update()
        time.sleep(0.3)

        summary = summarize_text(text)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, summary)

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = NeuroTextApp(root)
    root.mainloop()