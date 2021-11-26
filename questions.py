#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
from random import randint

n = None
if len(sys.argv) == 2: 
    try:
        n = int(sys.argv[1])-1
    except: pass

if not n or (n < 1 or n > 60): 
    n = randint(0,59)

url = 'https://danielmiessler.com/study/infosec_interview_questions/'
page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')
content = soup.find('div', class_='entry-content')

questions = []

for h3 in soup.find_all('h3'):
    nx = h3.next_sibling
    ans = []
    while nx and nx.name != 'h3':
        if nx.name == 'p':
            ans.append(nx.text)
        nx = nx.next_sibling
    questions.append({'q':h3.text,'a':' '.join(ans)})

def get_quest(x):
    return 'question: {}\nanswer: {}'.format(
        questions[x]['q'],
        questions[x]['a']
    )

print(get_quest(n))

