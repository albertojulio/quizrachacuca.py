from bs4 import BeautifulSoup
import requests
 
url = 'https://rachacuca.com.br/quiz/solve/77750/one-piece-akuma-no-mi/'
r = requests.get(url)
 
soup = BeautifulSoup(r.content, 'html.parser')
resultado = soup.findAll('p')
 
perguntas = {}
respostas = []
achou_pergunta = False
pergunta = ''
num_resposta = 0
 
for linha in resultado:
    if '?' in linha.get_text():
        if achou_pergunta:
            perguntas[pergunta] = respostas
            respostas = []
            num_resposta = 0
        pergunta = linha.get_text()
        perguntas[pergunta] = []
        achou_pergunta = True
    elif '?' not in linha.get_text() and achou_pergunta:
        if num_resposta < 5:
            respostas.append(linha.get_text())
            num_resposta += 1
        
perguntas[pergunta] = respostas
 
for pergunta, resposta in perguntas.items():
    print(pergunta,':', resposta)
