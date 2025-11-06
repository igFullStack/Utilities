import spacy
from langdetect import detect, LangDetectException
import json

nlp = spacy.load("en_core_web_sm")

def is_english(text):
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False

def text_to_json(text, output_path):
    doc = nlp(text)
    
    english_sentences = []
    for sent in doc.sents:
        sentence = sent.text.strip()
        if sentence and is_english(sentence):
            english_sentences.append({"text": sentence})
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(english_sentences, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        text = f.read()
    text_to_json(text, "output.json")
    print(f"Saved {len(json.load(open('output.json', encoding='utf-8')))} english sentences in output.json")