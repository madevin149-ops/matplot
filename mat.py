import matplotlib.pyplot as plt

# Line Chart
months = ['Jan','Feb','Mar','Apr','May','Jun']
sales = [12000,15000,13500,17000,19000,21000]

plt.plot(months, sales, marker='o')
plt.title('Monthly Sales')
plt.show()

# Pie Chart
expenses = [5000,8000,10000,2000,3000]
labels = ['Rent','Inventory','Salaries','Utilities','Marketing']

plt.pie(expenses, labels=labels, autopct='%1.1f%%')
plt.title('Expenses')
plt.show()
