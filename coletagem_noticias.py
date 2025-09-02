import requests
import xml.etree.ElementTree as ET

class GerenciadorColetaNoticias:
    """
    Objeto responsável pela busca e gerenciamento das noticiais.s
    """

    def coletar_noticias(self, pesquisa) -> list:
        """
        Função responsável por realizar a requisição no serviço do Google e coletar as noticiais.
        """

        try:
            # Montando e fazendo requisição:
            url_requisicao = f"https://news.google.com/rss/search?q={pesquisa}&hl=pt-BR&gl=BR&ceid=BR:pt-419"
            resposta = requests.get(url_requisicao)
            if resposta.status_code != 200:
                raise ValueError(f"Erro ao acessar feed RSS\nCodigo -> {resposta.status_code}")
            
            # Convertendo resultado:
            root = ET.fromstring(resposta.content)
            noticias = []

            # Obtendo os dados das noticiais:
            for item in root.findall(".//item"):
                titulo = item.find("title").text
                link = item.find("link").text
                data = item.find("pubDate").text
                descricao = item.find("description").text
                noticias.append({
                    "titulo": titulo,
                    "link": link,
                    "data": data,
                    "descricao": descricao
                })

            # retornando número limitado de notícias:
            return noticias[:15]
        except Exception as e:
            raise ValueError(f"Erro ao coletar as noticiais -> {e}")