from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector

#J'ai travalle avec mySql en locale

#connection a ma base de donnee
con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
cursor = con.cursor()
 
#creation de la table etudiant
cursor.execute("""CREATE TABLE IF NOT EXISTS etudiant (
                IdEtudiant INT(11) NOT NULL PRIMARY KEY ,
                IdFiliereFK INT(11) NOT NULL,
                nom VARCHAR(100) NOT NULL, 
                prenom VARCHAR(100) NOT NULL,
                age INT(11) NOT NULL);""")
#creation de la table filiere
cursor.execute("""CREATE TABLE IF NOT EXISTS filiere (
                idFiliere INT(11) NOT NULL PRIMARY KEY ,
                nomFiliere VARCHAR(100) NOT NULL);""")
con.close();

                

def insert() :
    IdEtudiant = e_IdEtudiant.get()
    nom = e_nom.get();
    prenom = e_prenom.get();
    age = e_age.get();
    IdFiliereFK = e_idFiliere.get();
    numfil = filiere.get();
    if numfil == "1":
        nomFiliere ="AF"
    elif numfil == "2":
        numfil ="SE"
    elif numfil == "3":
        nomFiliere ="SD"
    elif numfil == "4":
        nomFiliere ="ROAD"
    elif numfil == "5":
        nomFiliere ="DSE"
    else:
        nomFiliere ="DS"

    if (nom=="" or age=="" or prenom=="" or IdFiliereFK=="" or numfil==""):
        MessageBox.showinfo("Attention !", "Veuillez remplir tous les champs")
    else:
         con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
         cursor = con.cursor()
         cursor.execute("insert into etudiant values('"+ IdEtudiant +"','"+ IdFiliereFK +"','"+ nom +"','"+ prenom +"','"+age+"')")
         cursor.execute("insert into filiere values('"+ IdFiliereFK +"','"+ nomFiliere+"')")
         cursor.execute("commit");

         e_IdEtudiant.delete(0, 'end')
         e_nom.delete(0, 'end')
         e_prenom.delete(0, 'end')
         e_age.delete(0, END)
         e_idFiliere.delete(0, 'end')
         show1()
         show2()
         MessageBox.showinfo("Felicitation !","Informations inserees avec succes");
         con.close();



def delete():  
    
    if(e_IdEtudiant.get() == "" or e_idFiliere.get()==""):
         MessageBox.showinfo("Attention","les ID sont necessaire")
         
    else:
         MessageBox.showinfo("Attention","Etes vous sure de supprimer cet etudiant")
         con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
         cursor = con.cursor()
         cursor.execute("delete from etudiant where IdEtudiant='"+ e_IdEtudiant.get() +"'")
         cursor.execute("DELETE FROM filiere WHERE idFiliere = '"+ e_idFiliere.get() +"'")
         cursor.execute("commit");
         
         e_IdEtudiant.delete(0, 'end')
         e_nom.delete(0, 'end')
         e_prenom.delete(0, 'end')
         e_age.delete(0, END)
         e_idFiliere.delete(0, 'end')
         show1()
         show2()
         MessageBox.showinfo("Felicitation !","Suppression avec succes");
         con.close();
    
         
def update() :
    IdEtudiant = e_IdEtudiant.get();
    nom = e_nom.get();
    prenom = e_prenom.get();
    age = e_age.get();
    IdFiliereFK = e_idFiliere.get();
    numfil = filiere.get();
    if numfil == "1":
        nomFiliere ="AF"
    elif numfil == "2":
        numfil ="SE"
    elif numfil == "3":
        nomFiliere ="SD"
    elif numfil == "4":
        nomFiliere ="ROAD"
    elif numfil == "5":
        nomFiliere ="DSE"
    else:
        nomFiliere ="DS"
   
    if ( nom=="" or prenom=="" or age==""):
        MessageBox.showinfo("Attention !", "Veuillez remplir tous les champs")
    else:
         con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
         cursor = con.cursor()
         cursor.execute("update etudiant set IdFiliereFK='"+IdFiliereFK +"', nom='"+nom +"',prenom='"+prenom +"',age='"+age +"'where IdEtudiant ='"+IdEtudiant +"'")
         cursor.execute("UPDATE filiere SET nomFiliere='"+nomFiliere+"'where idFiliere=+ '"+IdFiliereFK+"'")
         cursor.execute("commit");

         show1()
         show2()
         MessageBox.showinfo("Felicitation !","Modification avec succees");
         con.close ;

         


def get() :
    if(e_IdEtudiant.get() == ""):
      MessageBox.showinfo("Attention","ID est necessaire")
    else:
      con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
      cursor = con.cursor()
      cursor.execute("Select * from etudiant where IdEtudiant='"+ e_IdEtudiant.get() +"'")
      
      rows = cursor.fetchall()

    for row in rows :
       e_idFiliere.insert(0,row[1])
       e_nom.insert(0, row[2])
       e_prenom.insert(0,row[3])
       e_age.insert(0,row[4])
  
    con.close();

def show1():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
    cursor = con.cursor()
    cursor.execute("Select * from etudiant ")
    rows = cursor.fetchall()
    list1.delete(0, list1.size())

    for row in rows :
       insertData = str(row[0]) +'   '+str(row[1]) +'   '+row[2]+'   '+row[3]+'   '+str(row[4])
       list1.insert(list1.size()+1, insertData)

    con.close();

def show2():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="python-tkinter")
    cursor = con.cursor()
    cursor.execute("Select * from filiere ")
    rows = cursor.fetchall()
    list2.delete(0, list2.size())

    for row in rows :
       insertData = str(row[0])+'   '+row[1]
       list2.insert(list2.size()+1, insertData)

    con.close();

#la mise de l'interface
root = Tk()
root.geometry("800x700")
root.title("MiniProjet Bouzouf Chaymae")


photo = PhotoImage(file="insea.png")

canvas = Canvas(root, width=70, height=200)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()


Titre= Label(root, text='Entrez vos Informations :', font=('bold',20))
Titre.place(x=260,y=70)
    
    
Id = Label(root, text=' Id Etudiant :', font=('bold',12))
Id.place(x=280,y=130)

Nom = Label(root, text=' nom :', font=('bold',12))
Nom.place(x=280,y=160)

Prenom = Label(root, text=' prenom :', font=('bold',12))
Prenom.place(x=280,y=190)

Age = Label(root, text=' age :', font=('bold',12))
Age.place(x=280,y=220) ;

idFiliere= Label(root, text=' Id Filiere :', font=('bold',12))
idFiliere.place(x=280,y=260) ;

e_IdEtudiant = Entry()
e_IdEtudiant.place(x=420,y=130)

e_nom = Entry()
e_nom.place(x=420,y=160)

e_prenom = Entry()
e_prenom.place(x=420,y=190)

e_age = Spinbox(root,from_=19 , to=100)
e_age.place(x=420,y=220)

e_idFiliere = Entry()
e_idFiliere.place(x=420,y=260)

insert = Button(root, text="inserer", font=("italic",10),bg="green", command=insert)
insert.place(x=300, y=410)

delete = Button(root, text="supprimer", font=("italic",10),bg="Red", command=delete)
delete.place(x=520, y=410)

update = Button(root, text="modifier", font=("italic",10),bg="yellow", command=update)
update.place(x=450, y=410)

get = Button(root, text="recuperer", font=("italic",10),bg="white", command=get)
get.place(x=370, y=410)

# pour traiter les filieres 
cadre1 = Frame(root, borderwidth=2, relief=GROOVE)
cadre1.place(x=240,y=300)
Label(cadre1, text="choisir une filiere:", font=('bold',11)).pack(padx=10, pady=10)

filiere = StringVar()

AF = Radiobutton(cadre1, text="AF", variable=filiere, value=1)
AF.pack(side= LEFT,padx=10, pady=10)

SE = Radiobutton(cadre1, text="SE", variable=filiere, value=2)
SE.pack(side= LEFT,padx=10, pady=10)

SD = Radiobutton(cadre1, text="SD", variable=filiere, value=3)
SD.pack(side= LEFT,padx=10, pady=10)

ROAD = Radiobutton(cadre1, text="ROAD", variable=filiere, value=4)
ROAD.pack(side= LEFT,padx=10, pady=10)

DSE = Radiobutton(cadre1, text="DSE", variable=filiere, value=5)
DSE.pack(side= LEFT,padx=10, pady=10)

DS = Radiobutton(cadre1, text="DS", variable=filiere, value=6)
DS.pack(side= LEFT,padx=10, pady=10)


#pour afficher les lists des etudiants et les filieres.
Tl1 = Label(root, text='Liste des etudiants :', font=('bold',10))
Tl1.place(x=200,y=460)

Tl2 = Label(root, text='Liste des filieres :', font=('bold',10))
Tl2.place(x=480,y=460) 

list1 = Listbox(root,width=30, height=14)
list1.place(x=200,y=480)
show1()

list2 = Listbox(root,width=30, height=14)
list2.place(x=480,y=480)
show2()

root.mainloop()

