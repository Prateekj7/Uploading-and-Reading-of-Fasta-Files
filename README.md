# Uploading-and-Reading-of-Fasta-Files
Reading Fasta file by uploading it through a GUI made on Tkinter, a python library which is then uploaded to Mysql server for a localhost

Fasta file is a document which contains information about the gene sequence, its location and the whole gene sequence. A gene sequence is altered when there is a disease. So if the sequence is changed, detecting diseases is easier.
In geneparse.py, it is python program for uploading gene sequence to a database, where the coluns are slno, information, gene sequence, count of A , count of T, count of G, count of C and GCPER.
For database i m used XAMPP, where we uploaded in the local host using pymysql package.
Packages used - 
        re(regex) - for understanding regular expressions. So it will be easier to detect them.
        pymysql - for connection to the databse.
        Tkinter - for the gui
