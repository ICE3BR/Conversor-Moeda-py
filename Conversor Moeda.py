import requests
import datetime
import textwrap

def cotacao_moeda(moeda_origem, moeda_destino):
    # Faz os textos do input de moedas ficar Maiusculas (para evitar do usuário escrever errado)
    moeda_origem_up = moeda_origem.upper()
    moeda_destino_up = moeda_destino.upper()
    moeda_junção = moeda_origem_up+moeda_destino_up

    # site: https://docs.awesomeapi.com.br/
    # API que faz a cotação das moedas
    link = (f"https://economia.awesomeapi.com.br/json/last/{moeda_origem_up}-{moeda_destino_up}")
    requisicao = requests.get(link)

    # Verificador - Se o retorno for True ou False
    if requisicao.status_code == 200: # 200 - é um código de requisições padrão da internet que retorna True
        cotacao = (requisicao.json()[moeda_junção]["bid"])
        return float(cotacao)
    else: # 404 - Código de Erro web padrão da internet que retorna False
        print("@@@ ERRO: Moeda não aceita @@@")
        return False

def conversor_moeda(valor, cotacao):
    if valor > 0:
        resultado = float(valor) * cotacao
        return resultado
    else:
        print("@@@ ERRO: Valor inválido @@@" )
        return False

def menu():
    menu = """\n\t<====== MENU ======>
[1] - Infomar a cotação da moeda
[2] - Converter Valor especifico
[0] - Sair
=>> """
    return input(textwrap.dedent(menu))

def menu_moedas():
    return f"""
[ CÓDIGO DA MOEDA |\t\tNOME\t\t]
- \tUSD\t  | Dólar Americano
- \tBRL\t  | Real Brasileiro
- \tEUR\t  | Euro
{"="*60}
"""

def main():
    date = datetime.datetime.now()
    data = date.strftime("%d-%m-%Y|%H:%M")

    print("\nBem-vindo ao Conversor de Moedas!")

    while True:
        opcao = menu()
        if opcao == "1":
            print("===< Cotação de Hoje >===")
            print(f"Data: {data}")
            print(menu_moedas())
            moeda_origem = input("Selecione a moeda de origem: ")
            moeda_destino = input("\nSelecione a moeda de destino: ")
            if moeda_origem and moeda_destino:
                converter = cotacao_moeda(moeda_origem, moeda_destino)
                print(f"\nA cotação da moeda está no valor: {converter:.2f}\n")
            else:
                print("@@@ Você não digitou as moedas de origem ou destino. @@@")
                print("Tente Novamente")
            
        elif opcao == "2":
            print("===< Conversor De Moedas >===")
            print(f"Data: {data}")
            print(menu_moedas())
            while True:
                moeda_origem = input("DE: ")
                moeda_destino = input("PARA: ")
                cotacao = cotacao_moeda(moeda_origem, moeda_destino)
                while True:
                    valor = input("Valor para conversão: ")
                    converter = conversor_moeda(float(valor), cotacao)
                    if converter:
                        print(f"\nO valor será: {converter:.2f}\n")
                        return main()

        elif opcao == "0":
            print("Saindo do Conversor de Moedas!")
            break
        else:
            print("Opção inválida, tente novamente!")

main()