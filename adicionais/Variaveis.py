def Variaveis():
    COR = CORES()    
    descricao = "buscar Nickname em plataformas"    
    erro1 = "Nenhum comando reconhecido pelo sistema, tente novamente"    
    S = f"{COR['VERDE']}Encontrado{COR['FIM']}"    
    V = f"{COR['VERDE']}Verificação{COR['FIM']}"    
    erro2 = "Erro identificado"    
    descI = "Salva os resultados em um arquivo.txt"    
    arq = "Salvo com sucesso"    
    a = "Arquivo"    
    descG = "Verificação de email"    
    men1 = """Número de combinações --> """               
    nm = "comando deve ser utilizado junto com -sn pois e a variável necessária para nome"    
    sn = "comando deve ser utilizado junto com -e pois e a variável necessária pelo sobrenome"
    
    return {
    "descricao": descricao, 
    "erro1": erro1, 
    "S": S,
    "V": V, 
    "erro2": erro2, 
    "descI": descI,
    "arq": arq, 
    "a": a,
    "descG": descG, 
    "men1": men1, 
    "nm": nm, 
    "sn": sn
      }

def CORES():
    VERDE = "[\033[1;32m"
    FIM = "\033[0m"
    AMARELO = "\033[43m"
    
    return {
    "VERDE": VERDE,
    "FIM": FIM,
    "AMARELO": AMARELO
    }