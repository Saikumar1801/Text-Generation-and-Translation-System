# 🧠 Text Generation and Translation System

A web-based content generation system that leverages OpenAI’s GPT models to automate the creation and translation of high-quality, context-aware content for blogs, social media, and marketing material.

---

![front](https://github.com/user-attachments/assets/b8825321-3aef-4e01-8f3d-c530db171cc5)


## 📝 Summary
This project allows users to input:
- A topic
- Keywords
- Tone
- Style

It generates structured content using OpenAI GPT, with:
- Title
- Subtitle
- Bullet points
- Summary

The system supports **multilingual output** via the **Google Translate API** (`googletrans`), and allows users to **download both original and translated content** in `.txt` or `.pdf` formats.
This project showcases:
- Natural Language Processing (NLP)
- Prompt engineering
- Web integration (Flask, FPDF)
- 

---

## 🔧 Tools & Technologies

- **Python**
- **OpenAI GPT** (`gpt-3.5-turbo`, or `text-davinci-003`)
- **googletrans** – Google Translate API (Python client)
- **Flask** – Lightweight web framework
- **FPDF** – PDF generation in Python
- **DejaVuSans.ttf** – Unicode-compatible font for multilingual PDF export

---

## 📁 Project Structure
Text-Generation-and-Translation-System/
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── fonts/
│   └── DejaVuSans.ttf
├── LICENSE
└── .gitignore


## 🔑 Setup
1. Clone this repository:
    ```bash
    git clone https://github.com/Saikumar1801/Text-Generation-and-Translation-System.git
    cd Text-Generation-and-Translation-System
    ```

2. Add your OpenAI API key to `app.py`:
    ```python
    openai.api_key = "your-api-key-here"
    ```

3. (Optional) Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

## ▶️ To Run the Project
```bash
python app.py
```
Visit http://127.0.0.1:5000 in your browser.


## ⚠️ Python Version Compatibility
❌ If you're using Python 3.13, you may see errors because the cgi module was removed and some dependencies (like googletrans) still require it.
✅ Recommended: Use Python 3.10 or 3.11
Install Python 3.10 or 3.11 (https://www.python.org/downloads/)
Then run:

## 👉 How to switch:
On Windows
```bash
py -3.11 -m venv venv
venv\\Scripts\\activate   # On Windows
pip install -r requirements.txt
python app.py
```
On macOS/Linux
```bash
py -3.11 -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
python app.py
```

## 🐳 Run with Docker
1. Build the image:
```bash
docker build -t Text-Generation-and-Translation-System
```
2. Run the container:

```bash
docker run -p 5000:5000 Text-Generation-and-Translation-System
```

## 🌍 Languages Supported
Translate content into:
-Spanish
-French
-German
-Hindi
-Chinese

## Screenshot
![1](https://github.com/user-attachments/assets/e2a6e279-23d8-4ef2-b1d8-9cb3e684a633)
![2](https://github.com/user-attachments/assets/684c7a74-ec88-42a6-b498-e7b8446704a3)
![3](https://github.com/user-attachments/assets/50446ecf-6553-4eb4-88ab-4ab6c6821be5)
![4](https://github.com/user-attachments/assets/bd52b886-f44a-4ae6-8c99-49be25edf24f)
![5](https://github.com/user-attachments/assets/20b9ea9e-136e-4f0a-923f-6a3f63d95052)


## 📄 Download Options
You can export your content in:
-Plain text (.txt)
-Portable Document Format (.pdf) – with Unicode font support


## 📬 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

## 📄 License
MIT License – see LICENSE file for full text.

## 🙌 Acknowledgements
- OpenAI API
- Google Translate
- FPDF for Python
- DejaVu Fonts
