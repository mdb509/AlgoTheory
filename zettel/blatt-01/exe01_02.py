import random
import time
import matplotlib.pyplot as plt
import numpy as np
import random

# Funktion zur Generierung von n Zufallszahlen als Liste
def generate_random_numbers(n, as_set=False):
    numbers = [random.randint(0, n) for i in range(n)]
    if as_set:
        return set(numbers)
    return numbers

def equivalenz_test(card1, card2):
    # Der Äquivalenztest: Karten werden als äquivalent angesehen, wenn sie gleich sind
    return card1 == card2


def fraud_detection(cards, n, n0, k):
    # Basisfall: Wenn nur eine Karte vorhanden ist, gib sie mit Anzahl 1 zurück
    if n == 1:
        return (False,{cards[0]: 1})

    # Teile die Karten in zwei Hälften
    mid = n // 2
    left_cards = cards[:mid]
    right_cards = cards[mid:]

    # Rekursiver Aufruf für linke und rechte Hälfte
    left_counts = fraud_detection(left_cards, len(left_cards),n0, k)
    right_counts = fraud_detection(right_cards, len(right_cards),n0, k)

    # Kombiniere die Zählungen unter Berücksichtigung des Äquivalenztests
    combined_counts = left_counts[1].copy()

    for right_card, right_count in right_counts[1].items():
        # Suche in der linken Hälfte nach Karten, die äquivalent zur rechten Karte sind
        found_equivalent = False
        for left_card in combined_counts:
            if equivalenz_test(left_card, right_card):
                # Wenn äquivalent, summiere die Zählungen
                combined_counts[left_card] += right_count
                found_equivalent = True
                break
        
        # Wenn keine äquivalente Karte gefunden wurde, füge die rechte Karte hinzu
        if not found_equivalent:
            combined_counts[right_card] = right_count
    # Überprüfe, ob irgendeine Karte mehr als n/k Mal vorkommt
    for card, count in combined_counts.items():
        if count > n0/ k:
            return (True, {card: count})

    # Gib die kombinierten Zählungen zurück
    return (False,combined_counts)


# Main-Funktion
def main():
    ns = [2**s for s in range(1, 16)]  # Verschiedene n-Werte für die Analyse
    runtimes = []
    for n in ns:
        k = n /4
        data = generate_random_numbers(n)
        start_time = time.time()
        passt, card = fraud_detection(data, len(data), len(data), k)
        if passt:
            print(f"n: {n}, k: {k}, n/k: {n/k}, Fraud Detection: {passt} und Card:{ card} ")
        else:
            print(f"n: {n}, k: {k}, n/k: {n/k}, Fraud Detection: {passt}  ")
        end_time = time.time()
        runtimes.append(end_time - start_time)  # Laufzeit speichern


    # Theoretische Komplexitäten (skalieren, um den Messwerten nahe zu kommen)
    max_runtime = max(runtimes) if runtimes else 1
    scale_factor = max_runtime / max(ns)  # Skaliere die theoretischen Funktionen
    scale_factor_nlogn = max_runtime / max(n * np.log(n) for n in ns)
    scale_factor_n2 = max_runtime / max(n**2 for n in ns)

    # Plotten der Laufzeiten und der theoretischen Komplexitäten
    plt.figure(figsize=(10, 6))

    # Plot der Laufzeit von fraud_detection
    plt.plot(ns, runtimes, label="Fraud Detection (gemessene Laufzeit)", color="black", marker="o")

    # Plot der skalierten O(n), O(nlogn), O(n^2)
    plt.plot(ns, [n * scale_factor for n in ns], label="O(n) (skaliert)", color="red", linestyle="--")
    plt.plot(ns, [n * np.log(n) * scale_factor_nlogn for n in ns], label="O(n log n) (skaliert)", color="green", linestyle="--")
    plt.plot(ns, [n**2 * scale_factor_n2 for n in ns], label="O(n^2) (skaliert)", color="blue", linestyle="--")

    # Diagramm-Details
    plt.xlabel("n (Größe des Datensatzes)")
    plt.ylabel("Laufzeit (Sekunden)")
    plt.title("Laufzeitanalyse von Fraud Detection")
    plt.legend()
    plt.grid(True)
    
    # Zeige das Plot
    plt.show()

if __name__ == "__main__":
    main()
