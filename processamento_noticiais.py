from coletagem_noticias import GerenciadorColetaNoticias


class ProcessadorNoticiais:
    """
    Módulo relacionado a manipulação e processamento das noticiais obtidas.
    """

    def obter_noticiais(self):
        gerenciador_de_coleta = GerenciadorColetaNoticias()
        noticiais = gerenciador_de_coleta.coletar_noticias("Intelgência Artificial Piaúi")  
    

    def limpar_texto(texto):
        




if __name__ == "__main__":
    processador = ProcessadorNoticiais()
    processador.obter_noticiais()


