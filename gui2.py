import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def monte_carlo_korean_cosmetics(num_simulations=100000):
    min_sales, max_sales = 500, 2000
    product_price = 30
    product_cost = 15

    # Reklamation und Kosten
    complaint_distribution = [0.8, 0.18, 0.02]
    complaint_costs = [20, 50, 200]

    # Allergy param
    allergy_rate = 0.03
    return_rate = 0.5

    # Simulation von Verkäufen, Allergien und Ansprüchen
    sales = np.random.randint(min_sales, max_sales, num_simulations)
    allergy_cases = np.round(sales * allergy_rate).astype(int)
    returns = np.round(allergy_cases * return_rate).astype(int)

    # Reklamationkosten berechnen
    complaint_types = np.random.choice([0, 1, 2], size=num_simulations, p=complaint_distribution)
    return_loss = np.array([complaint_costs[ct] for ct in complaint_types]) * returns

    # Gewinnberechnung
    revenue = sales * product_price
    total_cost = sales * product_cost
    profit = revenue - total_cost - return_loss

    avg_profit = np.mean(profit)

    plt.figure(figsize=(6, 4))
    plt.hist(profit, bins=50, edgecolor='black')
    plt.title('Gewinnverteilung (Monte-Carlo-Simulation)')
    plt.xlabel('Gewinn in BGN')
    plt.ylabel('Häufigkeit')
    plt.show()

    return {
        "Durchschnittlicher Gewinn": np.mean(profit),
        "Maximaler Gewinn": np.max(profit),
        "Minimaler Gewinn": np.min(profit),
        "Reklamationskosten gesamt": np.sum(return_loss),
        "Reingewinn nach Abzug der Kosten": avg_profit,
        "Betroffene Kunden (%)": (np.sum(returns) / np.sum(sales)) * 100
    }


def run_simulation():
    try:
        num_simulations = int(entry.get())
        if num_simulations <= 0:
            raise ValueError("Die Anzahl der Simulationen muss positiv sein!")
        results = monte_carlo_korean_cosmetics(num_simulations)
        output_text.delete(1.0, tk.END)
        for key, value in results.items():
            output_text.insert(tk.END, f"{key}: {value:.2f}\n")
    except ValueError as e:
        messagebox.showerror("Fehler", str(e))


# GUI erstellen
root = tk.Tk()
root.title("Monte-Carlo-Simulation - Goblin Cosmetics ©IVAYLA MARKOVA")
root.geometry("500x400")

tk.Label(root, text="Anzahl der Simulationen:(von 0 bis 100000)").pack()
entry = tk.Entry(root)
entry.pack()
entry.insert(0, "100000")

tk.Button(root, text="Simulation starten", command=run_simulation).pack()

output_text = tk.Text(root, height=10, width=60)
output_text.pack()

root.mainloop()
