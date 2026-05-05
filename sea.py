import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Boxplot
data = pd.DataFrame({'Dept':['CS']*20+['Math']*20, 'Score':[80,82,85,20,90]*8})
sns.boxplot(x='Dept', y='Score', data=data)
plt.title('Outliers')
plt.show()

# Heatmap
cars = pd.DataFrame({'Speed':[120,140,100], 'Engine':[2.0,3.5,1.5], 'Fuel':[15,10,20]})
sns.heatmap(cars.corr(), annot=True)
plt.title('Correlation')
plt.show()
