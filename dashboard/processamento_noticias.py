from dashboard.coletagem_noticias import GerenciadorColetaNoticias
import re
import pandas as pd


class ProcessadorNoticias:
    """
    Módulo relacionado a manipulação e processamento das noticias obtidas.
    """

    def obter_noticias(self, pesquisa) -> list:
        try:
            gerenciador_de_coleta = GerenciadorColetaNoticias()
            return gerenciador_de_coleta.coletar_noticias(pesquisa)  
        except Exception as e:
            raise Exception(f"Não foi possível coletar as notícias -> {e}")

    def limpar_texto(self, texto) -> str:
        """
        Função que padroniza o texto em letras minúsculas, remove caracteres especiais e espaçoes extras.
        """

        try:
            if texto is None:
                raise Exception("Um valor de texto é obrigatório!")

            texto = texto.lower()
            texto = re.sub(r'[^a-zA-Z0-9áàâãéêíóôõúüç\s]', '', texto)        
            texto = re.sub(r'\s+', ' ', texto).strip()
            return texto
        except Exception as e:
            raise Exception(f"Erro ao limpar conteúdo de texto -> {e}")


    def processar_noticias(self, pesquisa) -> list:
        
        try:
            # Obtendo noticias:
            noticias = self.obter_noticias(pesquisa)
            
            # Criando e populando objeto que armazenará os dados de forma pré-processada:
            dados_noticias_formatados = []
            for noticia in noticias:
                titulo = self.limpar_texto(noticia.get("titulo"))
                data = noticia.get("data_publicacao")[5:-4]
                link = noticia.get("link")
                fonte = self.limpar_texto(noticia.get("fonte"))
                dados_noticias_formatados.append({
                    "titulo": titulo,
                    "data_publicacao": data,
                    "link": link,
                    "fonte": fonte
                })

            # Carregando lexico e classificando os titulos:
            lexico = self.carregar_lexico()

            for noticia in dados_noticias_formatados:
                titulo_comparado = noticia.get("titulo")
                classificacao = self.classificar_titulo_noticia(titulo_comparado, lexico)
                noticia["classificacao_sentimento"] = classificacao
            
            return dados_noticias_formatados
        except Exception as e:
            raise Exception(f"Não foi possível processar os dados das notícias -> {e}")

    def carregar_lexico(self) -> dict:
        """
        Ler cada linha do arquivo sentiLex e adiciona à um dicionário a palavra e o seu valor de polaridade
        usando a estrutura chave-valor Por fim, retorna o dicionário.
        """
        
        try:
            lexico = {}
            with open("lexico/sentiLex-flex-pt02.txt", "r", encoding="utf-8") as arquivo_lexico:
                for linha in arquivo_lexico:
                    partes_linha = linha.strip().split(",")
                    if len(partes_linha) < 2:
                        continue
                    palavra = partes_linha[0]
                    match = re.search(r"POL:N0=(-?\d+)", linha)
                    if match:
                        polaridade = int(match.group(1))
                        lexico[palavra] = polaridade
            return lexico
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao carregar o lexico de palavras -> {e}")


    def classificar_titulo_noticia(self, titulo: str, lexicon: dict) -> str:
        
        try:
            score = 0
            palavras = titulo.split()

            for palavra in palavras:
                if palavra in lexicon:
                    score += lexicon[palavra]

            if score > 0:
                return "positivo"
            elif score < 0:
                return "negativo"
            else:
                return "neutro"
        except Exception as e:
            raise Exception(f"Ao tentar classificar as palavras do título '{titulo}', ocorreu um erro -> {e}")


    def obter_df_noticias(self, pesquisa) -> object:
        """
        Função que obtém a lista de noticias classificadas e estrutura um data frame a partir desses dados, 
        além de chamar a função responsável por criar o arquivo excel a partir destes mesmos dados.
        """
        
        try:
            dados_noticias_classificadas = self.processar_noticias(pesquisa)
            data_frame = pd.DataFrame(
                data=dados_noticias_classificadas,                       
                columns=["titulo", "data_publicacao", "link", "fonte", "classificacao_sentimento"])

            self.criar_arquivo_csv(data_frame)
            return data_frame
        except Exception as e:
            raise Exception(f"Não foi possível criar o data frame/arquivo_csv dos dados processados -> {e}")


    def criar_arquivo_csv(self, data_frame):
        """
        Cria um arquivo csv a partir dos dados do data frame processados
        """
        
        try:    
            data_frame.to_csv("classificacao_sentimentos_noticias.csv", sep=",", index=False, encoding="utf-8")
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao criar o arquivo csv oriundo dos dados processados -> {e}")


