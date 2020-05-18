from bs4 import BeautifulSoup
import requests

url = 'https://rachacuca.com.br/quiz/18992/bleach-sagas/'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

soup

perguntas = soup.find('ol').li.p.text
#print(perguntas)
respostas = soup.find('ol').find('div', class_='alternativa-texto').p.text
#print(respostas)

todos_elementos = soup.find_all('ol')
#print(todos_elementos)

for elemento in todos_elementos:
  perguntas = elemento.find('ol')li.p.text
  respostas = elemento.find('div', class_='alternativa-texto').p.text

  print(f'perguntas: {perguntas}')
  print(f'respostas: {respostas}')
  print('-'*70)