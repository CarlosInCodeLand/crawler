# Crawler de Telefones em um Site de Anuncios

Este projeto é um crawler em Python que coleta números de telefone de anúncios de automóveis do site [django-anuncios.solyd.com.br](https://django-anuncios.solyd.com.br) e exporta os dados em um arquivo CSV organizado.

## Funcionalidades

- Acessa a página de anúncios de automóveis.
- Extrai os links de cada anúncio.
- Acessa cada anúncio individualmente.
- Extrai números de telefone dos anúncios.
- Salva os telefones encontrados em um arquivo CSV, organizando DDD, prefixo e sufixo em colunas.

## Requisitos

- Python 3.7+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## Instalação

1. Clone este repositório ou baixe os arquivos.
2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv ambientetestes
   source ambientetestes/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requeriments.txt
   ```

## Como usar

1. Execute o script principal:
   ```bash
   python crawler.py
   ```
2. Os números de telefone extraídos serão salvos no arquivo `telefones.csv` no formato:
   ```
   11912345678
   21987654321
   ```

## Estrutura dos arquivos principais

- `crawler.py`: Script principal do crawler.
- `telefones.csv`: Arquivo gerado com os telefones extraídos.

## Observações

- O crawler depende da estrutura atual do site. Mudanças no HTML podem exigir ajustes no código.
- O uso deste crawler é apenas para fins educacionais.

## Licença

MIT 
