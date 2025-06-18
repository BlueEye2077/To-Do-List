from pyfiglet import figlet_format as ff
import os,sqlite3,sys
from termcolor import colored
from emoji import emojize
from random import randint


def get_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(__file__)

app_path= get_path()

db=sqlite3.connect(os.path.join(app_path,"data.db"))
print(app_path,"/data.db")
cr=db.cursor()
cr.execute("create table if not exists Tasks (id integer,Task string,Status bool) ")

def saving():
    db.commit()
    
def prog_name():
    abs_path=os.path.abspath(__file__)
    programm=os.path.basename(abs_path)
    print(ff(programm[0:programm.index(".py")].title()))

def Show_Tasks():
    global empty
    global tasks_length
    cr.execute("select task,status from Tasks")
    tasks=cr.fetchall()
    tasks_length=len(tasks)
    if len(tasks)==0:
        print("The To Do List Is Empty :(")
        empty=False    
    else:
        for num,task in enumerate(tasks):
            if task[1]==False:
                print(f"{num+1}-{task[0]} => {emojize(":hourglass_not_done:")}")
            else:
                print(f"{num+1}-{task[0]} => {emojize(":check_mark:")}")
        empty=True
        
def Add_Task():
    cr.execute("select id from tasks")
    ids=cr.fetchall()
    add=input("Enter The New Task:").title()
    if bool(ids)==False:
        new_id=1
    else:
        new_id=max(ids)[0]+1
    cr.execute("insert into Tasks values(?,?,?)" ,(new_id,f"{add}",False))
    print(colored("Task Added.","green"))
    saving()

def Update_Task():
    Show_Tasks()
    ut=False
    if empty==True:
        while ut==False:
            try:
                update_answer=int(input("Enter The Number Of The Task You Want To Update:"))
                while update_answer>tasks_length:
                    print("The Input Is Our Range:")
                    update_answer=int(input("Enter The Number Of The Task You Want To Update:"))
            except ValueError:
                print("Please Enter A Number")
            except :
                print("Error Happend")
            else:
                updated_task=input("Enter The Updated Task:").title()
                cr.execute(f"select id from tasks limit 1 offset {update_answer-1}")
                selected_id=cr.fetchone()[0]
                cr.execute(f"update tasks set task = '{updated_task}' where id = {selected_id}")
                print(colored("Task Updated.","green"))
                ut=True
    else:
        pass

    saving()

def Delete_Task():
    Show_Tasks()
    dt=False
    if empty==True:
        while dt==False:
            try:
                delete_answer=int(input("Enter The Number Of The Task You Want To Delete:"))
                while delete_answer>tasks_length:
                    print("The Input Is Our Range:")
                    delete_answer=int(input("Enter The Number Of The Task You Want To Delete:"))
            except ValueError:
                print("Please Enter A Number")
            except:
                print("Error Happend")
            else: 
                cr.execute(f"select id from tasks limit 1 offset {delete_answer-1}")
                selected_id=cr.fetchone()[0]
                cr.execute(f"delete from tasks where id = {selected_id}")
                print(colored("Task Deleted.","green"))
                dt=True
    else:
        pass
    saving()
     
def Mark():
    Show_Tasks()
    mt=False
    if empty==True:
        while mt==False:
            try:
                mark_answer=int(input("Enter The Number Of The Task You Want To Mark As Compelted:"))
                while mark_answer>tasks_length:
                    print("The Input Is Our Range:")
                    mark_answer=int(input("Enter The Number Of The Task You Want To Mark As Compelted:"))                
            except ValueError:
                print("Please Enter A Number")
            except:
                print("Error Happend")
            else: 
                cr.execute(f"select id,status from tasks limit 1 offset {mark_answer-1}")
                selected_id=cr.fetchone()
                if selected_id[1]==False:
                    cr.execute("update tasks set status=? where id =?",(True,selected_id[0]))
                    print("Task Marked As Completed.")
                else:
                    cr.execute("update tasks set status=? where id =?",(False,selected_id[0]))
                    print("Task Marked As Incompleted.")
                mt=True
    else:
        pass
    saving()

prog_name()
x=False
hub='''1-Show Tasks
2-Add Task
3-Mark As Completed
4-Update Task
5-Delete Task
6-Exit
Enter The Wanted Option=>'''

options=["1","2","3","4","5","6","Show","Add","Mark","Update","Delete","Exit","S","A","M","U","D","E"]

while x==False:
    hub_answer=input(hub).title()
    print("="*80)
    if hub_answer in options:
        if hub_answer=="1" or "Show" in hub_answer or hub_answer=="S":
            Show_Tasks()
            print("="*80)
        elif hub_answer=="2" or "Add" in hub_answer or hub_answer=="A":
            Add_Task()
            print("="*80)
        elif hub_answer=="3" or "Mark" in hub_answer or hub_answer=="M":
            Mark()
            print("="*80)
        elif hub_answer=="4" or "Update" in hub_answer or hub_answer=="U":
            Update_Task()
            print("="*80)
        elif hub_answer=="5" or "Delete" in hub_answer or hub_answer=="D":
            Delete_Task()
            print("="*80)
        elif hub_answer=="6" or "Exit" in hub_answer or hub_answer=="E":
            x=True
            db.close()
    else:
        print("Please Enter A Valid Option:")
        print("="*80)

