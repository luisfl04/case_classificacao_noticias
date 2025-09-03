from processamento_noticias import ProcessadorNoticias
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords





class ExibicaoProcessamentoNoticias:
    
    """
    Módulo que obtém o data frame dos dados já classificados e cria as visualizações
    """ 

    def exibir_dados(self):
        # Obtendo data Frame:
        processador_noticias = ProcessadorNoticias()
        data_frame_noticias = processador_noticias.obter_df_noticias()
        
        st.title("Dashboard - Análise de Sentimento de Notíciais")

        # ***** Gráfico de Pizza ******

        # Criando gráfico de pizza com a partir da contagem das classificações de sentimento:
        contagem_sentimentos = data_frame_noticias["classificacao_sentimento"].value_counts()
        grafico_pizza, ax = plt.subplots()
        ax.pie(contagem_sentimentos.values, labels=contagem_sentimentos.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")


        # ****** Nuvem de Palavras ******

        # Obtendo uma lista de palavras a partir dos titulos das noticias:
        lista_titulos_noticias = data_frame_noticias["titulo"].astype(str).tolist()
        lista_unificada = " ".join(lista_titulos_noticias)
        lista_palavras = lista_unificada.lower().split()
        
        # Buscando palavras removíveis a partir de um conjunto baixado, que podem estar na lista de palavras, como pronomes:
        nltk.download("stopwords")
        palavras_removiveis = set(stopwords.words("portuguese"))
        
        # Obtendo palavras filtradas:
        lista_palavras_filtradas = [palavra for palavra in lista_palavras if palavra not in palavras_removiveis]
        contagem_frequencia_palavras = Counter(lista_palavras_filtradas)
        palavras_mais_comuns = contagem_frequencia_palavras.most_common(10)

        # Exibindo nuvem de palavras:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(frequencias)



                            
        # st.pyplot(grafico_pizza)
    


if __name__ == "__main__":
    exibicao = ExibicaoProcessamentoNoticias()
    exibicao.exibir_dados()
