# 📝 Text Analysis Tool  

An **all-in-one NLP-based text analysis tool** that helps users quickly understand, evaluate, and compare text using modern AI techniques.  

---

## 🚀 Features  

- **Summarization (Gemini API):** Automatically condenses large texts into clear, concise summaries.  
- **Tokenization Comparison (GPT vs BERT):** Shows how different models break text into tokens.  
- **Text Statistics:** Word count, sentence count, average sentence length, unique words, etc.  
- **Sentiment Analysis:** Detects the emotional tone of text (positive, negative, neutral).  
- **Readability Metrics (Flesch Reading Ease, etc.):** Measures how easy or difficult a text is to read.  

---

## 🎯 Problem It Solves  

Working with **long, complex, or unstructured text** is time-consuming and inefficient.  
This tool provides a **single platform** to:  
- Summarize and analyze large documents.  
- Understand readability and emotional tone.  
- Compare tokenization between GPT & BERT for educational/research purposes.  
- Save time by avoiding multiple separate tools.  

---

## 🛠 Tech Stack  

- **Python**  
- **Google Gemini API** – for summarization  
- **Hugging Face Transformers** – GPT/BERT tokenization  
- **NLTK / TextStat** – statistics & readability  
- **Streamlit** – user-friendly interface (if UI used)  

---

## 📂 Project Structure  

````
TEXT_ANALYSIS_TOOL/
├── README.md # Project documentation
├── main.py # Main entry point for the app
├── requirements.txt # Python dependencies
├── config.py # API keys and configuration
├── utils/ # Helper functions and modules
│ ├── init.py
│ ├── llm_helpers.py # Gemini + summarization helpers
│ ├── tokenizer_helpers.py # GPT/BERT tokenization utilities
│ └── advanced_features.py # Sentiment & readability functions
├── data/
│ ├── sample_texts/ # Example input texts
└── docs/
└── usage_examples.md # Documentation with usage examples
````

---

## ⚡ Installation  

1. Clone this repo:  
   ```bash
   git clone https://github.com/your-username/TEXT_ANALYSIS_TOOL.git
   cd TEXT_ANALYSIS_TOOL

2. Create a virtual environment (recommended):
  python -m venv venv
  source venv/bin/activate   # On Linux/Mac
  venv\Scripts\activate      # On Windows

  3. Install dependencies:
  pip install -r requirements.txt

4. Add your API keys in config.py.
  ```bash

### 📌 Example Use Cases

- Students & Researchers → Summarize academic papers & compare readability.

- Writers & Bloggers → Check readability and tone before publishing.

- Businesses → Quickly analyze customer feedback and reviews.

- Developers → Learn how GPT and BERT process text differently.

🔮 Future Improvements

- Add more readability formulas.

- Multi-language support.

- Export results as PDF/CSV reports.
