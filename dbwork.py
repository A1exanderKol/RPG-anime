import sqlite3
import levels

con = sqlite3.connect('date.db')
crs = con.cursor()
crs.execute("""CREATE TABLE IF NOT EXISTS 'users'('id' INTEGER PRIMARY KEY AUTOINCREMENT, 'exp' INTEGER, 'level' INTEGER)""")


def strt (id):
    if id not in crs.execute("""SELECT 'id' FROM 'users'""").fetchall():
        crs.execute(f"""INSERT INTO 'users' ('id', 'exp', 'level') VALUES ('{id}',0,0)""")
        crs.execute(f"""CREATE TABLE '{id}' ('№' INTEGER PRIMARY KEY, 'name' TEXT, 'epesods' INTEGER, 'exp' INTEGER)""")
    con.commit()


def wtch (id,name,epesods,exp):
    crs.execute(f"""INSERT INTO '{id}' ('name','epesods','exp') VALUES ('{name}','{epesods}',{exp})""")
    con.commit()




def shw (id):
    con = sqlite3.connect('date.db')
    crs = con.cursor()
    crs.execute(f"""SELECT * FROM '{id}'""")
    all = crs.fetchall()
    with open (f'{id}.txt', 'w') as f:
        f.write('№  Name  epesods  exp'+'\n')
        for i in all:
            i=str(i)
            i = i.replace('(','')
            i = i.replace(')', '')
            i = i.replace("'", '')
            i = i.replace(',', ' ')
            f.write(i+'\n')
    with open(f'{id}.txt', 'r') as f:
        ans=''.join(f.readlines())
    con.commit()
    con.close()
    return ans

def prf(id):
    con = sqlite3.connect('date.db')
    crs = con.cursor()
    e = list(crs.execute(f"""SELECT * FROM 'users' WHERE id ={id}""").fetchone())
    del(e[0])
    con.commit()
    con.close()
    return e 


def l_e_v (id, exp):
    con = sqlite3.connect('date.db')
    crs = con.cursor()
    e,l=prf(id)
    e,l=levels.lev(e,l,exp)
    crs.execute(f"""UPDATE users SET exp ={e}, level ={l}   WHERE id = {id} """)
    con.commit()
    con.close()

