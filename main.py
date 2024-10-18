# Challenge 1

# Total Sales

# Design a program that asks the user to enter a store’s sales for each day of the week. 
# The amounts should be stored in a list. Use a loop to calculate the total sales for the week and display the result.


days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
sales_list = []
total_sales = 0

for day in days_of_week:
  day_sales =  int(input('What were the sales for ' + '' + day))
  sales_list.append(day_sales)

for int in sales_list:
  total_sales += int
  

# print(total_sales)



import random

# Capital Quiz

# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values. (Use the Internet to get a list of the states and their capitals.)
# The program should then randomly quiz the user by displaying the name of a state and asking the user
# to enter that state’s capital. The program should keep a count of the number of correct and incorrect 
# responses. (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)

states_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

correct_answer = 0
wrong_answer = 0

select = random.choice(list(states_capitals))


quiz = print(f'What is the capital of {select} ?')

user_answer = input()

if user_answer == states_capitals[select]:
   print('correct!')
   correct_answer =+ 1
 
else:
   print('wrong!')
   wrong_answer =+ 1
  

print(correct_answer)

print(wrong_answer)