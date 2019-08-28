import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates
from mpl_toolkits.mplot3d import axes3d
import sqlalchemy
register_matplotlib_converters()

conn=sqlalchemy.create_engine(
    'mysql+pymysql://root:denny2310@localhost:3306/world'
)

# =========NO1

plt.style.use('seaborn')
q="select Name as negara,Population as populasi from country where Region='Southeast Asia'"
df=pd.read_sql_query(q,conn)
plt.title('Populasi Negara ASEAN', fontdict={'fontsize':20})
plt.bar(df['negara'],df['populasi'],color=['r','g','b','k','r','y','lightblue','gold','pink','grey'])
ax=plt.gca()

for p in ax.patches:
    ax.annotate(str(p.get_height()),(p.get_x(),p.get_height()*1.015),ha='left')
plt.xlabel('Negara')
plt.ylabel('Populasi (x100jt jiwa)')
plt.xticks(rotation=60)
plt.show()




# =======no 2
plt.style.use('seaborn')
q="select Name as negara,Population as populasi from country where Region='Southeast Asia'"
df=pd.read_sql_query(q,conn)
plt.title('Persentase Penduduk ASEAN', fontdict={'fontsize':20})
plt.pie(df['populasi'],labels=df['negara'],autopct='%1.1f%%',textprops={'color':'black'})

plt.show()

# ===============no3
q="select Name as negara,GNP as GNP from country where Region='Southeast Asia'"
df=pd.read_sql_query(q,conn)
plt.title('Pendapatan Bruto Nasional ASEAN', fontdict={'fontsize':20})
plt.bar(df['negara'],df['GNP'],color=['r','g','b','k','r','y','lightblue','gold','pink','grey'])
ax=plt.gca()
for p in ax.patches:
    ax.annotate(str(p.get_height()),(p.get_x(),p.get_height()*1.005))
plt.xticks(rotation=60)
plt.xlabel('Negara')
plt.ylabel('GNP(USD)')
plt.show()

# ==========NO 4
q="select Name as negara,SurfaceArea as LuasArea from country where Region='Southeast Asia'"
df=pd.read_sql_query(q,conn)
plt.title('Persentase Luas Daratan ASEAN', fontdict={'fontsize':20})
plt.pie(df['LuasArea'],labels=df['negara'],autopct='%1.1f%%',textprops={'color':'black'})


plt.show()

