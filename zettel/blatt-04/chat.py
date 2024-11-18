import random

def generate_paper(n):
    """Generiert n zufällige Papers mit Bearbeitungszeiten und Deadlines."""
    P = []
    for i in range(n):
        t = random.randint(1, 20)  # Bearbeitungszeit
        d = random.randint(1, 20)  # Deadline
        if t <= d:
            P.append([t, d])
    return P

# Memoization dictionary
memo = {}

def Opt(P, i, D):
    """
    Berechnet die maximale Anzahl von Papers, die unter Berücksichtigung der Deadlines
    bearbeitet werden können, und gibt die Anzahl und das optimale Subset zurück.
    """
    # Basisfall: keine Papers übrig oder keine verfügbare Zeit
    if i < 0 or D == 0:
        return 0, []
    
    # Prüfen, ob das Ergebnis bereits berechnet wurde
    if (i, D) in memo:
        return memo[(i, D)]
    
    t_i, d_i = P[i][0], P[i][1]  # Bearbeitungszeit und Deadline des aktuellen Papers
    
    # Option 1: Paper i nicht aufnehmen
    exclude_paper, subset_exclude = Opt(P, i - 1, D)

    # Option 2: Paper i aufnehmen, falls es zeitlich passt und die Deadline einhält
    include_paper = 0
    subset_include = []
    if D >= t_i and D <= d_i:
        # Rekursiver Aufruf für den Fall, dass das Paper aufgenommen wird
        include_paper, subset_include = Opt(P, i - 1, D - t_i)
        include_paper += 1
        subset_include = subset_include + [P[i]]
    
    # Wähle die Option, die die maximale Anzahl an Papers liefert
    result = max((exclude_paper, subset_exclude), (include_paper, subset_include), key=lambda x: x[0])
    
    # Ergebnis speichern, um es später wiederzuverwenden
    memo[(i, D)] = result
    return result

def paper_submission(n):
    """Initialisiert die Papers und führt die Optimierung durch."""
    P = generate_paper(n)
    P.sort(key=lambda x: x[1])  # Sortieren nach Deadlines, um frühere Deadlines zu priorisieren
    max_deadline = max([d for _, d in P])  # Maximale Deadline als Zeitlimit setzen
    
    # Berechnung der maximalen Anzahl an bearbeitbaren Papers und des optimalen Subsets
    max_papers, subset = Opt(P, len(P) - 1, max_deadline)
    
    print("Papers:", P)
    print("Maximum number of schedulable papers:", max_papers)
    print("Subset of papers:", subset)
    return max_papers, subset

if __name__ == "__main__":
    paper_submission(10)
