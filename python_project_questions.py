# List Questions for Python Group Project.

# Question 1:
list = ['The cat knows code', 'She worked as a Project Manager before attending DigitalCrafts', 'Today is not yesterday!'] 
clue1 = (list[0]) 
clue2 = (list[0]) 
clue3 = (list[1]) 
clue4 = (list[2]) 
print(clue1[0:4] + clue2[14:18] + clue3 [3:10] + clue4[12:24])

# Question 2:
list2 = ['The', 'REASON', 'your', 'CODE', 'IS', 'NOT', 'working today....']
letter_1 = (list2[1])
letter_2 = (list2[4])
print('The ' + letter_1[2] + letter_2[0] + ' has leveled up and is now in contol of computer 1.')

# Question 3:
list3 = ['d1r0w', '0113h']
list3.reverse()
print(list3)

# Dictonary Questions:

# Question 1:
computer_1 = { 
  'user': 'Sean', 
  'folder': 9, 
  'oh no': 'Enemy Found' 
}

print(computer_1.pop('oh no'))

# Dictonary Questions:

# Question 2:
player_skills = { 
   'DigitalCrafts':{ 
      'programmer':{ 
         'name': 'Sean',
         'skills':{ 
            'python': 70,
            'git': -1,
            'team work': 'Expert'
         }
      }
   }
}

print(player_skills['DigitalCrafts']['programmer']['name'])

