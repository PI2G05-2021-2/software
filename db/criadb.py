import mysql.connector

class CriaDB():
    mydb = None
    cursordb = None

    def __init__(self):
        pass

    def instanciaDB(self, query,val,comita):

        self.mydb = mysql.connector.connect(
            host =      "127.0.0.1",
            user =      "pi2",
            passwd =    "P.assword123",
            database =  "pi2_db",
        )

        self.cursordb = self.mydb.cursor(dictionary=True)

        if val == None:
            self.cursordb.execute(query)
        else:
            self.cursordb.execute(query,val)
        
        if comita == True:
            self.mydb.commit()
        
    def fechaDB(self):
        self.cursordb.close()
        self.mydb.close()

    def criaTabelas(self):

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            # se não possui base, comenta a linha abaixo para criar uma
            # vai dar erro, descomenta e roda novamente
            database = "pi2_db", 
        )

        self.cursordb = self.mydb.cursor(dictionary=True)

        self.cursordb.execute(
            "CREATE DATABASE IF NOT EXISTS pi2_db"
        )
        
        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            CREATE TABLE IF NOT EXISTS PerfilExtracao (
                idPerfil int NOT NULL PRIMARY KEY,
                temperatura double,
                tempo int,
                potencia double,
                velocidade double
            );""")

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            CREATE TABLE IF NOT EXISTS Usuario (
                login char(15) NOT NULL PRIMARY KEY,
                senha char(15),
                tipo char(1)
            );""")

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            CREATE TABLE IF NOT EXISTS Lote (
                idLote int NOT NULL PRIMARY KEY,
                fk_PerfilExtracao_idPerfil int ,
                fk_Usuario_login2 char(15)
            );""")

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            CREATE TABLE IF NOT EXISTS Comprador (
                idComprador int NOT NULL PRIMARY KEY,
                cpf char(11),
                telefoneComprador char(12),
                nomeComprador char(50),
                cid char(6)
            );""")

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            CREATE TABLE IF NOT EXISTS Medico (
                idMedico int NOT NULL PRIMARY KEY,
                crm char(12),
                telefoneMedico char(12),
                nomeMedico char(50)
            );""")

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            CREATE TABLE IF NOT EXISTS Venda (
                idVenda int NOT NULL PRIMARY KEY,
                fk_medico_idMedico int,
                fk_comprador_idComprador int,
                endereco char(100),
                fk_Usuario_login3 char(15),
                fk_Lote_idLote int
			);
            """
        )
    
        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            ALTER TABLE Lote ADD CONSTRAINT FK_Lote_2
                FOREIGN KEY (fk_PerfilExtracao_idPerfil)
                REFERENCES PerfilExtracao (idPerfil)
                ON DELETE CASCADE;
            """)

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            ALTER TABLE Lote ADD CONSTRAINT FK_Lote_3
                FOREIGN KEY (fk_Usuario_login2)
                REFERENCES Usuario (login)
                ON DELETE CASCADE;
            """)

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            ALTER TABLE Venda ADD CONSTRAINT FK_Venda_2
                FOREIGN KEY (fk_medico_idMedico)
                REFERENCES medico (idMEdico)
                ON DELETE SET NULL;
            """)

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            ALTER TABLE Venda ADD CONSTRAINT FK_Venda_3
                FOREIGN KEY (fk_comprador_idComprador)
                REFERENCES comprador (idComprador)
                ON DELETE SET NULL;
            """)

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            ALTER TABLE Venda ADD CONSTRAINT FK_Venda_4
                FOREIGN KEY (fk_Usuario_login3)
                REFERENCES Usuario (login)
                ON DELETE CASCADE;
            """)

        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()

        self.mydb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "pi2",
            passwd = "P.assword123",
            database = "pi2_db", 
        )
        self.cursordb = self.mydb.cursor(dictionary=True)
        self.cursordb.execute(
            """
            ALTER TABLE Venda ADD CONSTRAINT FK_Venda_5
                FOREIGN KEY (fk_Lote_idLote)
                REFERENCES Lote (idLote)
                ON DELETE CASCADE;
            """
        )
        
        self.mydb.commit()
        self.cursordb.close()
        self.mydb.close()