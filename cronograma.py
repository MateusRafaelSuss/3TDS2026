from datetime import datetime
from palestrante import Palestrante
from event import Event
from typing import Dict, List

class cronograma:
    def __init__(self, eventos: List, palestrantes: List, horario: datetime):
        self.eventos = eventos,
        self.palestrantes = palestrantes,
        self.horario = horario
        
    @classmethod
    def create_cronograma(cls, data: Dict):
        return cls(
            eventos = data['eventos'],
            palestrantes = data['palestramtes'],
            horario = data['horario']
        )
        