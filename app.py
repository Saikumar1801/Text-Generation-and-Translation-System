from flask import Flask, render_template, request, send_file
from fpdf import FPDF
from googletrans import Translator
import openai
import re
import os

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key-here"

def clean_generated_content(raw_content):
    content = re.sub(r"\*\*(.*?)\*\*", r"\1", raw_content)
    content = re.sub(r"(?i)(title|subtitle|summary|bullet points?|main points?)\\s*[:：]", "", content)
    content = re.sub(r"^\\s*(?:[-*•]|\\d+\\.)\\s*", "- ", content, flags=re.MULTILINE)
    content = re.sub(r"\\n{3,}", "\\n\\n", content).strip()
    return content

def generate_structured_content(topic, keywords, tone, style):
    prompt = f"""
Create structured content on the topic "{topic}".
- Use the keyword "{keywords}" at least 10 times.
- Tone: {tone}
- Style: {style}
Include:
1. A title
2. A subtitle
3. Bullet points (at least 5)
4. A summary of the content
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for generating structured content."},
                {"role": "user", "content": prompt}
            ]
        )
        raw_content = response.choices[0].message.content
        return clean_generated_content(raw_content)
    except Exception as e:
        return f"OpenAI error: {e}"

@app.route('/')
def home():
    return render_template('index.html', content=None)

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form.get('topic')
    keywords = request.form.get('keywords')
    tone = request.form.get('tone')
    style = request.form.get('style')

    content = generate_structured_content(topic, keywords, tone, style)
    return render_template('index.html', content=content, original_content=content)

@app.route('/translate', methods=['POST'])
def translate():
    content = request.form.get('content')
    original_content = request.form.get('original_content')
    target_language = request.form.get('language')
    translator = Translator()
    translated = translator.translate(content, dest=target_language)
    return render_template('index.html', content=translated.text, original_content=original_content)

@app.route('/download_txt', methods=['POST'])
def download_txt():
    original = request.form.get('original_content', '')
    translated = request.form.get('translated_content', '')

    txt_filename = "structured_content.txt"
    with open(txt_filename, 'w', encoding='utf-8') as file:
        file.write("Original Content:\n")
        file.write(original + "\n\n")
        if translated:
            file.write("Translated Content:\n")
            file.write(translated)
    return send_file(txt_filename, as_attachment=True)

@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    original = request.form.get('original_content', '')
    translated = request.form.get('translated_content', '')

    pdf = FPDF()
    pdf.add_page()

    font_path = os.path.join("fonts", "DejaVuSans.ttf")
    if not os.path.exists(font_path):
        return "Error: fonts/DejaVuSans.ttf is missing. Please download it and place in the fonts/ folder."

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", "", 12)

    try:
        pdf.multi_cell(0, 10, "Original Content:\n" + original)
        if translated:
            pdf.ln(10)
            pdf.multi_cell(0, 10, "Translated Content:\n" + translated)
    except Exception as e:
        return f"PDF generation failed: {e}"

    pdf_filename = "structured_content.pdf"
    try:
        pdf.output(pdf_filename)
    except Exception as e:
        return f"Failed to write PDF: {e}"

    return send_file(pdf_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
