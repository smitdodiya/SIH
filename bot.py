import re
import sqlite3

conn = sqlite3.connect("Botans1.db")
col1 = conn.execute("select pro_id1 from ans")  # id
col2 = conn.execute("select pro_name1 from ans")  # name
col3 = conn.execute("select pro_ans1 from ans")

#ans

def ans_of_user123():

    list1 = []
    new_list1 = []
    new_list2 = []
    new_list3 = []
    list2 = []
    list3 = []

    for i in col1:
        j = list(i)
        list1 = j + new_list1
        new_list1 = list1
# print(new_list1)
    for i in col2:
        j = list(i)
        list1 = j + new_list2
        new_list2 = list1
# print(new_list2)
    for i in col3:
        j = list(i)
        list1 = j + new_list3
        new_list3 = list1
# print(new_list3)
    for i in range(1):
        u_l = []
        print("Bot : What is your fav Subject ?")
        u_in = input('You : ')
        u_in.lower()
        u_l = u_in.split()
    # print(u_l)
        for k in new_list2:
            for j in u_l:
                if k == j:
                    x = new_list2.index(j)
                    print("Bot : ",new_list3[x])



def que_of_user():
    conn = sqlite3.connect("Botans2.db")
    col1 = conn.execute("select pro_id1 from ans")  # id
    col2 = conn.execute("select pro_name1 from ans")  # name
    col3 = conn.execute("select pro_ans1 from ans")

    list1 = []
    new_list1 = []
    new_list2 = []
    new_list3 = []
    list2 = []
    list3 = []

    for i in col1:
        j = list(i)
        list1 = j + new_list1
        new_list1 = list1
    # print(new_list1)
    for i in col2:
        j = list(i)
        list1 = j + new_list2
        new_list2 = list1
    # print(new_list2)
    for i in col3:
        j = list(i)
        list1 = j + new_list3
        new_list3 = list1
    # print(new_list3)
    for i in range(1):
        u_l = []
        u_in = input('You : ')
        u_in=u_in.lower()
        u_l = u_in.split()
        # print(u_l)
        for k in new_list2:
            for j in u_l:
                if k == j:
                    x = new_list2.index(j)
                    print("Bot : ", new_list3[x])
                    from googletrans import Translator
                    languages = {"Hindi": 'hi', "Bengali": 'bn', "Tamil": 'ta', "Telugu": 'tl', "Marathi": 'mr',"Urdu": 'ur', "Kannada": 'kn', "Gujarati": 'gu', "Malayalam": 'ml'}
                    languages_list = ["Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Urdu", "Kannada", "Gujarati","Malayalam"]
                    print(languages_list)
                    y = input("Enter language : ")
                    source_text = new_list3[x]
                    translator = Translator()
                    input1 = languages[y]
                    if y in languages:
                        result = translator.translate(source_text, dest=input1)
                        print(result.text)
                    else:
                        print("This time not avalable this language we will update soon.... ")





print('ask que or give ans ? ')
a = input('You : ')
a = a.lower()
if a == 'ans':
    ans_of_user123()
elif a == 'que':
    que_of_user()
else:
    print("Enter only que or ans Nothing else :)")