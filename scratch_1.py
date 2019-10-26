import pandas as pd
df_male = pd.read_excel(r'C:\Users\Aidan\Downloads\python\life_expectancy_male.xlsx')
df_female = pd.read_excel(r'C:\Users\Aidan\Downloads\python\life_expectancy_female.xlsx')

print('Enter Age')
x = int(input())

print('Enter 1 for male and 0 for female')
gender = int(input())

df = 0
if gender == 0:
    df = df_female
else:
    df = df_male


position = x
label = 'Life Expectancy'

LE = df.at[position,label]
print('Life expectancy for someone who is '+str(x)+' years old is ' +str(LE))

print('Enter salary')
salary = int(input())

print('Enter savings')
savings = int(input())

ytr = 65 - x
goldyears = LE - ytr
retiresalary = (ytr*salary + savings) / goldyears
print(retiresalary)

