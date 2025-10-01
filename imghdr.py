# imghdr.py - fallback para Python 3.13+

def what(file, h=None):
    """
    Retorna None sempre, só para evitar erro de import.
    O python-telegram-bot usa imghdr apenas para tentar
    adivinhar tipo de imagem, mas não é crítico no seu bot.
    """
    return None