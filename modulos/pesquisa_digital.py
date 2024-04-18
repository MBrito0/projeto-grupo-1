import pandas as pd
import datetime as dt

class PesquisaDigital:
    def __init__(self):
        #Lista para armazenar as respostas do user
        self.respostas = []
        # Lista das perguntas para o user
        self.lista_perguntas = [
            'Você acredita que a falta de acesso à tecnologia contribui para a desigualdade social no Brasil?',
            'Você acredita que o custo dos serviços de internet e telecomunicações é acessível para a maioria da população brasileira?',
            'Você acredita que as empresas de tecnologia têm um papel significativo na redução da desigualdade social no Brasil?',
            'Você acha que a internet de alta velocidade está disponível para todas as classes sociais no Brasil?',
            'Você acha que todos têm acesso igual à educação digital no Brasil?',
            'Você acha que o governo está fazendo o suficiente para reduzir a diferença no acesso à tecnologia?'
        ] 
    # Metódo para mostrar o menu padrão.
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

    # Metódo para realizar a pesquisa com o user
    def fazer_pesquisa(self):
        while True:
            try:
                idade = int(input('Digite sua idade: '))
                # Caso a idade do user seja 0, o codigo vai parar
                if idade == 0:
                    if not self.respostas:
                        print('Nenhuma pesquisa realizada.')
                    else:
                        df = pd.DataFrame(self.respostas)
                        df.to_csv('pesquisa_digital.csv', index=False)
                        print(df)
                        print("Dados salvos com sucesso em 'pesquisa_digitalcsv'")
                    break

                # Caso não, ele realiza a pesquisa.
                elif idade > 0:
                 genero = input('Digite seu gênero: ')
                 respostas = {}
                 for i, pergunta in enumerate(self.lista_perguntas):
                     print(pergunta)
                     resposta = input(self.menu_pesquisa())
                     while resposta not in ['1', '2', '3']:
                         print('Por favor, escolha uma opção válida.')
                         print(pergunta) # Repete a pergunta
                         resposta = input(self.menu_pesquisa())
                     if resposta == 1:
                         resposta = 'SIM'
                     elif resposta == 2:
                         resposta = 'NAO'
                     elif resposta == 3:
                        resposta = 'NAO SEI RESPONDER'
                     respostas[f'resposta_{i+1}'] = resposta
                respostas['idade'] = idade
                respostas['genero'] = genero.upper()
                
                # Data e hora que a resposta foi escrita no sistema.
                hora_atual = dt.datetime.now()
                data_hora_resposta = hora_atual.strftime('%d/%m/%Y %H:%M')
                respostas['data_hora_resposta'] = data_hora_resposta

                self.respostas.append(respostas)

            except ValueError:
                print('Por favor, digite uma idade válida')

if __name__ == '__main__':
    pesquisa = PesquisaDigital()
    pesquisa.fazer_pesquisa()