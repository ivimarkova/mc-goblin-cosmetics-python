#Koreanische Kosmetika Online Shop "Goblin Cosmetics" - Simulator mit Monte-Carlo
import numpy as np

def monte_carlo_korean_cosmetics(num_simulations=1000):
    #  Parameter des Unternehmens
    min_sales, max_sales = 500, 2000  # Verkaufssortiment
    product_price = 30  # Produktpreis (BGN)
    product_cost = 15   # Kosten pro Produkt (BGN)
    return_cost = 5     #  Kosten der Schadenbearbeitung (BGN)//рекламация
    
    allergy_rate = 0.03  # 3% von den Kunden haben Allergische Reaktion
    return_rate = 0.5    # 50% von ihnen wollen eine Rückkehr

    # Simulation von Verkäufen, Allergien und Ansprüchen
    sales = np.random.randint(min_sales, max_sales, num_simulations)
    allergy_cases = np.round(sales * allergy_rate).astype(int)
    returns = np.round(allergy_cases * return_rate).astype(int)

    # Berechnungen
    revenue = sales * product_price  # Allgemeines Einkommen
    total_cost = sales * product_cost  # Kosten der Waren
    return_loss = returns * (product_price + return_cost)  # Verluste aus Schadensfällen
    profit = revenue - total_cost - return_loss  # Profit

    # Average
    avg_sales = np.mean(sales)
    avg_revenue = np.mean(revenue)
    avg_total_cost = np.mean(total_cost)
    avg_return_loss = np.mean(return_loss)
    avg_profit = np.mean(profit)

    return {
    "Durchschnittlicher Verkauf pro Monat": avg_sales,  
    "Durchschnittlicher Umsatz": avg_revenue,  
    "Gesamtkosten": avg_total_cost,  
    "Verluste durch Rückgaben": avg_return_loss, 
    "Reingewinn nach Abzug der Kosten": avg_profit  }


# Run die Simulation
results = monte_carlo_korean_cosmetics()
for key, value in results.items():
    print(f"{key}: {value:.2f} BGN")
