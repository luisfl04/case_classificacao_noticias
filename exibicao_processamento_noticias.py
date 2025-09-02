from processamento_noticias import ProcessadorNoticias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


class ExibicaoProcessamentoNoticias:
    
    """
    Módulo que obtém o data frame dos dados já classificados e cria as visualizações
    """ 

    def exibir_dados(self):
        # Obtendo data Frame:
        processador_noticias = ProcessadorNoticias()
        data_frame_noticias = processador_noticias.obter_df_noticias()

        st.title("Dashboard - Análise de Sentimento de Notíciais")

        # Criando gráfico de pizza com a partir da contagem das classificações de sentimento:
        contagem_sentimentos = data_frame_noticias["classificacao_sentimento"].value_counts()
        grafico_pizza, ax = plt.subplots()
        ax.pie(contagem_sentimentos, labels=["neutro", "positivo", "negativo"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        # Implementação da visualização de nuvens de palavras:
        titulos_noticias = data_frame_noticias["titulo"]
        print(titulos_noticias)


        # st.pyplot(grafico_pizza)
    
if __name__ == "__main__":
    exibicao = ExibicaoProcessamentoNoticias()
    exibicao.exibir_dados()
