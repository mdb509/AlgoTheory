---
date: 25.10.2024
author:
 Kai Malaka (km324) 5518467 -> Gruppe 4 /  Manuel DiBiase (md509)  5515822 -> Gruppe 4
---

# exerxise sheet 01

## exe. 1 
### a)

$$
n=3^j, j \in N\\
\begin{align*}
T(n) &\leq 3*T(\frac{n}{3})+c*n*log_3(n)\\
T(3^j) &\leq 3*T(3^{j-1})+c*n*log_3(3^j)\\\\

T(\frac{n}{3}) &\leq 3*T(\frac{n}{9})+c*\frac{n}{3}*log_3(\frac{n}{3})\\
T(3^{j-1}) &\leq 3*T(3^{j-2})+c*3^{j-1}*log_3(3^{j-1})\\\\

T(n) &\leq 3* (3* T(\frac{n}{9})+c*\frac{n}{3}*log_3(\frac{n}{3}))+c*n*log_3(n)\\
&\leq 3^2 T(\frac{n}{9})+c*n*log_3(\frac{n}{3})+c*n*log_3(n)\\
\rightarrow n = 3^j\\

&\leq 3^2 T(3^{j-2})+c*3^j*log_3(3^{j-1})+c*3^j*log_3(3^j)\\
&\leq 3^2 T(3^{j-2})+c*3^j*(j-1)+c*3^j*(j)\\
\rightarrow \text{nach k Schritten}\\
T(3^j) &\leq 3^k T(3^{j-k})+c* \sum^{k-1}_{i=0}3^{j-i}*(j-i)\\
\rightarrow \text{für k = j}\\
T(3^j) &\leq 3^j T(1)+c* \sum^{j-1}_{i=0}3^{j-i}*(j-i)\\
\rightarrow \text{da T(1) <= c}\\
T(3^j) &\leq 3^j *c+c* \sum^{j-1}_{i=0}3^{j-i}*(j-i)\\\\\\
\sum^{j-1}_{i=0}3^{j-i}*(j-i) &= 3^j * j + 3^{j-1}(j-1)+ 3^{j-2}(j-2)+...\\
&\rightarrow 3^j*j \text{ dominiert}\\
\rightarrow T(3^j) &\leq* 3^j*c+c*3^j*j\\
 &\leq* n*c+c*n*log_3n\\\\
 \rightarrow T(n) &= O(n*logn) \rightarrow \text{Laufzeit O(n*logn)}

\end{align*}
$$

### b)

**Induktionsanfang:**
$$
\begin{align*}
n = 1 &\rightarrow T(1)\leq c\\
&\rightarrow T(1)\leq c' * 1 log_3(1) = 0, c' \geq c, c\gt 0\\
\end{align*}
$$
**Induktionsvorraussetzung:**
$$
\begin{align*}
j&=k , n = 3^j\\
T(3^k) &\leq c'*3^k * log_3(3^k) = c' * 3^k * k\\
&\leq c' * n * log_3(n)
\end{align*}
$$
**Induktionsschritt:**
$$
\begin{align*}
j &= k+1, n=3^{k+1}\\
T(3^{k+1}) &\leq 3 T(\frac{3^{k+1}}{3})+c*3^{k+1}*log_3{3^{k+1}}\\
&\leq 3 T(3^k)+c*3^{k+1}*(k+1)\\
(IV)&\leq 3 (c'*3^k*k)+c*3^{k+1}*(k+1)\\
&\leq c'*3^{k+1}*k+c*3^{k+1}*(k+1)\\
&\leq 3^{k+1}*(c'*k+c*(k+1))\\
&\leq 3^{k+1}*(c'*k+c*k + c)\\
&\leq 3^{k+1}*((c'+c)*k+c)\\\\
\rightarrow ((c'+c)*k+c) &\leq c' * (k+1)\\
((c'+c)*k+c)&\leq c' * k + c'\\
c'*k+c*k + c&\leq c' * k + c'\\
\leftrightarrow c*k + c&\leq  c' \rightarrow c \leq c'\\\\
\rightarrow T(3^{k+1})&\leq 3^{k+1}* c' * (k+1)\\\\


\end{align*}
$$




## exe. 2

```python
def equivalenz_test(card1, card2):
    # The Equivalence Test: Cards are considered equivalent if they are the same
    return card1 == card2


def fraud_detection(cards, n, n0, k):
    # Base case: If there is only one card, return it with count 1
    if n == 1:
        return (False,{cards[0]: 1})

    # Divide the cards in half
    mid = n // 2
    left_cards = cards[:mid]
    right_cards = cards[mid:]

    # Recursive call for left and right halves
    left_counts = fraud_detection(left_cards, len(left_cards),n0, k)
    right_counts = fraud_detection(right_cards, len(right_cards),n0, k)

    # Combine the counts considering the equivalence test
    combined_counts = left_counts[1].copy()

    for right_card, right_count in right_counts[1].items():
        # Look in the left half for cards that are equivalent to the right card
        found_equivalent = False
        for left_card in combined_counts:
            if equivalenz_test(left_card, right_card):
                # If equivalent, sum the counts
                combined_counts[left_card] += right_count
                found_equivalent = True
                break
        
        # If no equivalent card was found, add the right card
        if not found_equivalent:
            combined_counts[right_card] = right_count
    # Check if any card appears more than n/k times
    for card, count in combined_counts.items():
        if count > n0/ k:
            return (True, {card: count})

    # Return the combined counts
    return (False,combined_counts)

```



### Correctness:

1. **Divide and Conquer**: The algorithm recursively divides the set of bank cards into smaller subsets. This is a common approach for problems like this because it allows us to reduce the complexity of comparing each card to all others.
   
2. **Equivalence Testing**: For each division, the algorithm recursively processes the left and right halves of the card set. It uses the $\texttt{equivalence\_test}$ function to determine if two cards are equivalent. By combining results from the left and right subsets, the algorithm keeps track of how many cards are equivalent to each other.
   
3. **Correctness**: The correctness follows from the fact that the algorithm tests equivalence between all cards across both halves and tracks counts for equivalent cards. In the merging step, we ensure that counts of equivalent cards from both halves are added up. If any card's count exceeds $ \frac{n}{k}$, it immediately returns $\texttt{True}$ with the card in question.

4. **Base Case**: The base case ensures that when a single card is left, it is counted as 1, which is then used to build up the counts in higher recursive levels.

5. **Final Check**: After combining counts from the left and right halves, the algorithm checks if any card appears more than $\frac{n}{k}$ times and returns the result if true.

### Time Complexity Analysis:

- **Divide and Conquer**: The algorithm splits the list of cards into two halves in each recursive call, which gives it a  $\log n$ factor in the time complexity, similar to merge sort.
  
- **Equivalence Testing**: In each merge step, for each card in the right half, the algorithm compares it with all the cards in the left half to check for equivalence. This takes $O(n)$ time in the worst case for each level of recursion. Hence, at each level, the merging step takes $O(n)$ comparisons.
  
- **Overall Complexity**: Since there are $O(\log n)$ levels of recursion (due to halving the list at each step), and at each level, $O(n)$ comparisons are made for equivalence testing, the time complexity of the basic divide-and-conquer approach would be $O(n \log n)$.

However, since the problem allows $k$ equivalence checks to find the set of cards that are equivalent to more than $\frac{n}{k}$, the total complexity will be $O(k \cdot n \cdot \log n)$. The $k$ factor comes in because for each card, we may have to perform equivalence checks across $k$ sets.

