from coletagem_noticias import GerenciadorColetaNoticias
import re


class ProcessadorNoticiais:
    """
    Módulo relacionado a manipulação e processamento das noticiais obtidas.
    """

    def obter_noticiais(self) -> list:
        gerenciador_de_coleta = GerenciadorColetaNoticias()
        noticiais = gerenciador_de_coleta.coletar_noticias("Intelgência Artificial Piaúi")  
        print(noticiais)
        return noticiais

    def limpar_texto(self, texto):
        """
        Função que padroniza o texto em letras minúsculas, remove caracteres especiais e espaçoes extras.
        """
        texto = texto.lower()
        texto = re.sub(r'[^a-zA-Z0-9áàâãéêíóôõúüç\s]', '', texto)        
        texto = re.sub(r'\s+', ' ', texto).strip()
        return texto




if __name__ == "__main__":
    processador = ProcessadorNoticiais()
    processador.obter_noticiais()


