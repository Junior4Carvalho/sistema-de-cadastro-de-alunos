from datetime import date
import mysql.connector
from time import sleep

from numpy import intp
conectar = mysql.connector.connect(
    host='localhost', 
    database='cadastro_db', 
    user='root', 
    password='')

if conectar.is_connected():
    print('Conectado com sucesso')
    cursor = conectar.cursor()
    primeiro_nome = input('primeiro nome: ')
    segundo_nome = input('segundo nome: ')
    numero_de_aluno = int(input('numero de aluno: '))
    telefone = int(input('numero de telefone: '))
    numero_do_aluno = int(input('numero do aluno: '))
    data_de_aniversario = int(input('data de aniversario: '))
    classe = int(input('classe: '))
    cidade = input('cidade: ')
    bairro = input('bairro: ')
    sala = int(input('sala: '))
    notas_1 = int(input('notas_1: '))
    notas_2 = int(input('notas_2: '))
    notas_3 = int(input('notas_3: '))
    media_final = notas_1 + notas_2 + notas_3 / 3
    
    sql = """INSERT INTO alunos (alunos_id, 
                                primeiro_nome,
                                segundo_nome, 
                                numero_de_aluno, 
                                telefone, 
                                numero_do_aluno, 
                                data_de_aniversario, 
                                classe, 
                                cidade, 
                                bairro,
                                sala,
                                notas_1,  
                                notas_2,  
                                notas_3,  
                                media_final ) 
                                VALUES ("default",
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}", 
                                "{}",  
                                "{}")
                                """.format(
                                primeiro_nome, 
                                segundo_nome, 
                                numero_de_aluno,
                                telefone,
                                numero_do_aluno,
                                data_de_aniversario,
                                classe,
                                cidade,
                                bairro,
                                sala,
                                notas_1,
                                notas_2,
                                notas_3,
                                media_final
                                )
    
    cursor.execute(sql)
    conectar.commit()

    cursor.close()
    conectar.close()
    sleep(1)

    print('Conexão Encerrada')
   
else:
    print('ERRO!')