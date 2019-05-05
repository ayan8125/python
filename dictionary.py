import pyttsx3
import speech_recognition as sr
dicts = {}
new_dict = {}
"""my  file   contains 6000+ words with there meaning will open it. """
"""As we know using readlines funtion return a list of each line as new member of a list,so we  will used that property"""
with open(file= 'meanings.txt',mode= 'r') as f:
    lists= f.readlines()
    lists.pop(0)
"""there was a '\n' character at index one so we poped  it from the list"""
for i in range(0, len(lists)-1, 2):
        dicts[lists[i]] = lists[i+1]
#print(dicts)
#print(len(dicts))
for i, j in dicts.items():
    i = i.replace('\n','')
    j = j.replace('\n','')
    new_dict[i] = j
"""for every value  there was a '\n' character so we replaced it with space  by str.replace method""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def listen():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print('say which word meaning you want?')
        a.energy_threshold = 300
        a.pause_threshold = 0.5
        audio = a.listen(source)
    try:
        query = a.recognize_google(audio,language='en-in')
        print('Reconized')
        return query
    except Exception as e:
        print('say it again......')
        return 'none'
def meaning():
    #global query
    query = listen()
    print('you said:',query)
    for a, b in new_dict.items():
        if a == query:
            sent = f"{a} means {b}"
            print(sent)
    return sent



speak(meaning())




