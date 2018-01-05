import re
from datetime import datetime, timedelta

#classe que cria e valida as talks;
"""
A duração das palestras devem ser em minutos;
A duração da menor palestra será as lightnings que são de 5 minutos.
O título das palestras não contém números.
"""

class Talk:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
