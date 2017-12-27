###Cria bloco de sessões para ser adicionadas as palestras;
"""
Há dois blocos de sessões: manhã e tarde.
Sessão da manhã se inicia as 9h;
Sessão da tarde se inicia as 13h;
A sessão da tarde deve ser finalizada entre 16h e 17h a tempo
de se realizar o evento de network.
"""

class Sessions:

    def __init__(self, Talks, block):
        self.talks = Talks
        self.block = block
