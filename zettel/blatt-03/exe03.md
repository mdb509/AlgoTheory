---
date: 25.10.2024
author: Kai Malaka (km324) 5518467 -> Gruppe 4; Manuel DiBiase (md509)  5515822 -> Gruppe 4
---

# exerxise sheet 02

## exe. 1 

### a) 

**Counterexample:**

Given a set of rational numbers $Y = \{0.0,0.75,1.0,1.5,1.75,2.5\} $. 

Algorithmn $\Alpha$ would return solution $S_1 = \{[0.75,1.75],[0.0,1.0],[2.5,3.5]\}$  but an optimal solution would be $S_2 = \{[0.0,1.0],[1.5,2.50]\}$

$\Alpha$ is stuck in a local minimum, without considering future coverage intervalls. 

### b) 

**An optimal greedy algorithm would be:**

1. Sort the points in $ X $ in ascending order.
2. Start with the leftmost uncovered element $ x \in X $.
3. Append the interval $[x, x+1]$ to $ S $.
4. Remove all elements $ x \in X $ that are covered by $[x, x+1]$.
5. Repeat steps 2–4 until the set $ X $ is empty.



**Proving Optimality with an Exchange Argument:**

Assume there is a optimal solution $ S_1 $ and an solution $ S_2$, which is produced by our greedy algorithm. 

**Exchange Argument:** Starting from the leftmost element $ x $ in $ X $, $ S_2$ covers it with the interval $[x, x+1]$, which covers all elements from $ x $ to $ x + 1 $.

If $ S_1 $ uses an interval that covers $ x $ but does not start at $ x $, we can replace it with the interval $[x, x+1]$ from $ S_2$. This replacement does not increase the total number of intervals, but it aligns $ S_1$ more closely to $ S_2$.

**Repeat the process:** Move to the next leftmost point beyond $ x+1 $ and repeat the replacement process.

In the end, we will have replaced all intervals in $ S_1$ with intervals from $ S_2$, without increasing the number of intervals in $ S_1 $.

Therefor the solution produced from greedy algorithm is optimal.





## 3



$$
\begin{align*}
NN &= m * a + (n - m) * b\\
OPT &= k * a + (n - k) * b\\
m &\leq \frac{k}{2}\leq k \leq n \\\\
\frac{NN}{OPT} &\leq \frac{m * a + (n - m) * b}{k * a + (n - k) * b}\\
&{\leq} \frac{\frac{k}{2} * a + (n - \frac{k}{2}) * b}{k* a + (n - k) * b}\\
&{\leq} \frac{\frac{k}{2} * a + n*b - \frac{k}{2}* b}{k* a + n* b - k * b}\\
&{\leq} \frac{\frac{n}{2} * a + n*b - \frac{n}{2}* b}{n* a + n* b - n * b}\\
&{\leq} \frac{n(\frac{1}{2} * a + b - \frac{1}{2}* b)}{n*(a + b - b)}\\
&{\leq} \frac{\frac{1}{2} * a + b - \frac{1}{2}* b}{a + b - b}\\
&{\leq} \frac{\frac{1}{2} * a +\frac{1}{2}* b}{a}\\
&{\leq} \frac{\frac{1}{2} * (a + b)}{a}\\
&{\leq} \frac{a + b}{2*a}\\
\end{align*}
$$
