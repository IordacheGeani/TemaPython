import matplotlib.pyplot as plt
import pandas as pd

file_path = r"C:\Users\Geanis\Desktop\TemaPython\data.csv"

df = pd.read_csv(file_path)

df.plot()
plt.title("Toate valorile")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df.head(8).plot()
plt.title("Primele 8 valori")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()

df[['Durata', 'Puls']].tail(12).plot()
plt.title("Ultimele 12 valori pentru Durata și Puls")
plt.xlabel("Index")
plt.ylabel("Valori")
plt.legend(title="Parametrii")
plt.show()
