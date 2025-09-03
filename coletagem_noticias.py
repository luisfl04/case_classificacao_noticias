import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

class GerenciadorColetaNoticias:
    """
    Objeto responsável pela busca e gerenciamento das noticias:
    """

    def coletar_noticias(self, pesquisa) -> list:
        """
        Função responsável por realizar a requisição no serviço do Google e coletar as noticias.
        """

        try:
            if pesquisa is None:
                raise Exception("Um valor para o campo de pesquisa é obrigatório!")

            # Montando e fazendo requisição:
            url_requisicao = f"https://news.google.com/rss/search?q={pesquisa}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
            resposta = requests.get(url_requisicao)
            if resposta.status_code != 200:
                raise ValueError(f"Erro ao acessar feed RSS\nCodigo -> {resposta.status_code}")
            
            # Convertendo resultado:
            root = ET.fromstring(resposta.content)
            noticias = []

            # Obtendo os dados das noticias:
            for item in root.findall(".//item"):
                titulo = item.find("title").text
                link = item.find("link").text
                data = item.find("pubDate").text
                fonte = self.extrair_fonte(item.find("description").text)
                noticias.append({
                    "titulo": titulo,
                    "link": link,
                    "data_publicacao": data,
                    "fonte": fonte,
                })

            # retornando número limitado de notícias:
            return noticias[:15]
        except Exception as e:
            raise Exception(f"Erro ao coletar as noticias -> {e}")
    
    def extrair_fonte(self, descricao_html: str) -> str:
        """
        Extrai o campo '<font>' a partir do campo '<description>' obtido na notícia.
        """
        try:    
            arvore_elementos_hmtl = BeautifulSoup(descricao_html, "html.parser")
            fonte = arvore_elementos_hmtl.find("font") 
            return fonte.get_text(strip=True) if fonte else ""  
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao obter afonte da notícia -> {e}")
