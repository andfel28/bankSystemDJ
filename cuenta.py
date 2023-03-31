import cx_Oracle

class Cuenta:
    def __init__(self,p_idOwner):
      try:
                #or:Oracle, pos:Postgres, my:mysql

                self.idOwner = p_idOwner
                self.crearConexion('or')

                #Se crea cursor para ejecutar SQL              ---
                self.cursor = self.connection.cursor()

                # Trae el idCuenta del usuario, suponemos que solo puede tener una cuenta por el momento
                self.cursor.execute(f"SELECT idCue FROM CUENTA WHERE idOwnerCue = {p_idOwner} and ROWNUM=1")
                rows = self.cursor.fetchall()
                self.idCue = rows[0][0]

                # Trae el balance actual de la cuenta (se necesita para GET y POST) -> Queda fuera del if
                self.cursor.execute(f"SELECT BALANCE FROM CUENTA WHERE idCue = {self.idCue}")
                rows = self.cursor.fetchall()
                self.balance = rows[0][0]
      except:
          pass

    def getName(self):
        self.cursor.execute(f"SELECT nameOwner FROM owner_cue WHERE idOwner = {self.idOwner}")
        rows           = self.cursor.fetchall()
        self.nameOwner = rows[0][0]

    def getInscritas(self):
        self.cursor.execute(f"select idCueHijo from inscritas_cue WHERE idCuePadre={self.idCue}")
        self.inscritas = self.cursor.fetchall()

    def closeBD(self):
       try:
          self.connection.close()
       except:
          pass

    def crearConexion(self,option):

       if option == 'or':
               self.connection =  cx_Oracle.connect(
               user='system',
               password='Su1382filter',
               dsn='localhost:1521/orcl',  # Data Source Name
               encoding='UTF-8'
           )

    def transferencia(self,p_valor,p_destino):
        try:
            # Realizamos ambas actualizaciones en cuenta Destino y Origen como una sola transacción.
            self.cursor.execute(f"UPDATE CUENTA SET balance= balance - {p_valor} WHERE idCue={self.idCue}")
            self.cursor.execute(f"UPDATE CUENTA SET balance= balance + {p_valor} WHERE idCue={p_destino}")
            # Commit
            self.connection.commit()
        except:
            self.connection.rollback()