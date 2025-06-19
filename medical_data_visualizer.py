import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
bmi_df = df["weight"]/(df["height"]/100)**2


df["overweight"] = [1 if x > 25 else 0 for x in bmi_df]

# 3
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)


# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = ["cardio"], value_vars = ['active','alco','cholesterol','gluc','overweight','smoke'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable','value']).size().reset_index(name='total')    

    # 7

    # 8
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) 
            & (df['height'] >= df['height'].quantile(0.025)) 
            & (df['height'] <= df['height'].quantile(0.975))
            & (df['weight'] >= df['weight'].quantile(0.025)) 
            & (df['weight'] <= df['weight'].quantile(0.975))]
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool)) #Optional, to hide the upper triangle

    # 14
    fig, ax = plt.subplots(figsize=(8,6))

    # 15
    sns.heatmap(corr, annot=True, fmt=".1f", linewidth=0.3, center=0, mask=mask, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig
