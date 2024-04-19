import pandas as pd
import datetime as dt

class PesquisaDigital:
    def __init__(self):
        # Criando dataFrame vazio
        self.df = pd.DataFrame()
        # Lista das perguntas para o user
        self.lista_perguntas = [
            'Você acredita que a falta de acesso à tecnologia contribui para a desigualdade social no Brasil?',
            'Você acredita que o custo dos serviços de internet e telecomunicações é acessível para a maioria da população brasileira?',
            'Você acredita que as empresas de tecnologia têm um papel significativo na redução da desigualdade social no Brasil?',
            'Você acha que a internet de alta velocidade está disponível para todas as classes sociais no Brasil?',
            'Você acha que todos têm acesso igual à educação digital no Brasil?',
            'Você acha que o governo está fazendo o suficiente para reduzir a diferença no acesso à tecnologia?'
        ]

    # Metodo para mostrar o meunu pardão.
    def menu_pesquisa(self):
        return f'''
        =================================================
        ======         ESCOLHA UMA OPÇÃO:          ======
        ======          (1) - SIM                  ====== 
        ======          (2) - NÃO                  ======
        ======          (3) - NÃO SEI RESPONDER    ======
        =================================================  
        -> '''
    # Metodo para realizar a pesquisa com o user
    def fazer_pesquisa(self):
        while True:
            lista_respostas = [] 

            try:
                idade = int(input('Digite sua idade (ou 0 para sair): '))
                # Caso a idade seja igual a Zero, o código para.
                if idade == 0:
                    self.df.to_csv('pesquisa_digital.csv', index=False, sep=';')
                    print(self.df)
                    print("Dados salvos em 'pesquisa_digital.csv'")
                    break
                # caso a variável idade seja maior que zero
                elif idade > 0:
                    genero = input('Digite a inicial do seu gênero: ')
                    while genero not in ['M','m','F','f','O','o']:
                        print('Por favor, digite somente a inicial do seu gênero: ')
                        genero = input('Digite seu gênero: ')

                    for pergunta in self.lista_perguntas:
                        print(pergunta)
                        resposta = int(input(self.menu_pesquisa()))
                        # while que verifica se na variável resposta existem algum dos int abaixo (1,2 ou 3)
                        while resposta not in [1, 2, 3]:
                            print('Por favor, escolha uma opção válida.')
                            print(pergunta) # Repete a pergunta
                            resposta = int(input(self.menu_pesquisa()))

                        # Realiza a verificação do do valor que a variável 'resposta' recebeu e adiciona ao DataFrame.
                        if resposta == 1:
                            resposta = 'SIM'
                            lista_respostas.append(resposta)
                        elif resposta == 2:
                            resposta = 'NAO'
                            lista_respostas.append(resposta)
                        elif resposta == 3:
                            resposta = 'NAO SEI RESPONDER'
                            lista_respostas.append(resposta)

            
                                
                # Cria uma variável que armazena a data e hora em que a resposta foi armazenada no DataFrame
                hora_atual = dt.datetime.now()
                data_hora_resposta = hora_atual.strftime('%d/%m/%Y %H:%M')
                        
                # Criando uma nova linha ao dataFrame
                nova_linha = {'idade': idade, 'genero': genero.upper(), 'resposta_1':lista_respostas[0], 'resposta_2':lista_respostas[1], 'resposta_3':lista_respostas[2], 
                          'resposta_4':lista_respostas[3], 'resposta_5':lista_respostas[4], 'resposta_6':lista_respostas[5], 'data/hora resposta': data_hora_resposta}
                # Adicionando a nova linha ao dataframe.
                self.df = self.df._append(nova_linha, ignore_index=True)

            except ValueError:
                print('Por favor, digite apenas números!')