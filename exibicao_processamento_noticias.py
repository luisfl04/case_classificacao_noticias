from processamento_noticias import ProcessadorNoticias
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import plotly.express as px
import seaborn as sns


class ExibicaoProcessamentoNoticias:
    
    """
    Módulo que obtém o data frame dos dados já classificados e cria as visualizações
    """ 

    def exibir_dados_analisados(self, pesquisa):
        try:
            # Obtendo data Frame:
            processador_noticias = ProcessadorNoticias()
            data_frame_noticias = processador_noticias.obter_df_noticias(pesquisa)
            
            # configs básicas do dashboard:
            st.title("Classificação de 'sentimento' de noticias")
            st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

            # ****** Tabela com os dados classificados *******
            # Métricas gerais:
            st.subheader("Métricas gerais observadas:")
            coluna_total_noticias, coluna_classificacao_frequente = st.columns(2)
            coluna_total_noticias.metric("Total de noticias", data_frame_noticias["titulo"].count())
            coluna_classificacao_frequente.metric("Classificação mais frequente", data_frame_noticias['classificacao_sentimento'].value_counts().index[0])

            # Pesquisa Feita:
            st.subheader("Tema Pesquisado")
            st.text(f"{pesquisa}")
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

            # Tabela oriúnda dos dados processados:
            st.subheader("Tabela Interativa obtida do processamento")
            st.dataframe(data_frame_noticias)
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            

            # ***** Gráfico de Pizza ******

            # Criando gráfico de pizza com a partir da contagem das classificações de sentimento:
            st.subheader("Distribuição das classificações")
            contagem_sentimentos = data_frame_noticias["classificacao_sentimento"].value_counts()
            fig = px.pie(contagem_sentimentos, names=contagem_sentimentos.index, values=contagem_sentimentos.values)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)


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
            nuvem_palavras = WordCloud(width=800, height=400, background_color="white", colormap="plasma").generate_from_frequencies(contagem_frequencia_palavras)
            figura_nuvem_palavras, axes_nuvem_palavras = plt.subplots(figsize=(10, 5))
            axes_nuvem_palavras.imshow(nuvem_palavras, interpolation="bilinear")
            axes_nuvem_palavras.axis("off")
            st.header("Termos mais frequentes")
            st.pyplot(figura_nuvem_palavras)
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)


            # ***** Gráfico exibindo dados apenas das noticias classificadas como positivas ***********
            data_frame_positivos = data_frame_noticias[data_frame_noticias["classificacao_sentimento"] == "positivo"]
            st.subheader("Dados de noticias classificadas como positivas")
            figura_scatter_plot, axes_scatter_plot = plt.subplots(figsize=(8, 3))
            sns.scatterplot(data=data_frame_positivos, x="fonte", y="data_publicacao", ax=axes_scatter_plot)
            axes_scatter_plot.set_xlabel("Fonte da notícia")
            axes_scatter_plot.set_ylabel("Data em que foi publicada")
            st.pyplot(figura_scatter_plot)
            st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)


            # Rodapé da página:        
            st.markdown(
                """
                <style>
                .footer {
                    position: fixed;
                    left: 0;
                    bottom: 0;
                    width: 100%;
                    text-align: center;
                    font-size: 14px;
                    color: gray;
                    background-color: #f0f2f6;
                }
                </style>
                <div class="footer">
                    Esta análise é limitada e usou dados de comparação que possívelmente não se aplicam a todos os contextos.<br>
                    Verifique as informações!
                </div>
                """,
                unsafe_allow_html=True
            )

            # Aviso sobre uso de modelos de IA:
            st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
            st.warning("⚠️ Não utilizamos modelos de IA na análise, apenas bases de dados com palavras já rotuladas.")
        except Exception as e:
            st.error(f"Erro ao renderizar o dashboard -> {e}")

