import pandas as pd
def user_results(gender, cage, desired_rage, salary,retirepercent,currentsavings,yearlysavings):
    if gender == 'F':
        gender = 0
    else:
        gender = 1
    df_male = pd.read_excel(r'life_expectancy_male.xlsx')
    df_female = pd.read_excel(r'life_expectancy_female.xlsx')
    df = 0
    if gender == 1:
        df = df_male
    else:
        df = df_female
    position = cage
    label = 'Life Expectancy'

    le = df.at[position, label]

    ytr = desired_rage - cage
    gy = le - desired_rage + cage
    net_savings = retirepercent*salary*ytr + currentsavings + yearlysavings*ytr
    retirement_income = net_savings/gy
    if net_savings >= 10*salary:
        print('Income Sufficient. Savings = ' + str(round(net_savings, 2)) + ' and retirement income = ' + str(round(retirement_income, 2)))
    else:
        ideal_ytr = (10*salary - currentsavings)/(retirepercent*salary + yearlysavings)
        ideal_retirement_age = ideal_ytr + cage
        ideal_percent_retire = (10 * salary - currentsavings - yearlysavings*ytr) / (ytr * salary)
        print('Income Insufficient. Increase percent savings to ' + str(round(ideal_percent_retire, 4)) + ' or choose to retire at' + str(round(ideal_retirement_age)))


user_results('F',20,65,50000,.08,50000,10000)