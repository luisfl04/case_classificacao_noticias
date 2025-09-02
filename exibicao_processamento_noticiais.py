from processamento_noticiais import ProcessadorNoticiais
import streamlit as st
import matplotlib.pyplot as plt


class ExibicaoProcessamentoNoticiais:
    
    """
    Módulo que obtém o data frame dos dados já classificados e cria as visualizações
    """ 

    def exibir_dados(self   ):
        processador_noticiais = ProcessadorNoticiais()
        data_frame = processador_noticiais.obter_df_noticiais()

        st.title("Dasboard de classificação")

        fig, ax = plt.subplots()
        ax.pie(data_frame["classificacao"], labels=data_frame["classificacao"], autopct="%1.1f%%", startangle=90)
        ax.axis("equal")  # Deixa a pizza redonda

        # Exibindo no Streamlit
        st.pyplot(fig)
    
if __name__ == "__main__":
    exibicao = ExibicaoProcessamentoNoticiais()
    exibicao.exibir_dados()
