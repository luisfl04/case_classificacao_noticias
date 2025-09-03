from processamento_noticias import ProcessadorNoticias
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter


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
        ax.pie(contagem_sentimentos.values, labels=contagem_sentimentos.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        # # Obtendo uma lista com os titulos das noticias e fazendo o processamento para contar as mais frequentes:
        # lista_titulos_noticias = data_frame_noticias["titulo"].astype(str).tolist()
        # lista_unificada = " ".join(lista_titulos_noticias)
        # lista_palavras = lista_unificada.lower().split()
        # contagem_frequencia_palavras = Counter(lista_palavras)
        # frequencia_limpa = contagem_frequencia_palavras.pop("em")
        # print(frequencia_limpa)

        # for titulo in titulos_noticias:
        #     titulo.mode()
                    
        st.pyplot(grafico_pizza)
    


if __name__ == "__main__":
    exibicao = ExibicaoProcessamentoNoticias()
    exibicao.exibir_dados()
