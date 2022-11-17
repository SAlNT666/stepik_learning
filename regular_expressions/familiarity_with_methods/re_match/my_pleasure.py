import re


greetings = input()
if re.match(r'Здравствуйте|Hello', greetings):
    print('Ну привет!')
else:
    print('Фу, как некультурно!')
