import random

SACAR=["s","sacar","saque"]
DEPOSITAR=["d","depositar","deposito"]
VISUALISAR_EXTRATO=["v","visualisar","extrato"]

extrato=random.randrange(0,7000)
numero_saques_restantes=3


while(True):
    menu=input("""-Menu Inicial-
                     -Escolha uma opção:
                      -Sacar(s) 
                      -Depositar(d) 
                      -Visualisar Extrato(v)
                      -Fechar(f)\n""").lower().strip().replace(" ","")
    if menu in SACAR:        
        if numero_saques_restantes>0:
            valor_saque=float(input("Quanto deseja sacar?"))
            if  valor_saque>0 and valor_saque<=500 and extrato-valor_saque>=0:
                    extrato-=valor_saque
                    numero_saques_restantes-=1
                    print(f"""Voce sacou R${valor_saque:.2f} e ficou com um extrato de (R${extrato:.2f}).
                            ,ainda possui {numero_saques_restantes} saque(s) restante(s).""")
            else:
                print(f"""Impossivel sacar, nao aceitamos saques maiores
                          que 500 ,seu saque requerido foi R${valor_saque:.2f},
                          ou maiores que o seu extrato (R${extrato:.2f})""")
        else:
            print("Você já gastou todos os 3 saques diarios")
    elif menu in DEPOSITAR:
        valor_deposito=float(input("Quanto deseja depositar?"))
        if valor_deposito>0:
            extrato+=valor_deposito
            print(f"""Voce depositou R${valor_deposito:.2f} e ficou com um extrato de (R${extrato:.2f}).""")
    elif menu in VISUALISAR_EXTRATO:
            print(f"""Seu extrato é de (R${extrato:.2f}).""")
    else:
        print("Acesso encerrado.")
        break
