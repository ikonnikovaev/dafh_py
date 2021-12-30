# write your code here
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def write_gender(s):
    if s in ['man', 'male']:
        return 'm'
    elif s in ['woman', 'female']:
        return 'f'
    else:
        return s

pd.set_option('display.max_columns', 8)
general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

prenatal.columns = general.columns
sports.columns = general.columns

df = pd.concat([general, prenatal, sports], ignore_index=True)
df.drop(columns='Unnamed: 0', inplace=True)
df.dropna(how='all', inplace=True)
df.gender = df.gender.apply(write_gender)
df.gender.fillna('f', inplace=True)
for c in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound',
          'mri', 'xray', 'children', 'months']:
    df[c].fillna('0', inplace=True)
#print(df.shape)
#print(df.sample(n=20,random_state=30))
#print(df.columns)
ranges = [0, 15, 35, 55, 70, 80]
age_counts = df.age.groupby(pd.cut(df.age, ranges)).count()
most_common_age = age_counts.idxmax()
print(f"The answer to the 1st question: {most_common_age.left}-{most_common_age.right}")
df.age.plot(kind='hist', bins=ranges)
plt.savefig("../pics/age.jpg")
plt.show()

plt.clf()
vc = df.diagnosis.value_counts()
print(f"The answer to the 2nd question: {vc.idxmax()}")
vc.plot(kind='pie')
plt.savefig("../pics/diagnosis.jpg")
plt.show()

plt.clf()
height_plot = sns.violinplot(x='hospital', y='height', data=df)
plt.savefig("../pics/height.jpg")
plt.show()
print(f"The answer to the 3rd question : It's because probably there are a lot of basketball or volleyball players in sports hospital")

'''
hospital_counts = df.hospital.value_counts()
print(f"The answer to the 1st question is {hospital_counts.index[0]}")
df_general = df.loc[df.hospital=='general']
df_sports = df.loc[df.hospital=='sports']
dscounts_general = df_general.diagnosis.value_counts()
print(f"The answer to the 2nd question is {dscounts_general['stomach']/df_general.shape[0]}")
dscounts_sports = df_sports.diagnosis.value_counts()
print(f"The answer to the 3rd question is {dscounts_sports['dislocation']/df_sports.shape[0]}")
print(f"The answer to the 4th question is {df_general.age.median() - df_sports.age.median()}")
pt = df.pivot_table(index='hospital', columns='blood_test', aggfunc={'blood_test':'count'})
#print(pt)
max_t = 0
max_t_h = None
for h in df.hospital.unique():
    vc = df.loc[df.hospital==h].blood_test.value_counts()
    if 't' in vc and vc['t'] > max_t:
        max_t_h = h
        max_t = vc['t']
print(f"The answer to the 5th question is {max_t_h}, {max_t} blood tests")
'''
df_general = df.loc[df.hospital=='general']
df_sports = df.loc[df.hospital=='sports']
gcounts_general = df_general.gender.value_counts()
gcounts_sports = df_sports.gender.value_counts()
#print(gcounts_general)
#print(gcounts_sports)
