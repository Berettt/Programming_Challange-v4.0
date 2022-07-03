import math
import time
import sys
global Init

def task1():
    task_val = input('(task1;print) ')
    print(task_val)

def task2():
    print('Type in two values and arithemtic operator(*,+,-,/)')
    task_math = int(input('(task2;calculate;type in the first value) '))
    task_math2 = int(input('(task2;calculate;type in the second value) '))
    task_math3 = input('(task2;calculate;type in arithemtic operator) ')
    if task_math3 == '*':
        score = task_math*task_math2
        print(f"The output is {score}")
    if task_math3 == '+':
        score = task_math+task_math2
        print(f"The output is {score}")
    if task_math3 == '-':
        score = task_math-task_math2
        print(f"The output is {score}")
    if task_math3 == '/':
        score = task_math/task_math2
        print(f"The output is {score}")

def task3():
    print('Type in counts')
    task_count = int(input('(task3;count) '))
    for tasks in range(task_count+1):
        time.sleep(0.4)
        print(tasks)


def Main():
    print('initating..')
    time.sleep(1)
    print('adding jobs...')
    print()
    taskk = input('What task do you need? 1 for printing, 2 for simple calculator, 3 for counting from 0-n, 4 for exit the program: ')
    tasks = 1
    if taskk == '1':
        task1()
            
    if taskk == '2':
        task2()

    if taskk == '3':
        task3()
    if taskk == '4':

      sys.exit()


        
    if taskk != '1' and taskk != '2' and taskk != '3' and taskk != '4':
        print('invalid task, try again')

    print(f'Finished tasks: {tasks} of {Init}')
 #   taskk = input('What next task do you need? 1 for printing, 2 for simple calculator, 3 for counting from 0-n, 4 for exit the program and finishing the tasks, 5 for add new task: ')
    for n in range(Init-1):
        taskk = input('What next task do you need? 1 for printing, 2 for simple calculator, 3 for counting from 0-n, 4 for exit the program: ')
        if taskk == '1':
             task1()
             thr = 'one'
            
        if taskk == '2':
             task2()
             thr = 'two'

        if taskk == '3':
             task3()

        if taskk == '4':
            
            break

        tasks+=1
        print(f'Finished tasks: {tasks} of {Init}')


        

#Welcome
Nickname = input('Ahoj, please enter your name/nickname: ')
print(f'Hello and welcome {Nickname} to the My Task Queue')

while True:
    Init = int(input('How many tasks do you need?: '))

    #if Init != 'Y' and Init != 'N':
     #   print('please enter only letter "Y" or "N"!')

    #if Init == 'N':
       # print(f'Thank you for the time and have a good day {Nickname}')
        #break

    if Init >0 and Init<100:
        Main()
        break
