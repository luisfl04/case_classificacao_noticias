from dashboard.exibicao_processamento_noticias import ExibicaoProcessamentoNoticias
import streamlit as st


class DashBoardClassificacaoNoticias:
    def main(self):
        try:
            st.set_page_config(page_title="Dashboard - Análise de Análise de Noticias")
            temas_pesquisas = ["Inteligência Artificial Piauí", "SIA Piauí"]

            # Interação incial:
            st.title("Bem-vindo ao Dashboard de Análise Notícias")
            st.write("Selecione um tema para continuar:")
            tema_escolhido = st.selectbox("Escolha o tema da pesquisa para análise", [""] + temas_pesquisas)
            
            # Fluxo de renderização da análise:
            if tema_escolhido != "":
                st.success(f"✅ Tema selecionado: **{tema_escolhido}**")
                exibicao_dashboard = ExibicaoProcessamentoNoticias()
                exibicao_dashboard.exibir_dados_analisados(tema_escolhido)
            else:
                st.warning("⚠️ Escolha um tema acima para carregar o dashboard.")
        except Exception as e:
            st.error(f"Erro ao inicializar o dashboard -> {e}")


if __name__ == "__main__":
    dashboard = DashBoardClassificacaoNoticias()
    dashboard.main()
