.. probability lecture

Probability
=============

Probability provides the mathematical tools we use to model randomness:

   * Probability tells us how likely an event (Frequentist) or what
     our degree of beliefs in an event is (Bayesian)
   * Provides the foundation for statistics and machine learning
   * Often our intuitions about randomness are incorrect because we live
     only one realization
   * Enumerating all possible outcomes (using combinatorics) can help us
     compute the probability of an event


Formalization
---------------

For some sample space `S`, a probability function `P` has three properties:

:math:`P(A) \ge 0 \forall A \in S`

:math:`P(S) = 1`

:math:`\forall A_i, A_j : A_i \cap A_j = \emptyset \Rightarrow P(A_i \cup A_j) = P(A_i) + P(A_j)`

Independence
--------------

Events are independent (notation :math:`A\bot B`) if:

.. math::
   
   P(A\cap B) = P(A)P(B)

or

.. math::
      
   P(A|B) = P(A)
   
The above is known as **conditional probability**.
   
   * How could we use the definition of independence to test whether two events are independent?
   * What does knowing that B has occurred tell us about the likelihood of A?
      * Under independence?
      * Without independence?

The :math:`P(A\cap B) = P(A)P(B)` is known as the multiplication rule

A problem
---------------

Take a moment to solve this question:

   * Three types of fair coins are in an urn: HH, HT, and TT
   * You pull a coin out of the urn, flip it, and it comes up H
   * Q: what is the probability it comes up H if you flip it a second time?

So does one event provide information about the other.
     
Solution:

   :math:`P(X_1 = H) = 1/2`

   :math:`P(X_2 = H | X_1 = H) = \frac{5}{6} \ne \frac{1}{2} = P(X_2=H)`

Conditional probability	
----------------------------

:math:`P(B|A) = P(A \cap B) / P(A)`

in other words

:math:`P(X_2=H | X_1=H) = P(X_2 = H \cap X_1 = H) / P(X_1=H) = \frac{\frac{1}{3} + \frac{1}{3}\frac{1}{4}}{\frac{1}{2}}`
	
      
.. code-block:: python

   import random
   import pandas as pd

   coins = ['HH', 'HT', 'TT']
   results = []
   for i in range(10000):
       coin = random.choice(coins)
       results.append([random.choice(coin) for j in [1,2]])
   df = pd.DataFrame(results, columns=['first', 'second']) == 'H'
   df.groupby('first').mean()
		     
.. code-block:: none

          second
   first
   False  0.168256
   True   0.838502
   
		
Probability Chain Rule
--------------------------

.. note:: In probability theory, the chain rule (also called the general product rule) permits the calculation of any member of the joint distribution of a set of random variables using only conditional probabilities.


We can rearrange the formula for conditional probability to get the product rule:


   :math:`P(A,B) = P(A|B)P(B)`

We can extend this for three or more variables:

   :math:`P(A,B,C) = P(A| B,C) P(B,C) = P(A|B,C) P(B|C) P(C)`


More generally:

   :math:`P(\cap_{i}^nX_i) = \prod_i^n P(X_i | \cap_k^{i-1} X_k)`
      

Law of Total Probability
----------------------------

If :math:`\{B_n\}` is a partition of a sample space `A`, meaning :math:`\cup_i B_i = A` and :math:`B_i \cap B_j=\emptyset \forall i, j`

Then

:math:`P(A) = \sum P(A\cap B_i)`

or

:math:`P(A) = \sum P(A|B_i) P(B_i)`
      
And we call A the **marginal distribution** of B
     

Bayes Rule
---------------

Use Bayes’s Rule when you need to compute conditional probability for :math:`A|B`
but only have probability for :math:`B|A`:

:math:`P(A|B) = \frac{P(B|A)P(A)}{P(B)}`

:math:`P(\theta|x) = \frac{P(x|\theta)P(\theta)}{P(x)}`

Proof: use the definition of conditional probability

Recall that

   :math:`P(A,B) = P(B,A)`

Lets start with the conditional probability defination
      
   :math:`P(A|B) = \frac{P(A \cap B)}{P(B)}`

If we write the reverse of that	 
	 
   :math:`P(B|A) = \frac{P(B \cap A)}{P(A)} = \frac{P(A \cap B)}{P(A)}`

Then multiply by :math:`P(A)`
      
   :math:`P(A \cap B) = P(B|A)P(A)`

Then plug this back into the conditional probability.
      
Bayesian inference works by combining information about parameters :math:`\theta` contained in the observed data :math:`x` as quantified in the likelihood function :math:`p(x|\theta)`.  Classical statistics works by making inference about a single point, while Bayesian inference works on the whole distribution.  Parameters through the Bayesian lens are treated as random variables described by distributions.

Lets put Bayesian inference on hold and first look at and example of Bayes Rule.

**Predictive value positive** - Prob. person has disease given the test was positive.
   :math:`PV^{+} = P (D^{+} |T^{+})`

**Predicitve value negative** - Prob. person does not have diease given test was negative 
   :math:`PV^{-} = P (D^{-} |T^{-} )`    

**Sensitivity** - Prob. that test positive given person has disease 
   :math:`P (T^{+} |D^{+})`
   
**Specificity** - Prob. that test negative given person does not have disease 
   :math:`P (T^{-} |D^{-})`

**Prevalance** - :math:`d = P(D^{+})`
   
Note that: :math:`P (T + |D - ) = 1 - \textrm{specificity}`

Lets say we wanted to know :math:`PV^{+}`.
   
   .. math::
      :nowrap:

      \begin{eqnarray}
      P (D^{+} |T^{+}) &=& \frac{P(T^{+}|D^{+}) P(D^{+})}{P(D^{+})P(T^{+}|D{+})+P(D^{-})P(T^{+}|D^{-})} \\
                       &=& \frac{d \times \textrm{sensitivity}}{d \times \textrm{sensitivity}+(1-d) \times (1-\textrm{specificity})} 
      \end{eqnarray}
      
So if we were given

Sensitivity = 0.84, specificity = 0.77, prevalence = 0.20

Then

   .. math::
    
      PV^{+} = \frac{(0.2)(0.84)}{(0.2)(0.84)+(0.8)(0.23)}  = 0.48 \\
      PV^{-} = \frac{(0.8)(0.77)}{(0.8)(0.77)+(0.2)(0.16)}  = 0.95
