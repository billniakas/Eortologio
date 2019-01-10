import sqlite3
import re
sqlite_file = 'saints.db'
conn = sqlite3.connect(sqlite_file)

onoma=input("Δώσε όνομα : ")
seek_text=""
c = conn.cursor()
onoma=onoma.capitalize()
c.execute('select *,Month,Day from Saints where Daily_feasts like "%{}%" and source like "saint.gr"'.format(onoma))
all_rows = c.fetchall()
name_list=list(all_rows)
for i in range(len(name_list)):
    date=str(name_list[i][-4])+"/"+str(name_list[i][-5])
    
    for name in name_list[i][0:-5]:
        seektext=name.replace("<b>"," ").replace("</b>"," ")
        
        result=re.findall(r'(.*{}.*)+'.format(onoma), seektext)
    if len(result) == 0:
        pass
    else:
        seek_text="Στις "+date+" γιορτάζει :"
        print(seek_text)
        for i in result:
            print("*",i)
        

    
conn.close()

#print(seek_text)

