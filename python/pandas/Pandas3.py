import pandas as pd

cpga = {
        'Name':['Taylor', 'Ann', 'Christine', 'Aroosa'],
        'CGPA':[3.1,2.2,2.95, 3.4]

        }
df_cpga = pd.DataFrame(cpga)

favSports = {
        'Name':['Taylor', 'Ann', 'Christine', 'Charlia'],
        'Fav Sports':['Basketball', 'Football', 'Tennis', 'Cricket']

        }

df_favSports = pd.DataFrame(favSports)
merged_df = pd.merge(df_cpga, df_favSports, on='Name') # how='inner'=>default   'outer' 'left'=>Aroosa only
#print(merged_df) # Aroosa not included

merged_df['Rank'] = merged_df['CGPA'].rank(ascending=0, method='min')
merged_df['Rank'] = merged_df['CGPA'].rank(ascending=0, method='dense') # rank no blank
merged_df.sort_values(by=['CGPA', 'Age'], ascending=[0,1])
print(merged_df)

merged_df = pd.merge(df_cpga, df_favSports, on='Name') 
def comment(x):
    if x>=2.8:
        return 'Above Average'
    else:
        return 'Below Average'

merged_df['Comment']=merged_df['CGPA'].apply(comment)

writer = pd.ExcelWriter('Std_Record.xlsx')
merged_df.to_excel(writer,'DataFrame')
writer.save()

bool_Series1 = merged_df['Fav Sports'].isin(['Tennis', 'Football'])
bool_Series2 = merged_df['Age'].isin([24])
new_df = merged_df[bool_Series1 & bool_Series2]

bool_Series1 = merged_df['CGPA'].between([2.8,3.1,inclusive=True])

bool_Series1 = merged_df['Fav Sports'].duplicated(keep=False)
bool_Series1 = -bool_Series1
new_df = merged_df[bool_Series1]


