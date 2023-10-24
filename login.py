import psycopg

class Usuario:
    def __init__(self, login,senha):
        self.login = login
        self.senha = senha

def existe(usuario):
    #abrir a conexao com o PostgeSQL
    with psycopg.connect(
        host='localhost',
        port='5432',
        dbname='2023_pbdi_login_python',
        user='postgres',
        password='123456'
    )as conexao:
        print(conexao)
        #obter um cursor
        with conexao.cursor() as cursor:
        #usando o cursor, executar um comando SELECT
            cursor.execute(
            'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
            (usuario.login, usuario.senha))
        #usando o cursor, verificar o resultado
            resultado = cursor.fetchone()
        #devolve TRUE or FALSE
            return resultado != None
        
def inserir(usuario):
    with psycopg.connect(
        host='localhost',
        port='5432',
        dbname='2023_pbdi_login_python',
        user='postgres',
        password='123456'
    )as conexao:
        print(conexao)
        #obter um cursor
        with conexao.cursor() as cursor:
        #usando o cursor, executar um comando SELECT
            cursor.execute(
            'INSERT INTO tb_usuario WHERE login=%s AND senha=%s',
            (usuario.login, usuario.senha))
        #usando o cursor, verificar o resultado
            resultado = cursor.fetchone()
        #devolve TRUE or FALSE
            return cursor.rowcount >= 1
        

usuario = Usuario('admin','12345')
print(existe(usuario))

def menu():
    texto ='0-Sair\n1-login\n2-Logoff\n'
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input('Digite o login: ')
            senha = input('Digte a senha: ')
            usuario = Usuario(login,senha)
            #exibir usuario ok ou Usuario Nok de acordo com 
            #o metodo existe. Use o operador ternario
            print('Usuario Ok!!!' if existe(usuario) else 'Usuario NOK!!!')
        elif op == 2:
            usuario = None
            print('logoff ok')
        elif op ==3:
            login = input('Digite o login para novo usuario: \n')
            senha = input('Digite a senha para novo usuario: \n')
            novoUsuario = Usuario(login,senha)
            print ("Usuario inserido com sucesso!!!" if inserir(novoUsuario) else 'Usuario não inserido')

        else:
            print('Opção invalida')
    #     op = int(input(texto))
    # else:
menu()
