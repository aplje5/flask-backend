from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import speech_recognition as sr

app = Flask(__name__)

def translate_text(text, target_language='en'):
    """Translate text to the specified language."""
    translator = GoogleTranslator(source='auto', target=target_language)
    return translator.translate(text)

def generate_suggestions(user_input, target_language):
    """Generate translation suggestions."""
    languages = {
        'es': 'Spanish', 'fr': 'French', 'de': 'German',
        'zh-CN': 'Chinese', 'ja': 'Japanese', 'ru': 'Russian'
    }
    suggestions = {}
    for lang_code, lang_name in languages.items():
        suggestion = translate_text(user_input, lang_code)
        suggestion_in_original = translate_text(suggestion, target_language)
        suggestions[lang_name] = {'original': suggestion_in_original, 'translated': suggestion}
    return suggestions

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language', 'en')

    translated = translate_text(text, target_language)
    suggestions = generate_suggestions(text, target_language)

    return jsonify({
        'translated_text': translated,
        'suggestions': suggestions
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
