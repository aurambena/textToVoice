"""This script recibes an URL from user and turn the text to a voice file .mp3. 
The user can choose the language, in this case English, Spanish, French and Portuguese
It's important to choose the correct language, in other case the scrit send the user
to the main menu. The script takes 300 caracters (that can be change on info_url) """


#import standar modules
from newspaper import Article
from gtts import gTTS
from playsound import playsound

#define variables needed
keep_asking = True

while keep_asking:

    class ToVoice():
        """recibes an URL from user, extract the text and turn to a voice file .mp3"""
        def __init__(self, url, language) -> None:
            self.url = url
            self.language = language
            self.text_to_read = ''

        #Download URL text
        def info_url(self):
            article = Article(self.url, language=self.language)
            article.download()
            article.parse()
            #read the text inside the url
            self.text_to_read = article.text[:300]
            print('URL succesfully introduced')
            print(self.text_to_read)
        
        #save the text as .mp3 audio
        def convert_to_mp3(self):
            text_to_voice = gTTS(self.text_to_read)
            speech_file = 'voice.mp3'
            text_to_voice.save(speech_file)
            print('File succesfully created')
        
        #reproduce the audio file
        def reproduce_mp3(self):
            playsound('voice.mp3')

    #allows the user to choose an option from a menu
    opcion = input("1. Insert URL\n2. Convert text to mp3\n3. Reproduce mp3\n4. Finish program\
    \nElige una opción: ")

    #Introduce the URL and language, does exception control in case the user introduce
    #numbers or an URL that does not exist
    if opcion == '1':
        try:
            Url = input('Introduce the URL: ')
            language = input('Introduce text language, \nEnglish: en \nSpanish: es \nFrench: fr\nPortuguese: pt\n')
            to_voice = ToVoice(Url, language)
            to_voice.info_url()
        except:
            print('URL or language no validate, please, try again')
    
    #creates the .mp3 file
    elif opcion == '2':
        to_voice.convert_to_mp3()

    #reproduces the .mp3 file
    elif opcion == '3':
        to_voice.reproduce_mp3()

    #exit the program
    elif opcion == '4':
        print('shutting down the program')
        keep_asking = False

