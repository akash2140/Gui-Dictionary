from tkinter import *
import sqlite3
from tkinter import messagebox
import os

dictionary=Tk()
dictionary.title("DICTIONARY")

f1=Frame(dictionary)
f1.grid(row=0,column=1)

f2=Frame(dictionary)
f2.grid(row=0,column=3)

f3=Frame(dictionary)
f3.grid(row=0,column=2)

f4=Frame(dictionary)
f4.grid(row=0,column=4)

Label(f3,text=" ").pack(side='top')

Label(f1,text='TYPE WORD HERE : ').pack(side='top')#grid(row=0,column=1)
Label(f2,text='MEANING HERE : ').pack(side='top')#grid(row=0,column=2)

word=Entry(f1,width=20)
word.pack(side='top')#grid(row=1,column=1)

meaning=Text(f2,height=10,width=23)
meaning.pack(side='top')#grid(row=1,column=2)

Label(f1,text=' ').pack(side='top')

search=Button(f1,text='SEARCH',bg='green',width=15,command=lambda:search_meaning())
search.pack(side='top')#grid(row=2,column=1)

clr=Button(f1,text='CLEAR',bg='green',width=15,command=lambda:clear_fields())
clr.pack(side='top')#grid(row=2,column=2)

ins=Button(f1,text='ADD WORD',bg='green',width=15,command=lambda:add_meaning())
ins.pack(side='top')#grid(row=3,column=1)

upd=Button(f1,text='UPDATE MEANING',bg='green',width=15,command=lambda:update_meaning())
upd.pack(side='top')#grid(row=3,column=2)

delete=Button(f1,text='DELETE WORD',bg='green',width=15,command=lambda:delete_meaning())
delete.pack(side='top')#grid(row=4,column=1)

Label(f1,text=' ').pack(side='top')

mainloop()

def clear_fields():
    word.delete(0,'end')
    meaning.delete("1.0",END)

def search_meaning():
    meaning.delete("1.0",END)
    My_dictionary=sqlite3.connect('word_meanings.db')
    dic=My_dictionary.cursor()
    txt=word.get()
    try:
        dic.execute("Select meanings from DICTIONARY_table where words='"+txt+"';")
        record=dic.fetchall()
        meaning.insert(END,record[0][0])
    except:
        messagebox.showinfo("DICTIONARY","SORRY...WORD NOT FOUND")
        word.delete(0,'end')

def add_meaning():
    if len(meaning.get("1.0",END)) in [0,1] or len(word.get())==0:
        print("Hii")
        messagebox.showinfo("DICTIONARY","WORD/MEANING FIELD CAN'T BE EMPTY")
        return
    My_dictionary=sqlite3.connect('word_meanings.db')
    dic=My_dictionary.cursor()
    txt=word.get()
    dic.execute("Select words from DICTIONARY_table where words='"+txt+"';")
    record=dic.fetchall()
    #print(record)
    if len(record)!=0:
        messagebox.showinfo("DICTIONARY","WORD ALREADY EXISTS\nIF YOU WANT TO UPDATE ITS MEANING\nTHEN CLICK UPDATE MEANING")
    else:
        txt2=meaning.get("1.0",END)
        dic.execute("Insert into DICTIONARY_table values(?,?)",(txt,txt2))
        messagebox.showinfo("DICTIONARY","WORD ADDED TO YOUR DICTIONARY SUCCESSFULLY")
        word.delete(0,'end')
        meaning.delete("1.0",END)
        My_dictionary.commit()

def update_meaning():
    if len(meaning.get("1.0",END)) in [0,1] or len(word.get())==0:
        messagebox.showinfo("DICTIONARY","WORD/MEANING FIELD CAN'T BE EMPTY")
        return
    My_dictionary=sqlite3.connect('word_meanings.db')
    dic=My_dictionary.cursor()
    txt=word.get()
    txt2=meaning.get("1.0",END)
    try:
        dic.execute("Update DICTIONARY_table set meanings='"+txt2+"' where words='"+txt+"';")
        My_dictionary.commit()
        messagebox.showinfo("DICTIONARY","MEANING UPDATED")
        word.delete(0,'end')
        meaning.delete("1.0",END)
    except:
        messagebox.showinfo("DICTIONARY","SORRY...MEANING CAN'T BE UPDATED RIGHT NOW")
        My_dictionary.rollback()

def delete_meaning():
    if len(meaning.get("1.0",END)) in [0,1] or len(word.get())==0:
        messagebox.showinfo("DICTIONARY","WORD/MEANING FIELD CAN'T BE EMPTY")
        return
    My_dictionary=sqlite3.connect('word_meanings.db')
    dic=My_dictionary.cursor()
    txt=word.get()
    txt2=meaning.get("1.0",END)
    try:
        dic.execute("delete from DICTIONARY_table where words='"+txt+"';")
        My_dictionary.commit()
        messagebox.showinfo("DICTIONARY","WORD DELETED")
        word.delete(0,'end')
        meaning.delete("1.0",END)
    except:
        messagebox.showinfo("DICTIONARY","SORRY...MEANING CAN'T BE DELETED RIGHT NOW")
        My_dictionary.rollback()

    
