# Research Paper Summarizer

This is a simple web application that allows users to upload research papers (PDFs) and generate concise summaries using Google's Gemini AI model. Users can also ask questions related to the uploaded document.

## Features
- Upload a research paper (PDF format)
- Generate an AI-powered summary
- Ask questions based on the uploaded document
- User-friendly Streamlit interface

## Installation & Setup
### Prerequisites
Ensure you have Python installed on your system.

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/Mrnobody2004/research-paper-summarizer.git
   cd research-paper-summarizer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up your Google Generative AI API key as an environment variable:
   ```sh
   export GENAI_API_KEY='your_api_key_here'
   ```
4. Run the application:
   ```sh
   streamlit run summary_bot.py
   ```

## Usage
1. Open the app in your browser.
2. Upload a research paper in PDF format.
3. Click the **Summarize** button to generate a summary.
4. Enter a query in the text box and click **Ask Query** to get answers from the document.
5. 

## Contributing
Pull requests are welcome! Feel free to open an issue if you find bugs or have feature requests.

---
Made with ❤️ by [@Mrnobody2004](https://github.com/Mrnobody2004)

