import pymysql
import re
from tkinter import *
from tkinter import messagebox as tkMessageBox
#import tkMessageBox
from tkinter import filedialog as tkFileDialog
#import Tkinter, Tkconstants, tkFileDialog

root = Tk()     # tkinter class imported, creates blank window, constructor in this class

# tframe = Frame(root)
# tframe.pack() # gives 1 invisible rectangle or container
# bframe = Frame(root)
# bframe.pack(side=BOTTOM)a


def dialogueBox():
    root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    #tkMessageBox.showinfo( "MESSAGE", "FILE UPLOADED SUCCESSFULLY")
    func(root.filename)


info = ""
gene = ""
counterA = 0
counterT = 0
counterG = 0
counterC = 0
gcper = 0
sql = 0

def parsegeneinfo (f , slno, mygene):
    geneinfo = mygene.split('\n', 1)
    geneinfo[1] = geneinfo[1].replace('\n', '')
    x = re.findall("[^ATGC]", geneinfo[1])

    info = geneinfo[0]
    gene = geneinfo[1]
    counterA = geneinfo[1].count('A')
    counterT = geneinfo[1].count('T')
    counterG = geneinfo[1].count('G')
    counterC = geneinfo[1].count('C')
    addGC = counterG + counterC
    addATGC = counterG + counterC + counterT + counterA
    gcper = float(addGC) / float(addATGC) * 100

    if x:
        print("Error\n")
    else:
        writetofile(f, slno, geneinfo[0], geneinfo[1], counterA, counterT, counterG, counterC, gcper)



def writetofile(file, str0, str1, str2, str3, str4, str5, str6, str7):
    file.write(str(str0) + '\t' + str1 + '\t' + str2 + '\t' + str(str3) + '\t' + str(str4) + '\t' + str(str5) + '\t' + str(str6) + '\t' + str(str7) + '\n')

def func(filename):
    file = open(filename, 'r')
    genefile = file.read()
    singlegenes = genefile.split('>')
    i = 1
    name = input("What should be the output filename? ")
    f = open(name, "w")
    f.write("Slno\tInfo\tGene\tcounterA\tcounterT\tcounterG\tcounterC\tgcper\n")
    for i in range(1, len(singlegenes)):
        parsegeneinfo(f, i, singlegenes[i])
    tkMessageBox.showinfo("MESSAGE", "FILE UPLOADED SUCCESSFULLY")


one = Label(root, text="Software Engineering Project", bg="cyan", fg="black")
one.grid(row=1, columnspan=10)
label_1 = Label(root, text="Enter file name: ")
entry_1 = Entry(root)
label_1.grid(row=10)
entry_1.grid(row=10, column=1)
button_1 = Button(root, text="UPLOAD FILE", fg="green")
button_1.grid(row=11, column=1)
label_2 = Label(root, text="OR")
label_2.grid(row=13, sticky=E)
button_2 = Button(root, text="CHOOSE FROM DEVICE", fg="green", width=25, command=dialogueBox())
button_2.grid(row=14, column=1, sticky=E)
# button1.pack(side=TOP)


root.mainloop()     #running infinitely


#SQL COMMAND START
# f = open(name, "r")
# fstring = f.read()
# 
# flist = []
# for line in fstring.split('\n'):
#     flist.append(line.split('\t'))
# 
# 
# # Open database connection
# db = pymysql.connect("localhost", "cse", "se123project", "genevalidation")
# 
# # prepare a cursor object using cursor() method
# cursor = db.cursor()
# 
# cursor.execute("DROP TABLE IF EXISTS SEPROJECT")
# 
# Slno = flist[0][0]; Info = flist[0][1]; Gene = flist[0][2]; counterA = flist[0][3]; counterT = flist[0][4]; counterG = flist[0][5]; counterC = flist[0][6]; gcper = flist[0][7]
# 
# query = """CREATE TABLE SEPROJECT(
#         {} int not null,
#         {} varchar(255) not null,
#         {} text not null,
#         {} int,
#         {} int,
#         {} int,
#         {} int,
#         {} int
#         )""".format(Slno, Info, Gene, counterA, counterT, counterG, counterC, gcper)
# 
# 
# cursor.execute(query)
# 
# 
# del flist[0]
# 
# rows = ''
# for i in range(len(flist) - 1):
#     rows += "('{}', '{}','{}','{}','{}','{}', '{}', '{}')".format(flist[i][0], flist[i][1], flist[i][2], flist[i][3], flist[i][4], flist[i][5], flist[i][6], flist[i][7])
#     if i != len(flist) - 2:
#         rows += ','
# 
# sql = "INSERT INTO SEPROJECT VALUES" + rows
# 
# try:
#     # Execute the SQL command
#     cursor.execute(sql)
#     # Commit your changes in the database
#     db.commit()
# except:
#     # Rollback in case there is any error
#     db.rollback()
# 
# # disconnect from server
# db.close()
