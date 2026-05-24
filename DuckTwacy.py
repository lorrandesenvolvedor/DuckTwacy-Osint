from adicionais.Variaveis import Variaveis, CORES
from adicionais.O_Olista import LISTA
import argparse
import sys 
import requests
from bs4 import BeautifulSoup
import asyncio 
from adicionais.email import combinacoes, TESTE
from adicionais.email_veri import email_verificacao, FUN
from adicionais.imagens.imagem import imagem
def OSINT(Variaveis):
    dados = Variaveis()   
    IMG = imagem()
    COR = CORES()
    print (IMG['imagem'])
    VARIAVEL = argparse.ArgumentParser(description=f"DuckTwacy-Osint Desenvolvido por @LorranC.S.")
    VARIAVEL.add_argument('-b', '--busca', help=dados['descricao'], action='append')
    VARIAVEL.add_argument('-s', '--salvar', help=dados['descI'])
    VARIAVEL.add_argument('-n', '--nome', help=dados['nm'])
    VARIAVEL.add_argument('-sn', '--sobrenome', help=dados['sn'])
    VARIAVEL.add_argument('-vE', '--verificaremail', help='verifica emails')
    VARIAVEL2 = VARIAVEL.parse_args()
    
    if not (VARIAVEL2.busca or VARIAVEL2.salvar or VARIAVEL2.nome or VARIAVEL2.sobrenome or VARIAVEL2.verificaremail):
        print (dados['erro1'])
        sys.exit()
    SALVAR_RES = []     
    if VARIAVEL2.busca: 
        for NICK in VARIAVEL2.busca:   
            for SITE in LISTA:
                site = (f"{SITE.rstrip('/')}/{NICK}")
            
                try:
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept-Language': 'en-US,en;q=0.9'
                    }
                    REQ = requests.get(site, headers=headers, timeout=5)
                    if REQ.status_code == 200:
                        ver = BeautifulSoup(REQ.text, 'html.parser')
                        titulo = ver.title.text.lower() if ver.title else " "
                        nao_acessar = ["login", "entrar", "sign in", "welcome", "não encontrado", "not found", "profiles", "Erro"]
                        if NICK.lower() in REQ.text.lower() and not any(falsa in titulo for falsa in nao_acessar):                                              
                            print(f"{dados['S']} {site} {dados['V']} {REQ}\n\n")  
                            SALVAR_RES.append(f"{dados['S']} {site} {dados['V']} {REQ}\n\n")  
                except Exception as err:
                    print(dados['erro2'], err)      
                                                                
    if VARIAVEL2.nome and VARIAVEL2.sobrenome:
        lista_de_email = combinacoes(VARIAVEL2.nome, VARIAVEL2.sobrenome)
        asyncio.run(TESTE(lista_de_email, dados, COR, SALVAR_RES))
    
    if VARIAVEL2.verificaremail:
        #FUNCAO
        email_V = email_verificacao(VARIAVEL2.verificaremail)
        asyncio.run(FUN(email_V, COR, SALVAR_RES))

    if VARIAVEL2.salvar:     
        if SALVAR_RES:                   
            with open(f"{VARIAVEL2.salvar}.txt", 'a' , encoding='utf-8') as arquivo:
                for RES_SALVO in SALVAR_RES:
                    arquivo.write(RES_SALVO)               
            print (f"{dados['a']} {VARIAVEL2.salvar}.txt {dados['arq']}")      
                  
                        
if __name__ == "__main__":
    OSINT(Variaveis)
    
    
    