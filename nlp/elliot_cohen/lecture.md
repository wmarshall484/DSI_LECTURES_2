NLP
================================

Natural Lanaguge Processing is a subfield of machine learning focused on making sense of text. Text is inherently unstructured and has all sorts of tricks required for converting (vectorizing) text into a format that a machine learning algorithm can interpret.


One thing we will be covering today (relevant for a lot of applications) is Information Retrieval (ranking of documents via a search query)


IR is a subfield of NLP focusing on identifying document similarity.

Think of  a document as something we search for in a corpus (a textual data set)

We can think of a document as an article, an email, or even just a sentence.

A good analogy for a corpus we use everyday is the web search index from google.

Text pipeline
=================================

A natural language processing pipeline allows for the creation of a bag of words
over a corpus. This bag of words is composed of a vocabulary (1 column for each
word in the overall corpus.) These bags of words are then represented by word
counts over the whole corpus, with 0 marking words as not present.

The pipeline starts with tokenization. Tokenization takes the corpus or document
and splits it in to a list of strings. This list of strings then composes up a
document.

When we translate to a bag of words, assuming we already have a vocabulary, we 
can then take the words that appear in the document and represent this as 0. Any
words that appears in the document is represented by a special token called OOV
(Out-of-Vocabulary).

```python
#Run this to setup nltk if its not setup already
import nltk
nltk.download('all')
```

```python
#Using the news groups data set, let's fetch all of the data
from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train')

#Subset the data, this dataset is huge
cats = ['alt.atheism', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
```

```python
#Tokenization example
from nltk.tokenize import word_tokenize
sentence = 'Giovanna is teaching at zipfian'
#Note how each word is an individual entry in a list.
document = word_tokenize(sentence)
print document   # ['Giovanna', 'is', 'teaching', 'at', 'zipfian']
```

The above is a tokenization example. Note that I call the list of tokens a
document. This could be any number of sentences and is purely meant as an
example.


Part of Speech Tagging
=====================================

Part of speech tagging is exactly as we remember back in english class. Given a
word, what is its part of speech? This could be a verb, noun, adverb, ...

![alt text](images/postags.png "Part of speech tags")

So there's the list. Part of speech tags are used as features in all sorts of
NLP applications. Many of these are featurization techniques that are NOT bag of
words or tfidf encoding. These are used in sequential applications with trained
conditional random fields or other sequential techniques for applications
including parse trees and named entity recognition. This is further down the NLP
pipeline.

Stop Words
=============================

If we remember from information theory/decision trees, features that do not have
that much information in them are not worth keeping around. In NLP, we call
these stop words.

```python
from nltk.corpus import stopwords
these_are_stop_words = stopwords.words('english')
word_list = []
#filter words
filtered_words = [w for w in word_list if not w in stopwords.words('english')]
print these_are_stop_words

['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now']
```

A lot of these words are very common in english and do not really differentiate
on any particular topic. There will be words like this on a per topic basis, but
these are in general agreed upon that they are bad language wide.

Sentence Segmentation
=======================================

We typically want to convert lists of tokens into sentences. If we look at an
example here:

```python
words = 'This is one sentence. This is another sentence.'
document = word_tokenize(words)
print document

['This', 'is', 'one', 'sentence.', 'This', 'is', 'another', 'sentence', '.']
```

This isn't what we want! What if instead, we do sentence boundary detection?

```python
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
sents = sent_tokenizer.tokenize(words)
print sents

['This is one sentence.', 'This is another sentence.']
```

This makes a little more sense. Now let's turn these "documents" into tokens.

```python
def to_doc(sentences):
    ret = []
    for sentence in sentences:
        ret.append(word_tokenize(sentence))
    return ret

print to_doc(sents)

[['This', 'is', 'one', 'sentence', '.'], ['This', 'is', 'another', 'sentence', '.']]
```

That looks better. Now that we have two documents, we can think about how to do
all sorts of techniques on them.

Textual Transformations/Pre processing
===================================

When we are dealing with text, there are a lot of homogenization techniques
applied to actually getting the text into a computer parseable form. An example
of this could be as simple as lower casing words so your features generalize
better. This is known as pre processing.

Pre processing techniques can happen before or after your NLP pipeline (even
during!) It really depends on what you're looking to do with text.

Context
========================
 * N grams
 * Moving Window
 * Skip Grams
 * Sequence of features

NGrams
================================

NGrams if we remember are strings of word sequences. NGrams can be individual
tokens or multi word sequences. Very similar to a moving window. An example of
ngrams:

```python
from nltk.util import ngrams
sentence = 'the rain in Spain falls mainly on the plain'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
  print grams

('the', 'rain', 'in', 'Spain', 'falls', 'mainly')
('rain', 'in', 'Spain', 'falls', 'mainly', 'on')
('in', 'Spain', 'falls', 'mainly', 'on', 'the')
('Spain', 'falls', 'mainly', 'on', 'the', 'plain')
```

How would we use this in practice? Bag of words vectorization perhaps?

```python
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_df=0.8, 
                             stop_words='english',
                             ngram_range=(1,2))
X = vectorizer.fit_transform([sentence])
print X

  (0, 8)    0.333333333333
  (0, 7)    0.333333333333
  (0, 6)    0.333333333333
  (0, 5)    0.333333333333
  (0, 4)    0.333333333333
  (0, 3)    0.333333333333
  (0, 2)    0.333333333333
  (0, 1)    0.333333333333
  (0, 0)    0.333333333333
```

Moving Window
=================

If we remember moving window, just note that ngrams are a textual moving window.

This is very similar to images.

Skipgram
==================================

the set of 1-skip-2-grams includes all the bigrams (2-grams), and in addition
the subsequences for the sentence:

```
the rain in Spain falls mainly on the plain

the in, rain Spain, in falls, Spain mainly, mainly the and on plain.
```

Sequence of Features
==================================

Feature sequencing would be used with part of speech tagging (think features per
token) to identify named entities such as people.

Unicode
===================================

```python
unicode('abcdef')
u'abcdef'
s = unicode('abcdef')
print type(s)
#stayed the same
print type(s.replace("abc","123"))
#converts to byte string
print type(str(s))
#converts to unicode
print type(s.decode('utf8'))
#encode unicode to bytestring
print type(s.encode())

def to_unicode(word):
   try:
     return word.encode('latin-1').decode('utf8')
   except:
     return ''

to_unicode(s)
```

General idea: Start with utf8, convert to unicode in the middle, write back to
bytestrings.

Big Picture
============================

Let's go over a simple example.

Sample sentence:

I banked on going to the river bank today.

Let's start with the flow:

```
Tokenization ----> Sentence segmentation ----> Stemming/Lemmatization ---->
stop words ----> Bag of words/TFIDF
```

Tokenization
=====================

```python
['I', 'banked', 'on', 'going', 'to', 'the', 'river', 'bank', 'today', '.']
```

Document Creation
======================

Remember: a document is a list of lists where each list is a list of strings
that contains one token.

```python
[['I', 'banked', 'on', 'going', 'to', 'the', 'river', 'bank', 'today', '.']]
```

lower case
=========================

```python
[['i', 'banked', 'on', 'going', 'to', 'the', 'river', 'bank', 'today', '.']]
```

Stemming/Lemmatization
=============================================

```python
[['i', 'bank', 'on', 'go', 'to', 'the', 'river', 'bank', 'today', '.']]
```

Remove stop words
=====================================

```python
[['bank', 'on', 'go', 'to', 'the', 'river', 'bank', 'today', '.']]
```

Information Retrieval
=================================================

IR is a subfield of natural language processing used for understanding similar documents. We can think of similar documents as a web search problem.

Whenever you search a website, tfidf is what a lot of websites to do bring up relevant web pages for a query.

TFIDF is a relevance measure. It is used for identifying documents that are related to a search query.

A search query itself is also a document.

If we remember documents are word counts based on a vocab. Search queries get encoded in the same way and then compared against the search engine to identify and rank candidate search results.

Documents are stored in a data structure called an inverted index. An inverted index is a reverse store of words to documents.

TO build an inverted index first a forward index mapping words to document occurrences is built.

In this case, it would look something like:

```
T[0] = "it is what it is"
T[1] = "what is it"
T[2] = "it is a banana"
```

This process is encapsulated by our tokenization process from before. Basically, we store full text documents and occurrences in a database. We use this to build an inverted index which we then do seaerch queries against.

This will look something like:

```
"a":      {2}
"banana": {2}
"is":     {0, 1, 2}
"it":     {0, 1, 2}
"what":   {0, 1}
```

Note that the inverted index is composed of our vocab.

Let's remind ourselves of the tfidf formula and dive in to what it means to be a relevance measure.

In a document d with term t:

```
tfidf(t,d) = tf(t,d) * idf(t)
```

Concretely, we take a document from the postings list (and even search queries!)

and based on the term frequencies and document frequencies compute a score for each term.

We then use this for identifying documents relevant to a search query.

Concretely:

```
idf(t, D) = log(N / (1 + number of documents containing term t ))
```

where N is the number of documents in the corpus.

idf is again the amount of information an individual word provides.

Let's run through how this works using our inverted indices.

Documents
=========================

1. I am teaching at Zipfian Academy.
2. There are students learning at zipfian Academy.
3. Students teach each other at Zipfian Academy.
4. Students are learning from other students.

The first step is to remove stop words, stem and lowercase. Now we can calculate the Term Frequency.

**Term Frequency (tf)**

| document | teach | zipfian | academy | student | learn |
| -------- | ----- | ------- | ------- | ------- | ----- |
|        1 |     1 |       1 |       1 |       0 |     0 |
|        2 |     0 |       1 |       1 |       1 |     1 |
|        3 |     1 |       1 |       1 |       1 |     0 |
|        4 |     0 |       0 |       0 |       2 |     0 |

This is our document table. Each document has word counts. Let's compute some tfidf scores.

```
tfidf(t, d) = tf(t, d) * idf(t)
idf(t, D) = log(N / (1 + number of documents containing term t) )
```

**Inverse Document Frequency (idf)**

```
| word    | df |                 idf |     idf |
| ------- | -- | ------------------- | ------- |
| teach   |  2 | `log (4 / (1 + 2))` | 0.28768 |
| zipfian |  3 | `log (4 / (1 + 3))` |     0.0 |
| academy |  3 | `log (4 / (1 + 3))` |     0.0 |
| student |  3 | `log (4 / (1 + 3))` |     0.0 |
| learn   |  1 | `log (4 / (1 + 1))` | 0.69315 |
```

After formula applications:

  
 **Term Frequency - Inverse Document Frequency (tfidf)**

| document |   teach | zipfian | academy | student |   learn |
| -------- | ------- | ------- | ------- | ------- | ------- |
|        1 | 0.28768 |     0.0 |     0.0 |     0.0 |     0.0 |
|        2 |     0.0 |     0.0 |     0.0 |     0.0 | 0.69315 |
|        3 | 0.28768 |     0.0 |     0.0 |     0.0 |     0.0 |
|        4 |     0.0 |     0.0 |     0.0 |     0.0 |     0.0 |

# Naive Bayes

## What?

Naive Bayes is one of the simpler supervised techniques (and sometimes is criticized for its naivete) but it has found a nice home in the domain of text processing and information retrieval.  We will see how the algorithm works, how to use it, and why it works so well for text data.

## Where/When?

1. n << p (# of features)
2. n somewhat small __or__ 
3. n quite large
4. streams of input data (online learning)
5. not bounded by memory (usually)
6. Multi-class

## Why?

1. Independence Assumption
2. Generative algorithm
3. Very performant... it's just counting!
4. Learns online by processing one data point at a time
5. see above (it is online and does incremental processing) ^^
6. Each class has a different parameterization (through CPTs)

### Why Text?

Text data happens to fit very nicely to the bullet points of __Where/When__ to use Naive Bayes.  Due to bag of words featurization of text, the input feature matrix is often very wide (~10,000 - 50,000 columns/dimensions) and can even be greater than the number of data samples (n << p).

Often in the text classification problem, we have the text of articles/documents and would like to classify the article to its appropriate topic/categorization (e.g. sports, politics, arts, etc.).

### Example: Spam Detection

It is often illuminating to look at where (and why) techniques have come from to better understand their motivation, strengths, and weaknesses.  Naive Bayes technically can be traced back to the formulation of Bayes Theorem, but it was first extensively studied as a supervised classifier in the [1960s](). 

It really came into its own however in the [late 1990s](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering#History) as email became increasingly popular.  And most famously it was [popularized](http://www.paulgraham.com/spam.html) as a technique to filter spam emails by Paul Graham (of Y Combinator fame).

But why was spam email the "[killer app](http://en.wikipedia.org/wiki/Killer_application)" for Naive Bayes?

### Constraints of Service-wide Spam detection

Let us think about the problem of spam... If you are Google, you have millions of users who receive emails daily.  But the pattern of email is quite particular as compared to other datasets: a user receives a single email at a time and before you (Google) pass the email to their inbox you need to determine at that immediate moment whether or not it is spam.  So why not another classifier?

To be a successful feature of an email client, spam detection needs to:

1. Have __low False Negatives__ (you don't want your boss's email to go in your spam folder)
2. Be fast to predict (to deliver emails in a timely manner)
3. Train fast on all of your data... or incrementally update (the stream of emails is not stopping anytime soon)

Keep these constraints in mind as we walk through the algorithm itself and think what would happen with another model (such as kNN) in the use case of spam detection.

## Naive Bayes Intuition
We are going to be calculating the "probability" that an article belongs to each class. It's important to note that this will not be a true probability, but it will enable us to rank the classes to figure out which is the most likely.

Here's Bayes Rule applied to our scenario. *x* here is a word, *c* is the class (article topic). *X* is the document text of a specific document. The *x<sub>i</sub>*'s are all the words in the given document.

![bayes](images/bayes_rule.png)

### Naivite of Naive Bayes
We make a BIG assumption here that the occurrences of each word are *independent*. If they weren't, we wouldn't be able to just multiply all the individual word probabilities together to get the whole document probability. Hence the "Naive" in *Naive Bayes*.

Take a moment to think of how absurd this is. A document that contains the word "soccer" is probably more likely to contain the word "ball" than an average document. We assume that this is not true! But it turns out that this assumption doesn't hurt us too much and we still have a lot of predictive power. But the probabilities that we end up with are not at all true probabilities. We can only use them to compare which of the classes is the most likely.

## The Algorithm

![](images/naive-bayes.png)

For every document, we calculate the probability that the document belongs to each class and chose the class with the highest probability.

To do this, we need to calculate two things:
* **Priors:** The probability that a generic document belongs to each class: *P(c)*
* **Conditional Probabilities:** The probability that each word appears in each class: *P(x|c)*

So how do we actually get all those probabilities? *It's just counting!* We count occurrences in our training set to get approximations of the probabilities.

### Priors
The priors are the likelihood of each class. Based on the distribution of classes in our training set, we can assign a probability to each class:

![priors](images/priors.png)

Take a very simple example where 3 classes: sports, news, arts. There are 3 sports articles, 4 politics articles and 1 arts articles. This is 8 articles total. Here are our priors:

![priors examples](images/priors_example.png)


### Conditional Probability Table
The first step is building the *Conditional Probability Table (CPT)*. We would like to get, for every word, the count of the number of times it appears in each class. We are calculating the probability that a random word chosen from an article of class *c* is word *x*.

![conditional probability](images/conditional_prob.png)

Again, let's take our example. Let's look at the word "ball". Here are the occurrences in each of the 8 documents. We also need the word count of the documents.

| Article    | Occurrences of "ball" | Total # of words |
| :--------- | --------------------: | ---------------: |
| Sports 1   |                     5 |              101 |
| Sports 2   |                     7 |               93 |
| Sports 3   |                     0 |              122 |
| Politics 1 |                     0 |               39 |
| Politics 2 |                     0 |               81 |
| Politics 3 |                     0 |              142 |
| Politics 4 |                     0 |               77 |
| Arts 1     |                     2 |              198 |

Here are the values in the CPT table for the word "ball". We will do these calculations for all the words that appeared in the training documents.

![cpt example](images/cpt_example.png)


### Maximum Likelihood Estimation
We need to pull this all together to use these calculations to make a prediction. Here, *X* is the content of an article and *x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ...* are the words that make up the article.

![mle](images/mle.png)

We assign the article that has the largest probability. Note that since we made our incredibly naive assumption, these "probabilities" will not add to 1.

In our example, if we had the very short article of `The Giants beat the Nationals`, we would do the following calculations:

![mle example](images/mle_example.png)

The first probability is the prior, and the remaining come from the Conditional Probability Table. We make the same calculation for each of the 3 classes and choose the class with the biggest probability.

### Zero Probabilities
If a word has never before appeared in a document of a certain class, the probability will be 0. Since we are multiplying the probability, the whole probability becomes 0! We basically lose all information.

In the above example, since "ball" never appears in a politics article in the training set, if it appeared in a new article, we would say that there was a 0% chance that that was a politics article. But that's too harsh!

How can we fix this?

The simplest option is to replace these zeros with a really small value, like 0.00000001.
The better option is *Laplace Smoothing*.

#### Laplace Smoothing
Laplace Smoothing is assuming that every word has been seen by every article class one extra time. One way of thinking of it is that we add a new document to every class which has every word in it exactly once. This will guarantee that no value will be 0. So we modify our calculations of the probabilities slightly.

Here's our new conditional probability with Laplace smoothing.

![conditional probability with smoothing](images/conditional_prob_smoothing.png)

The standard is to use 1 as the smoothing constant, but in theory we could assume every word appeared half a time or something like this. This gives us a *smoothing constant*, which is a parameter we can tune:

![conditional probability with smoothing](images/conditional_prob_smoothing_constant.png)


### Log Likelihood
These probability values are going to get *really small*. Theoretically, this is not an issue, but when a computer makes the computation, we run the risk of *numerical underflow*. To keep our values bigger, we take the log. Recall that this is true: `log(ab) = log(a) + log(b)`

So when we calculated the MLE, we actually calculate the *log maximum likelihood error*.

![log mle](images/log_mle.png)

Recall that if `a > b` `log(a) > log(b)` so we can still find the maximum of the log likelihoods.

### Summary of Naive Bayes Algorithm
* **Training**: Calculate the priors and Conditional Probability Table
* **Predict**: Calculate the MLE for the new article for each label and pick the max

## One Bayes, many models

1. Multinomial Bayes
2. Bernoulli Bayes 
3. Gaussian Bayes

## The fun of Bayes

In theory you can use any prior distribution and any distribution for each feature

