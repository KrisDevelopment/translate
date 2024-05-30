from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

translator = Translator()

def convert_lang_code_to_name(code):
    # e.g. 'en' -> 'english', 'es' -> 'spanish'
    r = LANGUAGES.get(code, code)
    assert r is not None, f"Invalid language code: {code}"
    return r

@app.route('/translate', methods=['POST', 'GET'])
def translate_text():
    
    if request.is_json:
        data = request.get_json()
        text = data.get('text')
        src_lang = data.get('src_lang')
        dest_lang = data.get('dest_lang')

        # convert short language codes to full language names
        src_lang = convert_lang_code_to_name(src_lang)
        dest_lang = convert_lang_code_to_name(dest_lang)
        
        if not text or not src_lang or not dest_lang:
            return jsonify({'error': 'Missing required fields'}), 430

        if src_lang not in LANGUAGES.values() or dest_lang not in LANGUAGES.values():
            return jsonify({'error': 'Invalid language code'}), 431
        
        try:
            translated = translator.translate(text, src=src_lang, dest=dest_lang)
            return jsonify({
                'translated_text': translated.text,
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
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

@app.route('/', methods=['GET', 'POST'])
def index():
    return translate_text()
    

app.run(debug=True, host="0.0.0.0", port=80)