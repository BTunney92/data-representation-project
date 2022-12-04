import dbconfig as cfg

import mysql.connector 

class VoteDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def create(self, values):
        
       cursor = self.getcursor()
       sql="insert into vote (goalname,emailaddress) values (%s,%s)"
       cursor.execute(sql, values)

       self.connection.commit()
       newid = cursor.lastrowid
       self.closeAll()
       return newid
        
    def countvotes(self,goalname):
        
        cursor = self.getcursor()
        sql="select count(*) as votes from vote where goalname like %s"
        values = (goalname, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        count = result[0]
        
        self.closeAll()
        return count
       

    def convertToDictionary(self, result):
        pass
    '''
        colnames=['id','title','author', "price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
       '''
    def createtable(self):
        cursor = self.getcursor()
        sql="create table vote (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, goalname varchar(250), emailaddress varchar(250))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()
        
    
    def createdatase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()
        

voteDAO = VoteDAO()

if __name__ == "__main__":
    voteDAO.createdatase()
    voteDAO.createtable()

    data = ('Diego Maradona Vs England (1986)', "124@gmail.com")
    voteDAO.create(data)
    count = voteDAO.countvotes('Diego Maradona Vs England (1986)')
    print (count)

    print("sanity")