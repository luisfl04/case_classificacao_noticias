import requests
import xml.etree.ElementTree as ET


class GerenciadorColetaNoticias:

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
            
            # Convertendo resultado
            root = ET.fromstring(resposta.content)
            noticias = []

            print(root)

            
            #     for item in root.findall(".//item"):
            #         titulo = item.find("title").text
            #         link = item.find("link").text
            #         data = item.find("pubDate").text
            #         descricao = item.find("description").text
            #         noticias.append({
            #             "titulo": titulo,
            #             "link": link,
            #             "data": data
            #         })
                
            #     return noticias
        except Exception as e:
            raise ValueError(f"Erro ao coletar as noticiais -> {e}")
        
if __name__ == "__main__":
    gerenciador_coleta = GerenciadorColetaNoticias()
    resultados = gerenciador_coleta.coletar_noticias("inteligência artificial piauí")
    for noticia in resultados:
        print(f"{noticia}")
        break
