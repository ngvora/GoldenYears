import pandas as pd
def user_results(gender, cage, desired_rage, salary,retirepercent,currentsavings,yearlysavings):
    df_male = pd.read_excel(r'C:\Users\Aidan\Documents\GitHub\GoldenYears\life_expectancy_male.xlsx')
    df_female = pd.read_excel(r'C:\Users\Aidan\Documents\GitHub\GoldenYears\life_expectancy_female.xlsx')
    df = 0
    if gender == 'M':
        df = df_male
    else:
        df = df_female
    position = cage
    label = 'Life Expectancy'

    le = df.at[position, label]

    ytr = desired_rage - cage
    gy = le - desired_rage + cage
    net_savings = (retirepercent/100)*salary*ytr + currentsavings + yearlysavings*ytr
    retirement_income = net_savings/gy
    if net_savings >= 8*salary:
        print('Congratulations! You are on track to retire on time with adequate savings')
        print('Your savings at retirement should roughly be $' + str(round(net_savings,2)))
        print('You could spend $' + str(round(retirement_income,2)) + ' yearly for ' + str(round(gy,1)) + ' years')
    else:
        ideal_ytr = (8*salary - currentsavings)/((retirepercent/100)*salary + yearlysavings)
        ideal_retirement_age = ideal_ytr + cage
        ideal_percent_retire = (8 * salary - currentsavings - yearlysavings*ytr) / (ytr * salary)
        print('You should consider saving more for a more comfortable retirement')
        print('Your retirement savings would be $' + str(round(net_savings,2)) + ' and you should roughly aim for $' + str(round(8*salary,2)))
        print('To correct this, you should retire later at ' + str(int(ideal_retirement_age)))
        print('OR adjust the percentage of your salary invested in retirement to ' + str(round(100*ideal_percent_retire,2)) + '%, which is $' + str(round(salary*ideal_percent_retire,2)) + ' yearly')


