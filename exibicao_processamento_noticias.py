from processamento_noticias import ProcessadorNoticias
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import pandas as pd




class ExibicaoProcessamentoNoticias:
    
    """
    Módulo que obtém o data frame dos dados já classificados e cria as visualizações
    """ 

    def exibir_dados(self):
        # # Obtendo data Frame:
        # processador_noticias = ProcessadorNoticias()
        # data_frame_noticias = processador_noticias.obter_df_noticias()
        
        data_frame_noticias = pd.read_csv("classificacao_sentimentos_noticias.csv")
        
        # configs básicas do dashboard:
        st.title("Dashboard - Classificação de 'sentimento' de noticias")

        # ****** Tabela com os dados classificados ******** 
        coluna_total_noticias, coluna_classificacao_frequente = st.columns(2)
        coluna_total_noticias.metric("Total de noticias", data_frame_noticias["titulo"].count())
        coluna_classificacao_frequente.metric("Classificação mais frequente:", data_frame_noticias['classificacao_sentimento'].value_counts().index[0])
        st.text("Tabela com as noticias classificadas", width=500)
        st.dataframe(data_frame_noticias)
        
        # ***** Gráfico de Pizza ******

        # Criando gráfico de pizza com a partir da contagem das classificações de sentimento:
        contagem_sentimentos = data_frame_noticias["classificacao_sentimento"].value_counts()
        grafico_pizza, axes_grafico_pizza = plt.subplots()
        axes_grafico_pizza.pie(contagem_sentimentos.values, labels=contagem_sentimentos.index, autopct="%1.1f%%", startangle=90)
        axes_grafico_pizza.axis("equal")
        st.title("Grafico de pizza")     
        st.pyplot(grafico_pizza)

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

        # Exibindo nuvem de palavras:
        nuvem_palavras = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(contagem_frequencia_palavras)
        figura_nuvem_palavras, axes_nuvem_palavras = plt.subplots(figsize=(10, 5))
        axes_nuvem_palavras.imshow(nuvem_palavras, interpolation="bilinear")
        axes_nuvem_palavras.axis("off")
        st.title("Nuvem de palavras frequêntes")
        st.pyplot(figura_nuvem_palavras)



    


if __name__ == "__main__":
    exibicao = ExibicaoProcessamentoNoticias()
    exibicao.exibir_dados()
