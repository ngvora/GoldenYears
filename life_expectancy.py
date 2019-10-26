import pandas as pd
def life_expectancy(gender, age):
    df_male = pd.read_excel(r'C:\Users\Aidan\Downloads\python\life_expectancy_male.xlsx')
    df_female = pd.read_excel(r'C:\Users\Aidan\Downloads\python\life_expectancy_female.xlsx')
    df = 0
    if gender == 1:
        df = df_male
    else:
        df = df_female
    position = age
    label = 'Life Expectancy'

    LE = df.at[position, label]
    print('Your life expectancy is ' + str(LE) + 'years')

if __name__ == "__main__":
       life_expectancy(0,21)