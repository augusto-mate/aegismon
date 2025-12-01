# aegismon/utils/helpers.py
""" Funções utilitárias diversas para o AegisMon. """

def format_bytes(size):
    """ Formata um número de bytes em uma string legível (e.g., 1.2 KB, 3.4 MB). """
    if size is None:
        return "N/A"
    
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    i = 0
    while size >= 1024 and i < len(units) - 1:
        size /= 1024.0
        i += 1
    
    return f"{size:.2f} {units[i]}"