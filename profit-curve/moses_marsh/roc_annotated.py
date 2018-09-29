def roc_curve(model, X_test, y_test, threshold=None, plot=True):
    """
    DESCRIPTION:
        Take a numpy array of the predicted probabilities and a numpy array of the
        true labels.
        Return the True Positive Rates, False Positive Rates and Thresholds for the
        ROC curve.
        If you include the threshold you want to look at it scores the model
    INPUTS:
        model - classifier model
        X_test - X test set
        y_test - y test set
        plot - boolean (default=True)
    OUTPUTS:
        tpr - (list) true positve rate
        fpr - (list) false positive rate
        thresholds - (list) thresholds for the rates
    """
    if threshold is not None:
        pred = model.predict_proba(X_test)[:, 1] > threshold
        print("Accuracy:{}\nPrecision:{}\nRecall:{}\nF1:{}\nROC AUC:{}\n"\
              .format(metrics.accuracy_score(y_test, pred),
                      metrics.precision_score(y_test, pred),
                      metrics.recall_score(y_test, pred),
                      metrics.f1_score(y_test, pred),
                      metrics.roc_auc_score(y_test, pred)))
    tpr = []
    fpr = []
    thresholds = []
    tp = 0.
    fp = 0.
    probabilities = model.predict_proba(X_test)[:, 1]
    labels = y_test
    for p, label in sorted(zip(probabilities, labels), reverse=True):
        if label == 1:
            tp += 1.
        else:
            fp += 1.
        tpr.append(tp / labels.sum())
        fpr.append(fp / (len(labels) - labels.sum()))
        thresholds.append(p)
    if plot:
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        plt.plot(fpr, tpr)
        plt.xlabel("False Positive Rate (1 - Specificity)")
        plt.ylabel("True Positive Rate (Sensitivity, Recall)")
        plt.title("ROC plot")
        lst_t = 1
        # Plot threshold
        for t, x, y in zip(thresholds, fpr, tpr):
            if (lst_t - t) > .1:
                ax.annotate('%0.2f' % t, xy=(x, y), textcoords='data')
                lst_t = t
        plt.show()
    return tpr, fpr, thresholds
