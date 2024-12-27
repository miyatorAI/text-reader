import pyttsx3

def main():
    engine = pyttsx3.init()
    with open('./data/sample.txt', encoding='UTF-8', mode='r') as file:
        content = file.read()
        engine.say(content)
        engine.runAndWait()

if __name__ == "__main__":
    main()
