from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import smtplib
import sys
from weather import Weather


def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            com = '.com'
            url = 'https://www.' + domain + com
            webbrowser.open(url)
            print('تم!')
        else:
            pass
    elif 'what' in command:
        reg_ex = re.search('what (.*)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            com = '.com'
            url = 'https://www.google.com/search?q=' + domain 
            webbrowser.open(url)
            print('تم!')
    elif 'music' in command:
        reg_ex = re.search('music', command)
        if reg_ex:
           # domain = reg_ex.group(1)
            com = '.com'
            url = 'https://youtu.be/rKJ3bDLtOxc' 
            webbrowser.open(url)
            print('تم!')        
    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'current weather' in command:
        reg_ex = re.search('current weather (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    elif 'weather forecast ' in command:
        reg_ex = re.search('weather forecast (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))

# add
    elif 'exit' in command :
        talkToMe('مع السلامة')
        sys.exit(0)
        
    elif 'email' in command:
        talkToMe('من تريد الأرسال له')
        recipient = myCommand()

        if 's' in recipient:
            talkToMe('ماذا تريد ان تقول')
            content = myCommand()          
            class Email_bot:
                count = 0

                def __init__(self):
                    try:
                        cj = 'cj505jon@gmail.com'
                        print('\n[+]Initializing program [+]')
                        self.target = str(cj)
                        self.mode = int(1)
                        if int(self.mode) >  int(self.mode) < int(1):
                            print('ERROR: Invalid Option. GoodBye.')
                            sys.exit(1)
                    except Exception as e:
                        print(f'ERROR: {e}')
                def spam(self):
                    try:
                        print('\n[+] Setting up bot [+]')
                        self.amount = None
                        if self.mode == int(1):
                            self.amount = int(0)
          
                        else:
                             self.amount = int(input( 'Choose a CUSTOM amount : '))
            
                    except Exception as e:
                        print(f'ERROR: {e}')   
                def email(self):
                    try:
                        print('\n[+] Setting up email [+]')
                        self.server = str(1)
                        premade = ['1']
                        default_port = True
                        if self.server not in premade:
                            default_port = False
                            self.port = int(input('Enter port number : '))

                        if default_port == True:
                            self.port = int(587)

                        if self.server == '1':
                            self.server = 'smtp.gmail.com'
           
                        megmail = '3azoz505@gmail.com' 
                        password = 'A$0509099372z'
                        message = 'message'
                        self.fromAddr = str(megmail)
                        self.fromPwd = str(password)
                        self.subject = str(message)
                        self.message = str(content)

                        self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                        ''' % (self.fromAddr, self.target, self.subject, self.message)

                        self.s = smtplib.SMTP(self.server, self.port)
                        self.s.ehlo()
                        self.s.starttls()
                        self.s.ehlo()
                        self.s.login(self.fromAddr, self.fromPwd)
                    except Exception as e:
                        print(f'ERROR: {e}')

                def send(self):
                    try:
                        self.s.sendmail(self.fromAddr, self.target, self.msg)
                        self.count +=1
                        print('SPAM: {self.count}')
                    except Exception as e:
                        print(f'ERROR: {e}')

                def attack(self):
                    print('\n[+] sening ... [+]')
                    for email in range(self.amount+1):
                        self.send()
                    self.s.close()
                    print('\n[+] sending finished [+]')
                  #  sys.exit(0)


            if __name__=='__main__':
                spam = Email_bot()
                spam.spam()
                spam.email()
                spam.attack()

        
            talkToMe('تم الأرسال.')

        else:
            talkToMe('I don\'t know what you mean!')

# add
talkToMe('انا مستعد لي اوامرك')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
