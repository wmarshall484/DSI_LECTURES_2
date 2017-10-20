# Cost Benefit Matrices and Profit Curves

We've seen Confusion Matrices and ROC curves as a way to demonstrate the trade-off between False Positives and False Negatives. This is often referred to as the Precision - Recall tradeoff.

In information retrieval (IR), `Precision` is the fraction of retrieved instances (e.g. search results) that are relevant. `Recall` is the fraction of relevant results retrieved. You can imagine two competing IR models -- one that returns a highly-curated list of only the most relevant results, but as a result, fails to retrieve some relevant results (high precision); and a second model that returns all relevant results, but a bunch of junk as well (high recall).

`Precision = TP / (TP + FP)`  
`Recall = TP / (TP + FN)`

Put another way, would you rather over predict True and get lots of *False Positives* or over predict False and get lots of *False Negatives*?

In the case of a spam filter, it's preferable to miss some spam and let it through to your inbox, than to catch all spam at the risk of also catching ham. Thus we care more about minimizing False Positives than False Negatives. In the case of fraud, it's the opposite -- we would rather catch all potential fraud at the risk of flagging non-fraudulant activity -- thus we care more about minimizing False Negatives than False Positives.

But *how much more* do we care about FP than FN (or vice versa)? How do we figure out where the sweet spot is?

A *profit curve* enables us to see the the tradeoff in monetary terms, so we can pick a threshold that maximizes profit!

## Confusion Matrix and ROC Curve Review

Recall the confusion matrix (as oriented in `sklearn` for consistency):

|                | Predicted No   | Predicted Yes  |
| -------------- | -------------- | -------------- |
| **Actual No**  | True negative  | False positive |
| **Actual Yes** | False negative | True Positive  |


Note: Different texts will sometimes orient the confusion matrix differently, with FN and FP swapped. *sklearn has TN in the upper left!* Eyes akimbo!

If you'd like to review all the terms associated with the confusion matrix, check the [Wikipedia page for Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix).

Models like Logistic Regression have a threshold that we can vary to make a tradeoff between FN and FP. We can visualize this with an ROC curve.

![ROC_curve](https://docs.eyesopen.com/toolkits/cookbook/python/_images/roc-theory-small.png)

The best model to pick really depends on our circumstances. We can use *Cost-Benefit Matrices* and *Profit Curves* to be more rigorous about this choice.

You can review our first day of classification [here](https://github.com/gschool/dsi-logistic-regression/blob/master/pair.md).

## Cost Benefit Matrix

The first step is to assign a dollar amount to each of the four cells in the confusion matrix.

Say that our classifier is detecting whether a credit card charge is fraudulent. If we think a charge is fraudulent, we will call the customer, which costs us $5. If, however, we catch a fraudulent charge, we save ourselves $100. Since it still costs us the $5, we gain $95.

Here is our Cost-Benefit Matrix:

|                | Predicted No   | Predicted Yes  |
| -------------- | -------------- | -------------- |
| **Actual No**  | 0              | -5             |
| **Actual Yes** | 0              | 95             |

Note that this is built off the baseline of never detecting fraud at all. Also note that the profit could theoretically go negative if we over detect fraud and have our customer service center calling too much.

### Expected Profit

The expected profit of a model is the expected value of the money we will make *per user* by deploying it.

We can calculate this by multiplying the entries of the Cost-Benefit Matrix by the entries of the Confusion Matrix and summing all the values and dividing by the total number of users.

Take a look at the following example Confusion Matrix.

|                | Predicted No   | Predicted Yes |
| -------------- | -------------- | ------------- |
| **Actual No**  | 818            | 307           |
| **Actual Yes** | 11             | 114           |


Note for this Confusion Matrix we have an accuracy of 0.746, precision 0.271 and recall 0.912.

```
Accuracy = (TP + TN) / (TP + TN + FP + FN) = (114 + 818) / (114 + 818 + 307 + 11) = 0.746
Precision = TP / (TP + FP) = 114 / (114 + 307) = 0.271  
Recall = TP / (TP + FN) = 114 / (114 + 11) = 0.912
```

Here's our calculation for expected profit:

```
Total # of users = 114 + 307 + 11 + 818 = 1250

E(profit) = (114 * 95 + 307 * -5 + 11 * 0 + 818 * 0) / 1250
          = 9295 / 1250
          = 7.436
```

In `numpy` that is:
```
costs = np.array([0, -5, 0, 95]).reshape(2,2)
freqs = np.array([818,307,11,114]).reshape(2,2)
probs = freqs / freqs.sum()
expected_profit = np.tensordot(probs, costs)  
```

The expected profit is given by the sum of the element-wise product of the confusion matrix and cost-benefit matrix.

Now take a look at the following Confusion Matrix. This may look like it does a better job at prediction (higher overall accuracy), but given our costs, it's worse in terms of profit.

|                | Predicted No   | Predicted Yes |
| -------------- | -------------- | ------------- |
| **Actual No**  | 1104           | 21           |
| **Actual Yes** | 78             | 47           |

Here we have an accuracy of 0.921, precision 0.376 and recall 0.691.

```
E(profit) = (47 * 95 + 21 * -5 + 78 * 0 + 1104 * 0) / 1250
          = 4360 / 1250
          = 3.488
```

Our profit is much worse!

## Profit Curve

Just as an ROC Curve shows the false-positive rate and true-positive rate for a model (or set of models) as a function of the positive class probability threshold, a profit curve shows *profit* as a function of probability threshold.

For every possible threshold, we calculate the associated confusion matrix. Then we can calculate the profit as shown above.

Here's what a profit curve will look like:

![Profit Curve](http://pltalot.com/2016/12/11/galvanize-week-4/imgs/profit_models.png)

The dotted gray line shows the profit curve of a random model, so our profit curve should always be above this line.

Here's the pseudocode for computing the profit curve.

```
function profit_curve(costbenefit_matrix, predict_probas, labels):
    Sort instances by their prediction strength (the probabilities)
    For every instance in increasing order of probability:
        Set the threshold to be the probability
        Set everything above the threshold to the positive class
        Calculate the confusion matrix
        Compute the expected profit:
            - multiply each of the 4 entries in the confusion matrix by
            their associated entry in the cost-benefit matrix
            - sum up these values
            - divide by the total number of data points
    return a list of the profits
```

Note the similarity to the pseudocode for the [ROC curve](https://github.com/zipfian/logistic-regression/blob/master/pair.md)!

Now, let's look at some code samples in `precision-recall.ipynb`

And finally let's look at some remedies for imbalanced classes.
See: `Profit_Curves_and_Imbalanced_Classes.pdf` and `class_imbalance.ipynb`
