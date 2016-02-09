## Singular Value Decomposition

Consider these golf scores.

    A = Alice
    B = Bob
    C = Chi
    H = Hole

    H A B C 
    - - - - 
    1 4 4 4 
    2 5 5 5 
    3 4 4 4 
    4 3 3 3

We can represent them with this matrix.

$
\left[ \begin{matrix}
4 & 4 & 4 \\ 
5 & 5 & 5 \\ 
4 & 4 & 4 \\ 
3 & 3 & 3 \\
\end{matrix} \right]
$

$ 
PredictedScore = HoleDifficulty * PlayerAbility
$ 


$
\left[ \begin{matrix}
4 & 4 & 4 \\ 
5 & 5 & 5 \\ 
4 & 4 & 4 \\ 
3 & 3 & 3 \\
\end{matrix} \right]
= 
\left[ \begin{matrix}
4 \\
5 \\
4 \\
3 \\
\end{matrix} \right]
\times
\left[ \begin{matrix}
1 && 1 && 1 
\end{matrix} \right]
$

Turning these into unit vectors.

$
\left[ \begin{matrix}
4 & 4 & 4 \\ 
5 & 5 & 5 \\ 
4 & 4 & 4 \\ 
3 & 3 & 3 \\
\end{matrix} \right]
= 
\left[ \begin{matrix}
0.49 \\
0.62 \\
0.49 \\
0.37 \\
\end{matrix} \right]
\times
\left[ \begin{matrix}
14.07
\end{matrix} \right]
\times
\left[ \begin{matrix}
0.58 && 0.58 && 0.58 
\end{matrix} \right]
$


