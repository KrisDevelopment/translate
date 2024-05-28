from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    src_lang = data.get('src_lang')
    dest_lang = data.get('dest_lang')
    
    if not text or not src_lang or not dest_lang:
        return jsonify({'error': 'Missing required fields'}), 400

    if src_lang not in LANGUAGES.values() or dest_lang not in LANGUAGES.values():
        return jsonify({'error': 'Invalid language code'}), 400
    
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return jsonify({
            'translated_text': translated.text,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    lang_vals = LANGUAGES.values()
    return """
    <h1>Translation Service</h1>
    <p>Use the /translate endpoint to translate text from one language to another.</p>
    <p>Send a POST request with JSON body containing 'text', 'src_lang', and 'dest_lang'.</p>
    <p>Example:</p>
    <pre>{
    "text": "Hello, world!",
    "src_lang": "en",
    "dest_lang": "es"
    }</pre>
    #EXAMPLE 2:<br>
    curl -X POST http://127.0.0.1:20881/translate \
     -H "Content-Type: application/json" \
     -d '{"text": "Hello, world!", "src_lang": "english", "dest_lang": "bulgarian"}'
     <br>
     ----
     <br><h2>Accepted Language Codes:</h2><br>
    """ + '<br>'.join(lang_vals)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)