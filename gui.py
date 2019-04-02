# import Tkinter
#from Tkinter import *
from tkinter import *
from tkinter import messagebox as tkMessageBox
#import tkMessageBox
from tkinter import filedialog as tkFileDialog
import re

top = Tk()

def dialogueBox():
    top.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    #tkMessageBox.showinfo( "MESSAGE", "FILE UPLOADED SUCCESSFULLY")
    func(top.filename)

# def parsegeneinfo(f,slno,mygene):
#     geneinfo = mygene.split('\n',1)
#     geneinfo[1] = geneinfo[1].replace('\n', '')
#     x = re.findall("[^ATGC]",geneinfo[1])
#     if(x):
#         tkMessageBox.showinfo( "MESSAGE", "ERROR")
#     else:
#         writetofile(f,str(slno),geneinfo[0],geneinfo[1])

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
# def writetofile(file,str1,str2,str3):
#     file.write(str1 + '\t\t\t\t\t\t\t\t\t\t\t' + str2 + '\t\t\t\t\t\t\t\t\t' + str3 + '\n')


def func(filename):
    file = open(filename,'r')
    genefile = file.read()
    singlegenes = genefile.split('>')
    i = 1
    name = input("What should be the output filename? ")
    #filemenu.add_command(label="Save", command=file_save(singlegenes))
    f = open(name,"w")
    f.write("Sl.no\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInfo\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGene\n")
    for i in range(1,len(singlegenes)):
        parsegeneinfo(f,i,singlegenes[i])
    tkMessageBox.showinfo( "MESSAGE", "FILE UPLOADED SUCCESSFULLY")
    f.close
    #top.config(menu=menubar)


#def file_save(singlegenes):
#    name=asksaveasfile(mode='w',defaultextension=".txt")
#    f = open(name,"w")
#    f.write("Sl.no\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInfo\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tGene\n")
#    i=1
#    for i in range(1,len(singlegenes)):
#        parsegeneinfo(f,i,singlegenes[i])


#menubar=Menu(top)
#filemenu=Menu(menubar,tearoff=0)

w = Label(text='GENE VALIDATOR')
w.config(font=("GENE VALIDATOR",30))
w.config(width=200)

B = Button(text ="UPLOAD FILE", width=25 , bg='red' , command = dialogueBox)

w.pack(pady=50)
B.pack()
top.mainloop()
