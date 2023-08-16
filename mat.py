import matplotlib.pyplot as plt

operating_systems = ['Android', 'iOS', 'Windows', 'Others']
market_share = [74.6, 22.9, 1.3, 1.2]

colors = ['lime', 'orange', 'blue', 'lightblue']

plt.pie(market_share, labels=operating_systems, colors=colors, autopct='%.1f%%')
plt.title('Market Share of Mobile Operating Systems')
plt.axis('equal')
plt.show()