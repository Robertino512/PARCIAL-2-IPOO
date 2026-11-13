from abc import ABC, abstractmethod

class Bonificable(ABC):

    @abstractmethod
    def aplicar_bonificacion(self, importe):
        pass