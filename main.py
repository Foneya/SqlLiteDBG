import sqlite3
import os
import random

if os.path.isfile("program.db"):
    con = sqlite3.connect("program.db")
    cur = con.cursor()
    print("Проверка присутствий всех таблиц")
    nameexist = cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='names'")
    if nameexist.fetchone()[0] == 1:
        print("Таблица с именами присутсвует")
    else:
        print("Отсутсует таблица с именами создание...")
        cur.execute("CREATE TABLE names(id INTEGER, name TEXT)")
        con.commit()
    familiaexist = cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='families'")
    if familiaexist.fetchone()[0]== 1:
        print("Таблица с фамилиями присутсвует")
    else:
        print("Таблица с фамилиями отсутствет создание....")
        cur.execute("CREATE TABLE families(id INTEGER, familia TEXT)")
        con.commit()
    jobsexist = cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='jobs'")
    if jobsexist.fetchone()[0] == 1:
        print("Таблица с работами присутствует")
    else:
        mnid = 0
        tstjobs = "Made by Foneya"
        print("Таблица с работами отсутсвует создание......")
        cur.execute("CREATE TABLE jobs(id INTEGER, jobname TEXT)")
        con.commit()
        cur.execute("INSERT INTO jobs (id,jobs) values(?,?)", (mnid,tstjobs))
        con.commit()
    print("Основная база даных была успешно загружена")
else:
    print("File not exist")
    choise = input("Вы хотите создать этот файл?: y/n ")
    if choise == "y" or choise == "н":
        f = open("program.db", "x")
        con = sqlite3.connect("program.db")
        cur = con.cursor()
        fids = "0"
        testname = "Made by Foneya"
        cur.execute("CREATE TABLE names(id INTEGER, name TEXT)")
        cur.execute("CREATE TABLE families(id INTEGER, familia TEXT)")
        cur.execute("CREATE TABLE jobs(id INTEGER, jobname TEXT)")
        cur.execute("insert into names (id ,name) values(?,?)", (fids, testname))
        cur.execute("insert into jobs (id,jobname) values(?,?)",(fids, testname))
        cur.execute("insert into families (id ,familia) values(?,?)", (fids, testname))
        con.commit()
        print("Файл был успешно создан")
        quit("Перезапустите програму чтобы подключить новую базу даных")
    elif choise == "n" or choise == "т":
        quit("Програма не может работать без основной базы даных")
    elif choise != "n" or choise != "y":
        quit("Неопознаная команда")
print("Добро пожаловать в генератор баз даных с именами и фамилиям версия 0.1")
print("Выберите действие")
print("1 - генерация/дополнение базы даных")
print("2 - Измененте базы имен/фамили/работ")
print("3 - Выход")
command = input()
if command == "1":
    filename = input("Введите название файла: ")
    if os.path.isfile(filename + ".db"):
        print("Такой файл уже есть")
        filename = input("Введите название файла: ")
    else:
        f = open(filename + ".db", "x")
        cons = sqlite3.connect(filename + ".db")
        curs = cons.cursor()
        tablescount = input("Введите название таблицы: ")
        curs.execute("CREATE TABLE " + tablescount +"(id INTEGER,name TEXT ,familia TEXT , job TEXT)")
        con = sqlite3.connect("program.db")
        cur = con.cursor()
        idsf = 1
        repeats = input("Сколько человек будет в базе: ")
        repetscount = 1
        while repetscount <= int(repeats):
            nameids = cur.execute("SELECT id FROM names WHERE ID = (SELECT MAX(ID)  FROM names);")
            nameids = cur.fetchone()
            cleannameid = nameids[0]
            namerand = random.randint(1,cleannameid)
            famids = cur.execute("SELECT id FROM families WHERE ID = (SELECT MAX(ID) FROM families);")
            famids = cur.fetchone()
            cleanfamids = famids[0]
            famrand = random.randint(1,cleanfamids)
            famfamilia = cur.execute("SELECT familia FROM families WHERE id =" + str(famrand))
            famfamilia = cur.fetchone()
            cleanfamilia = famfamilia[0]

            namesname = cur.execute("SELECT name FROM names WHERE id =" + str(namerand))
            namesname = cur.fetchone()
            cleanname = namesname[0]
            jobrandmax = cur.execute("SELECT id FROM jobs WHERE ID = (SELECT MAX(ID) FROM jobs);")
            jobrandmax = cur.fetchone()
            clenjobmax = jobrandmax[0]
            jobrandom = random.randint(1,clenjobmax)
            jobsvars = cur.execute("SELECT jobname FROM jobs WHERE id =" + str(jobrandom))
            jobsvars = cur.fetchone()
            cleanjobsvar = jobsvars[0]
            print(cleanname, cleanfamilia, cleanjobsvar)

            curs.execute("INSERT INTO "+tablescount+"(id ,name ,familia ,job) values(?,?,?,?)",(idsf,cleanname,cleanfamilia,cleanjobsvar))
            cons.commit()
            repetscount = repetscount + 1
            idsf = idsf + 1
elif command == "2":
    print("1 - добавить имя в таблицу имён")
    print("2 - добавить фамилию в таблицу фамилий")
    print("3 - добавить работу в таблицу работ")
    razd = input("Выбирите раздел: ")
    if razd == "1":
        activete = True
        con = sqlite3.connect("program.db")
        cur = con.cursor()
        print("Чтобы закончить вводить имена напишите STOP")
        tabids = cur.execute("SELECT id FROM names WHERE ID = (SELECT MAX(ID)  FROM names);")
        tabids = cur.fetchone()
        cleanids = tabids[0]
        while activete == True:
            cleanids = cleanids + 1
            inptname = input("Ведите имя: ")
            if inptname != "STOP":
                cur.execute("insert into names (id ,name) values(?,?)",(cleanids, inptname))
                con.commit()
            else:
                activete = False
    elif razd == "2":
        activete = True
        con = sqlite3.connect("program.db")
        cur = con.cursor()
        print("Чтобы закончить вводить имена напишите STOP")
        tabids = cur.execute("SELECT id FROM families WHERE ID = (SELECT MAX(ID)  FROM families);")
        tabids = cur.fetchone()
        cleanids = tabids[0]
        while activete == True:
            cleanids = cleanids + 1
            inptfam = input("Ведите фамилию: ")
            if inptfam != "STOP":
                cur.execute("insert into families (id ,familia) values(?,?)", (cleanids, inptfam))
                con.commit()
            else:
                activete = False
    elif razd == "3":
        activete = True
        con = sqlite3.connect("program.db")
        cur = con.cursor()
        print("Чтобы закончить вводить имена напишите STOP")
        tabids = cur.execute("SELECT id FROM jobs WHERE ID = (SELECT MAX(ID)  FROM jobs);")
        tabids = cur.fetchone()
        cleanids = tabids[0]
        while activete == True:
            cleanids = cleanids + 1
            inptfam = input("Ведите работу: ")
            if inptfam != "STOP":
                cur.execute("insert into jobs (id ,jobname) values(?,?)", (cleanids, inptfam))
                con.commit()
            else:
                activete = False
    elif razd != "1" or razd != "2" or razd != "3":
        quit("Неправильный код команды")
elif command == "3":
    quit("Выход")
