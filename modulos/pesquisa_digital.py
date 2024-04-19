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
        print(f'''
        =================================================
        ======         ESCOLHA UMA OPÇÃO:          ======
        ======                                     ====== 
        ======          (1) - SIM                  ====== 
        ======          (2) - NÃO                  ======
        ======          (3) - NÃO SEI RESPONDER    ======
        ======                                     ======
        =================================================  
        -> ''')
    # Metodo para realizar a pesquisa com o user
    def fazer_pesquisa(self):
        while True:
            idade = int(input('Digite sua idade: '))
            # Caso a idade do user seja 0, o codigo vai parar
            if idade == 0:
                self.df.to_csv('pesquisa_digital.csv', index=False, sep=';')
                print(self.df)
                print("Dados salvos com sucesso em 'pesquisa_digital.csv'")
                break

            # caso não, ele realiza a pesquisa.
            elif idade > 0:
                genero = input('Digite seu gênero: ')
                respostas = []
                for pergunta in self.lista_perguntas:
                    print(pergunta)
                    resposta = int(input(self.menu_pesquisa()))
                    if resposta == 1:
                        resposta = 'SIM'
                        respostas.append(resposta)
                    elif resposta == 2:
                        resposta = 'NÃO'
                        respostas.append(resposta)
                    elif resposta == 3:
                        resposta = 'NÃO SEI RESPONDER'
                        respostas.append(resposta)
                
                # Data e hora que a resposta foi escrita no sistema.
                hora_atual = dt.datetime.now()
                data_hora_resposta = hora_atual.strftime('%d/%m/%Y %H:%M')
                        
                # Criando uma nova linha ao dataFrame
                nova_linha = {'idade': idade, 'genero': genero.upper(), 'resposta_1':respostas[0], 'resposta_2':respostas[1], 'resposta_3':respostas[2], 
                          'resposta_4':respostas[3], 'resposta_5':respostas[4], 'resposta_6':respostas[5], 'data/hora resposta': data_hora_resposta}
                # Adicionando a nova linha ao dataframe.
                self.df = self.df._append(nova_linha, ignore_index=True)