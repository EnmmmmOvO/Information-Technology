import sqlite3


### Database connection ###
def queryPlayer(sql, values=None):
    conn = sqlite3.connect("./week3.db")
    curr = conn.cursor()

    try:
        res = curr.execute(sql).fetchall()
    except:
        print("Broken SQL")
        curr.close()
        return None

    conn.commit()
    curr.close()
    conn.close()

    if len(res) == 0:
        return []
    else:
        return res



def listUsers():
    # TODO 
    return


def getUser(username, password):
   # TODO
   return
  

def add_user(user_record):
    # TODO 
    return
