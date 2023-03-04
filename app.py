import speech_recognition as sr
import pyttsx3
import json
import re
import pyaudio
from num2words import num2words
import streamlit as st

if st.button('Start'):
  r = sr.Recognizer()
  doneOrder = "ThankYou for Ordering, Your order is being prepared"
  mic = sr.Microphone(device_index=0)
  number_dict = {
      "zero": 0,
      "one": 1,
      "two": 2,
      "three": 3,
      "four": 4,
      "five": 5,
      "six": 6,
      "seven": 7,
      "eight": 8,
      "nine": 9,
      "ten": 10,
      "eleven": 11,
      "twelve": 12,
      "thirteen": 13,
      "fourteen": 14,
      "fifteen": 15,
      "sixteen": 16,
      "seventeen": 17,
      "eighteen": 18,
      "nineteen": 19,
      "twenty": 20,
      "thirty": 30,
      "forty": 40,
      "fifty": 50,
      "sixty": 60,
      "seventy": 70,
      "eighty": 80,
      "ninety": 90,
      "hundred": 100
      }
  menu = ['pizza','burger','burgers','pasta']
  order = []
  def convert_words_to_numbers(text):
      words = text.split()
      numbers = []
      for word in words:
          if word in number_dict:
              numbers.append(number_dict[word])
          else:
              try:
                  numbers.append(int(word))
              except ValueError:
                  pass
      return sum(numbers)

  def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

  with mic as source:
      SpeakText("Welcome to Marsbristo! What would you like to order")
      audio = r.record(source, duration = 4)

      text = r.recognize_google(audio, language="en-EN")
      text = text.lower()
      words = text.split()

      for word in words:
          if word in menu:
              order.append(word)


      numbers = [convert_words_to_numbers(word) for word in text.split() if word in number_dict or word.isnumeric()]
      print("Quantity is :",numbers)
      SpeakText(doneOrder)

      #print(text)
  with mic as source:
      SpeakText("How many people are in your party")
      audio2 = r.record(source,duration = 3)
      text = r.recognize_google(audio, language="en-EN")
      text = text.lower()
      words = text.split()

      people = [convert_words_to_numbers(word) for word in text.split() if word in number_dict or word.isnumeric()]

      print("Total people are: ",people)
      data = {'food_item':order,'Quantity':numbers,'Active_users':people}
      with open('output.json', 'w') as f:
          json.dump(data, f)
