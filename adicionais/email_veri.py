import asyncio 
import httpx          
from holehe import core
import logging

def email_verificacao(verificaremail):

    verificaremail = verificaremail.strip().lower()
    return verificaremail
    
async def FUN(verificaremail, COR, SALVAR_RES=None):
    print (40*"_")
    print("Varrendo: ", COR['AMARELO'],verificaremail,COR['FIM'])
    print (40*"-")
    sites = core.import_submodules("holehe.modules")
    extrair_info = core.get_functions(sites)
    RES = []
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        for extraídos in extrair_info:
            RES = []
            
            try:
                await core.launch_module(extraídos, verificaremail, client, out=RES)
                
                for res in RES:
                    if res.get("exists"):
                        nome_site = res.get('name', 'Desconhecido')
                        tel = res.get("phoneNumber", "Não detectado")
                        email2 = res.get("emailrecovery", "Não detectado")
                        outros = res.get("others", "Não detectado")  
                        print(f"| Conta encontrada --> {nome_site} | {verificaremail}")
                        print(f"| Telefone: {tel} | E-mail 2: {email2} | Outros: {outros}")
                        print(40 * "_")
                        
                        if SALVAR_RES is not None:
                            SALVAR_RES.append(f"""| Conta encontrada --> {nome_site} | {verificaremail}
                            | Telefone: {tel} | E-mail 2: {email2} | Outros: {outros}
                            \n\n""")
                                       
            except Exception as ERR:
                print("Erro identificado: ", ERR)