from abc import ABC, abstractmethod

class MetodoDeEnvio(ABC):
    @abstractmethod
    def get_contacts(custom_fields):
        pass
    @abstractmethod
    def send(assunto, columns_data, destinatario):
        pass