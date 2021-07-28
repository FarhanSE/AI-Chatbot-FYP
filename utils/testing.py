import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import json
import pickle
import numpy as np
nltk.download('punkt')
import random


lemma = WordNetLemmatizer()
intents = json.loads(open(r"C:\Users\Muhammad Farhan\Desktop\FYP\ChatBox\utils\dataset.json" , encoding="utf-8").read())
words = pickle.load(open(r"C:\Users\Muhammad Farhan\Desktop\FYP\ChatBox\utils\words.pkl", "rb"))
classes = pickle.load(open(r"C:\Users\Muhammad Farhan\Desktop\FYP\ChatBox\utils\classes.pkl", "rb"))
model = load_model(r'C:\Users\Muhammad Farhan\Desktop\FYP\ChatBox\utils\chatbot_model.model')

def cleanUpSentences(sentence):
    sentence_word = nltk.word_tokenize(sentence)
    sentence_word = [lemma.lemmatize(word) for word in sentence_word]
    return sentence_word

def bag_of_words(sentence):
    sentence_word = cleanUpSentences(sentence)
    bag = [0]*len(words)
    for w in sentence_word:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    error = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > error]
    results.sort(key=lambda x: [1], reverse=True)
    return_list = []
    for r in results:
        return_list.append( {'intents': classes[r[0]], 'probability': str(r[1])})
    return return_list

def det_responses(ints, intents):
    tag = ints[0]['intents']
    list_of_intents = intents['intents']
    for i in list_of_intents:
        if i['intent'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# while True:
#     print("Type Here")
#     message  = input("")
#     ints = predict(message)
#     res = det_responses(ints, intents)
#     print ("Chatbot:  ",res)