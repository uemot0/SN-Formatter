import time
import webbrowser
import sys
import threading

def inserir_virgulas(numero):
    numero = str(numero)[::-1]
    numero_com_virgulas = ','.join(numero[i:i+9] for i in range(0, len(numero), 9))
    return numero_com_virgulas[::-1]

def animacao_carregamento():
    animation = "|/-\\"
    for i in range(12):
        time.sleep(0.25)
        sys.stdout.write("\r" + animation[i % len(animation)] + " ")
        sys.stdout.flush()

print("Formatador de SN para atualização Salesforce")
print("1. Copie os numeros das notas e inpute aqui")
print("2. Espere o programa formatar da maneira correta pra inserir no Saleforce.")
print("3. Após a inserção e formatação o programa ira abrir o Salesforce para a edição.\n")
print("Por favor insira os numeros a seguir:")

while True:
    numero = input()
    if numero.lower() == 'sair':
        break
    else:
        print("\nFormatando")
        thread = threading.Thread(target=animacao_carregamento)
        thread.start()
        time.sleep(3)
        thread.join()
        numero_formatado = inserir_virgulas(numero)
        grupos = numero_formatado.split(',')
        for i in range(0, len(grupos), 100):
            print("\nGrupo " + str(i//100 + 1) + " (" + str(len(grupos[i:i+100])) + " SN's): " + ','.join(grupos[i:i+100]))
            if i > 0 and i % 100 == 0:
                print("\nSe encontrar dificuldades ao assimilar mais de um grupo no report, acesse: https://help.salesforce.com/s/articleView?id=sf.filter_logic.htm&type=5")
                confirmacao = input("\nConfirma a leitura para prosseguir (s/n): ")
                if confirmacao.lower() != 's':
                    break
        print("\nDone! Abrindo o relatório Salesforce")
        thread = threading.Thread(target=animacao_carregamento)
        thread.start()
        time.sleep(3)
        thread.join()
        print("\n")
        webbrowser.open('https://voithhydro.lightning.force.com/lightning/r/Report/00O7U000001GlW8UAK/edit')
        print(f"{numero_formatado.count(',') + 1} SN's formatadas")
        print("Formatador feito por Pedro Aufieri, qualquer dúvida me procure no Microsoft Teams.")
        print("Open Source: https://github.com/uemot0/SN-Formatter")
        fechar = input("Deseja fechar o programa? (s/n): ")
        if fechar.lower() == 's':
            break
