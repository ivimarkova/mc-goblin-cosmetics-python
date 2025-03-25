#Koreanische Kosmetika Online Shop "Goblin Cosmetics" - Simulator mit Monte-Carlo
#Authorin: Ivayla Markova, Technische Universität - Sofia, Fakultät für deutsche Ingenieur- und Betriebswirtschaftsausbildung
import matplotlib.pyplot as plt
import numpy as np
def monte_carlo_korean_cosmetics(num_simulations=1000000):
    #  Parameter des Unternehmens
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

    # Fortschrittsanzeige
    print("Hallo! \nDas ist ein Simulator mit Monte-Carlo für Koreanische Kosmetika Online Shop 'Goblin Cosmetics'")
    print(f"\nSimulation läuft ({num_simulations} Iterationen):")
    for i in range(num_simulations):
        if i % 10000 == 0:
            print(".", end="", flush=True)

    # Average
    avg_profit = np.mean(profit)

    # Graphische Darstellung
    plt.hist(profit, bins=50, edgecolor='black')
    plt.title('Gewinnverteilung (Monte-Carlo-Simulation)')
    plt.xlabel('Gewinn in BGN')
    plt.ylabel('Häufigkeit')

    return {
        "Durchschnittlicher Gewinn": np.mean(profit),
        "Maximaler Gewinn": np.max(profit),
        "Minimaler Gewinn": np.min(profit),
        "Reklamationskosten gesamt": np.sum(return_loss),
        "Reingewinn nach Abzug der Kosten": avg_profit,
        "Betroffene Kunden (%)": (np.sum(returns) / np.sum(sales)) * 100
    }


# Run die Simulation
results = monte_carlo_korean_cosmetics()
for key, value in results.items():
    if "(%)" in key:
        print(f"{key}: {value:.2f} %")
    else:
        print(f"{key}: {value:.2f}")

plt.show()
