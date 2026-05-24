import asyncio 
import httpx              
from holehe import core
import logging
logging.getLogger("bs4").setLevel(logging.CRITICAL)

def combinacoes(nome, sobrenome):
 
    nome = nome.strip().lower()
    sobrenome = sobrenome.strip().lower()
    tipo = ["gmail.com", "outlook.com", "hotmail.com"]
    
    
    FORMAR = [
        f"{nome}.{sobrenome}",
        f"{nome}{sobrenome}",       
        f"{nome[0]}{sobrenome}",
        f"{nome}{sobrenome[0]}"
    ]
    
    lista_de_email = []
    
    for FORMA in FORMAR:
        for tipo_loop in tipo:
            lista_de_email.append(f"{FORMA}@{tipo_loop}")
    return lista_de_email
        
async def TESTE(lista_de_email, dados, COR, SALVAR_RES=None):
    print(dados['men1'],f"{len(lista_de_email)}")    
    modules = core.import_submodules("holehe.modules")  
    websites = core.get_functions(modules)
     
    async with httpx.AsyncClient(timeout=10.0) as client:        
        for email in lista_de_email:                      
            for website in websites:
                out = []
                
                try:                   
                    await core.launch_module(website, email, client, out)
                                     
                    if out:
                        for RES in out:                           
                            if RES.get("exists") and RES.get("rateLimit") is False:
                                print(f"{dados['S']} Conta encontrada no {RES['name']} {COR['AMARELO']}({email}){COR['FIM']}")
                                if SALVAR_RES is not None:
                                
                                    SALVAR_RES.append(f"{dados['S']} Conta encontrada no {RES['name']} ({email})")
                                    
                except Exception:
                    continue
                    