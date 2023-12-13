#!/usr/bin/env python
# coding: utf-8

# # Problem statement
# 
# Create famous 'Frog leap' puzzle game. Try completing the game before starting to get an idea about its working.
# [Demonstration](https://www.neok12.com/games/leap-froggies/leap-froggies.htm).
# 
# 
# ### Rules ###
# 1. The left set of frogs can only move right, the right set of frogs can only move left.
# 2. Frogs can move forward one space, or move two spaces by jumping over another frog from opposite side.
# 3. The puzzle is solved when the two sets of frogs have switched positions.
# 
# 
# ## Steps to solve the problem:
# ### Step1:-
# - Display green and brown frogs on the left and right sides initially.
# 
# Initial Display :-  
# ```
# [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]
# ['G', 'G', 'G', '-', 'B', 'B', 'B']
# ```
# <br>
# Here 'G' represents Green frogs on the left side and 'B' represents brown frogs on the right side. The '-' defines the position of empty leaf.
# (You can change display according to your imagination or convinience)
# 
# ### Step2:-
# Accept positions of the frog that you want to move.<br>
# Example: If we enter position 2 then the game will look like this:-
# ```
# [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]
# ['G', 'G', '-', 'G', 'B', 'B', 'B']
# ```
# 
# ### Step3:- ###
# Define Invalid moves and add conditional 'if' statements accordingly
# #### Rules
# 1. Entered position should be between 0 to 6. Or a character 'q' to quit the game.
# 2. Entered position cannot be the position of empty leaf.
# 3. If the selected frog position cannot perform the contraints given in rule 2 then the move is invalid.
# 
# ### Step4:-
# Make the appropriate move by changing the game display.

# ## Step 1
# First create a list `positions` which contains the characters 'G','B' and '-' in the same sequence as given in the initial display state.

# In[5]:


### Search the python Src Unicode version of Frog.
a=u"\U0001F438"
a1=u"\U0001F422"
b='-'
### Make a list using the frog emoji and a blank[Acc to our Game Theme] 
l=[a1,a1,a1,b,a,a,a]


# Now print this string ```[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]``` and after that print the list `positions`

# In[6]:


### print the list
print(l)


# Take position input from user and write a message as `"Press q to quit else \nEnter position of piece:"`.

# In[7]:


### To quit or enter the position of piece.
n=input("Press q to quit else\n Enter position of piece:")


# Now the taken input is in string format. So first check if the input is `'q'` character. If input is `'q'` then the person is quiting the game so print `'You Lose'`.

# In[8]:


### If input is q then the person lost the game and play from the start.
if n=='q':
    print("you lose")


# Next if input character is not `'q'` then it has to be some integer. so convert input to integer format.

# In[9]:


### If input is not 'q' then convert the string into Integer.
if n!='q':
    n=int(n)
    print(n)


# ## Step 2
# Now we have to check validity of the selected positions or move.<br>
# If the entered number isn't between 0 and 6, then print 'Invalid move'.

# In[10]:


### If input is not in between "0 to 6" it is invalid.
if n<0 and n>6:
    print("Invalid Move")
    


# A frog should be present on the selected position to make a move. If leaf is selected then it doesn't make sense. Therefore, if entered postition is same as the postition of empty leaf then the move is invalid and print `Invalid Move`

# In[11]:


### If selected position is blank it is invalid.
if l[n]=='-':
    print("Invalid Move")
    


# Initialize a variable named `pos2` at value 0, to store the index of empty leaf, so that we can use it later.

# In[12]:


### initializing "pos2" to "zero"
pos2=0
        


# ```   
#     Check if the selected frog is 'G':
#   
#         (Inside if when it's 'G'. As 'G' is selected frog can move to right only.)
#         
#         ❗condition 1
# 
#         If **selected_position + 1** is less than or equal to 6 and **curent_position + 1** contains '-'
#         then it's a valid move and store that postion in `pos2`.
#         
#         ❗condition2
# 
#         Else if **selected_position + 2** is less than or equal to 6 and if **current_position + 2**
#         contains '-' and if **selected_position + 1** contains 'B' then it's a valid move  and store that postion in `pos2`.
#         
#         ❗condition3:
# 
#         Else remainig all are invalid, so print `Invalid Move`
#       
# ```

# In[13]:


###
if l[n]==a1:
    if n+1<=6 and l[n+1]=='-':
        pos2=n+1
    elif n+2<=6 and l[n+2]=='-' and l[n+1]==a1:
        pos2=n+2
    else:
        print("Invalid Move")
        


# ```
#     Check if the selected frog is 'B':
#     
#         (Inside if when it's 'B'. As 'B' is selected frog can move to left only.)
#         
#         ❗condition1:
# 
#         If **selected_position - 1** is more than or equal to 0 and **curent_position - 1** contains '-' then
#         it's a valid move and and store that postion in `pos2`.
#         
#         ❗condition2:
# 
#         Else if **selected_position - 2** is more than or equal to 0 and if **current_position - 2** contains '-'
#         and if **selected_position - 1** contains 'G' then it's a valid move and and store that postion in `pos2`.
# 
#         ❗condition3:
#         
#         Else remainig all are invalid,, so print `Invalid Move`.
#         
# ```

# In[14]:


### your code here
if l[n]==a:
    if n1>=0 and l[n-1]=='-':
        pos2=n-1
    elif n-2>=0 and l[n-2]=='-' and l[n-1]==a1:
        pos2=n-2
    else:
        print("Invalid Move")


# Swap the element at selected positions and calculated position2 in the list.<br> So basically we are moving the frog to next valid position by swapping elelments of array.

# In[15]:


### your code here
t=l[pos2]
l[pos2]=l[n]
l[n]=t


# Now print the display of the game again to see the change.<br>
# If we enter position 2 then the output will look like this:-
# ```
# [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]
# ['G', 'G', '-', 'G', 'B', 'B', 'B']
# ```

# In[16]:


### your code here
print(l)


# Check for winning condition by comparing the elements of list. If player has won the game print `'You Win'`

# In[17]:


### your code here
if l.reverse()==l:
    print("You Win")
    


# Now the game should keep running until the player quits, so place all conditional statements inside an infinite loop.<br>
# 
# 1. We have to `'break'` the loop if the player presses `'q'` and quits.
# 
# 2. If the move made by player is `'Invalid Move'` then we have to `'continue'` without executing remaining part of the selected iteration.
# 
# 3. If player wins the game we have to `break` the loop.
# 
# 
# ```
# Infinite loop:
#     (inside loop)
#     1.Take input
#     2.Check all valid and invalid conditions of `pos`.
#     3.Make the appropriate move by calculating `pos2`.
#     4.Display game
#     4.Check winning condition
# ```

# In[9]:


import tkinter


# In[8]:



### make a temperory list

temp_list=[]
### give the unicode of frog to green frog

green_frog=u"\U0001F438"
### we have one frog available in unicode so, let's take a turtle 
turtle_frog=u"\U0001F422"
### initialize a variable with blank

blank=' '
### Make a list using the frog emoji and a blank[Acc to our Game Theme] 

game=[turtle_frog,turtle_frog,turtle_frog,blank,green_frog,green_frog,green_frog]
### write an infinite loop
while(1):
    pos=input("Press q to quit else\n Enter position of piece:")
    if pos=='q':
        print("you lose\n")
        break
### check if the entered input is number or 'q'
    
    if pos!='q':
        pos=int(pos)
    pos2=0    
### check if the position is valid or not
    
    if pos<0 and pos>6:
        print("Invalid Move")
        continue
    if game[pos]=='-':
        print("Invalid Move")
        continue
###  check if the entered podsition have turtle and perform the conditions given   
    if game[pos]==turtle_frog:
        if pos+1<=6 and game[pos+1]=='-':
            pos2=pos+1
        elif pos+2<=6 and game[pos+2]=='-' and game[pos+1]==green_frog:
            pos2=pos+2
        else:
            print("Invalid Move")
            continue
### check if the entered position have frog and perform the conditions given
    elif game[pos]==green_frog:
        if pos-1>=0 and game[pos-1]=='-':
            pos2=pos-1
        elif pos-2>=0 and game[pos-2]=='-' and game[pos-1]==turtle_frog:
            pos2=pos-2
        else:
            print("Invalid Move")
            continue
### swap the frog with the blank            
    temp=game[pos2]
    game[pos2]=game[pos]
    game[pos]=temp  
### for every cicle print the output game    
    for i in game:
        print(i,end="   ")
### the above result list is stored in temperory list

    temp_list=game[::-1]
    print("\n")
### check if the lists are equal or not    
    if temp_list==game:
        print("You Win")
        break


# In[ ]:



# Import module 
from tkinter import *
from tkinter import messagebox
# Create object 
root = Tk() 
pos2=0
# Adjust size 
root.geometry("800x1200") 
root.title("Frog Leap Game")
root.configure(bg="light blue")
root.iconbitmap(r"C:\Users\sindu\Downloads\icon.ico")
def button_code(b):
    if b[text]=="🐸":
        




b1=Button(root,text="🐸",command=lambda:button_code(b1))
b2=Button(root,text="🐸",command=lambda:button_code(b2))
b3=Button(root,text="🐸",command=lambda:button_code(b3))
b4=Button(root,text="   ",command=lambda:button_code(b4))
b5=Button(root,text="🐢",command=lambda:button_code(b5))
b6=Button(root,text="🐢",command=lambda:button_code(b6))
b7=Button(root,text="🐢",command=lambda:button_code(b7))

# grid the button

b1.place(x=250,y=250)
b2.place(x=300,y=250)
b3.place(x=350,y=250)
b4.place(x=400,y=250)
b5.place(x=450,y=250)
b6.place(x=500,y=250)
b7.place(x=550,y=250)



# Execute tkinter 
root.mainloop() 

