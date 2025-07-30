import threading
import re
import requests
from bs4 import BeautifulSoup

DOMINIO = "https://django-anuncios.solyd.com.br"
URL_AUTOMOVEIS = "https://django-anuncios.solyd.com.br/automoveis/"
LINKS = []
TELEFONES = []

def requisicao(url):
    try:
        respostas = requests.get(url)
        if respostas.status_code == 200:
            return respostas.text
    except Exception as e:
        print(e)

def parsing(resposta_html):
    try:
        soup = BeautifulSoup(resposta_html, 'html.parser')
        return soup
    except Exception as e:
        print(e)

def encontrar_links(soup):
    try:
        cards_pai = soup.find('div', class_='ui three doubling link cards')
        cards = cards_pai.find_all('a', class_='card')
    except Exception as e:
        print(e)
        return None
    links = []
    for card in cards:
        try:
            link = card['href']
            links.append(link)
        except:
            pass
    return links

'''def acessar_anuncio(link):
    try:
        respostas = requests.get(dominio+link)
        if respostas.status_code == 200:
            return respostas.text
    except Exception as e:
        print(e)'''

def encontrar_telefone(soup):
    try:
        descricao = soup.find_all('div', class_='sixteen wide column')[2].p.get_text().strip()
    except Exception as e:
        print(e)
        return None
    
    regex = re.findall(r"\(?0?([1-9]{2})\)?[\s.-]?(9\d{4})[\s.-]?(\d{4})", descricao)
    if regex:
        return regex
    
def descobir_telefones():
    while True:
        try:
            link_anuncio = LINKS.pop(0)
        except:
            break
        resposta_anuncio = requisicao(DOMINIO+link_anuncio)

        if resposta_anuncio:
            soup_anuncio = parsing(resposta_anuncio)
            if soup_anuncio:
                telefones = encontrar_telefone(soup_anuncio)
                if telefones:
                    for telefone in telefones:
                        #print(f'Telefone encontrado: {telefone}')
                        TELEFONES.append(telefone)
                        
                        salvar_telefone(telefone)

def salvar_telefone(telefone):
    string_telefone = f'{telefone[0]}{telefone[1]}{telefone[2]}\n'
    try:
        with open('telefones.csv', 'a') as arquivo:
            arquivo.write(str(string_telefone))
    except Exception as e:
        print(e)

if __name__ == "__main__":

    resposta_busca = requisicao(URL_AUTOMOVEIS)
    
    if resposta_busca:
        soup_busca = parsing(resposta_busca)
        if soup_busca:
            LINKS = encontrar_links(soup_busca)
            THREADS = []
            for i in range(14):
                t = threading.Thread(target=descobir_telefones)
                THREADS.append(t)
            for t in THREADS:
                t.start()
            for t in THREADS:
                t.join()

    print('*' * 31)
    print(f'*    Telefones encontrados    *')
    for tel in TELEFONES:
        telefone = ''.join(tel)
        print(f'*  {telefone}                *')
    print('*' * 31)