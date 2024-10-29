import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
from datetime import datetime 
import webbrowser

def get_time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    return formatted_time
def text_to_speech(text,text_lang):
    # Initialize gTTS with the text to convert
    speech = gTTS(text, lang = text_lang)
    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    playsound(speech_file)


def speech_to_text(lang):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source :
        audio =  recognizer.listen(source)
    text = "" 
    try:
        text = recognizer.recognize_google(audio ,language = lang)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")

    return text


def main():

    text_to_speech("Hello I am Alexa , What language do you want Arabic or English ?",'en')
    speech_lang_response = speech_to_text('en')
    while True:
        if 'Arabic' in speech_lang_response:
                text_to_speech("كيف يمكنني مساعدتك؟",'ar')
                speech_text = speech_to_text('ar')

                if 'الكود' in speech_text or 'كود' in speech_text:
                    text_to_speech("جاري فتح الكود",'ar')
                    os.system("code .")
                    print("جاري فتح الكود")

                elif 'الوقت' in speech_text or 'التوقيت' in speech_text or 'الساعه' in speech_text:
                    current_time = get_time()
                    text_to_speech("الوقت اﻷن" + current_time ,'ar')
                    print(f'التوقيت الأن : {current_time}')

                elif 'جوجل' in speech_text or 'الجوجل' in speech_text:
                    print("جاري فتح جوجل")
                    text_to_speech("جاري فتح جوجل",'ar')
                    webbrowser.open("https://www.google.com")
                elif 'شكرا' in speech_text or 'انتهيت' in speech_text: 
                    print("أتمني لك يوما سعيدا")
                    text_to_speech("أتمني لك يوما سعيدا",'ar')
                    break
                else:
                    print('لا أستطيع أن افهم هذا اﻷمر')
                    text_to_speech('لا أستطيع أن افهم هذا اﻷمر','ar')


        elif 'English' in speech_lang_response: 
                text_to_speech("How can i help you ?",'en')
                speech_text = speech_to_text('en')
                
                if 'code' in speech_text or 'vscode' in speech_text:
                    print('Opening the vs code ...')
                    text_to_speech('Opening vs code','en')
                    os.system("code .")
                
                elif 'time' in speech_text or 'timing' in speech_text:
                    print('Getting Time ... ')
                    current_time = get_time()
                    text_to_speech("The current time is " + current_time ,'en')
                    print("The current time is " + current_time)
                
                elif 'google' in speech_text or 'Google' in speech_text:
                    print('Opening Google ...')
                    text_to_speech('Opening Google ...','en')
                    webbrowser.open("https://www.google.com")

                elif 'exit' in speech_text or 'thank you' in speech_text:
                    print('Exiting ...')
                    text_to_speech('Exiting the system , Have a good day','en')
                    break
                
                else:
                    print('I can not understand this command')
                    text_to_speech('I can not understand this command','en')

if __name__ == "__main__":
    main()