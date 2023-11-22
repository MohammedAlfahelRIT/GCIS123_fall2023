#Group Members: Suhail Ahmed and Mohamed Al Fahel

#the scenarios and what they require which are basically the task dependencies using a shortcut of tdep instead of writing the whole task_dependencies thing each time
#tdep1, tdep2, tdep3, and tdep4 are scenario1, scenario2, scenario3,and scenario4
tdep1={"T1":[],"T2":["T1"], "T3": ["T1","T2"]}
tdep2={"T1":[],"T2":["T1","T3"], "T3": ["T2"]}
tdep3={"T0":[],"T1":[], "T2":["T1"], "T3": ["T2"]}
tdep4={"T1":[],"T2":["T1"],"T3": ["T1","T2"],"T4":["T3"]}

#defining the function to flip whichever scenario provided
def mirror(tdep):
    #d_T is the dependency_tasks
    d_T = {x: [task for task in tdep if x in tdep[task]] for x in sum(tdep.values(), [])}
    return d_T
#you put whichever task dependency you'd like to see in the print function when you write for example tdep1, tdep2, tdep3, or tdep4
#print("tdep1: ",tdep1)
#print("tdep1 mirror: ",mirror(tdep1))

def remove_value(list_tasks,Tx,tdep):
    #removed_dict={task for task in tdep if not Tx tdep[task]}
    
    for T in list_tasks:
        if Tx in tdep[T]:
            tdep[T].remove(Tx)
    return tdep
#print(tdep1)
#print(remove_value(["T2","T3"],"T1",tdep1))

#this function checks if a all the tasks in a key are done, if they are all done the list will be empty
#therefore we can send it to ready list, if it is not ready it is sent to not ready list

def sorter(tdep):
    ready=[]
    notready=[]
    for task in tdep:
        if tdep[task]==[]:
            ready.append(task)
        else:
            notready.append(task)
    return ready, notready
'''''
The schedule function iterates over every task in the list, then it sends 
each task to sorter to see if its dependencies are ready, if they are ready it is sent 
to the schedule.
then the next for loop removes the ready tasks from the other tasks dependencies so that they can be sorted next.
'''''
def schedule(tdep):
    schedule=[]
    notready=[]
    for i in tdep:
        #answer.append(sorter(tdep))
        schedule,notready=sorter(tdep)
    
        for t in schedule:
            #print(t)
            tdep=remove_value(notready,t,tdep)
            #print(tdep)
    if len(schedule)!=len(tdep):
        schedule.clear()
    return schedule


print(schedule(tdep4))