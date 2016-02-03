# Natural Language Processing / Naive Bayes

## Objectives

- Make computers read text.

- Turn raw text into features we can feed into our classifiers.

- Classify email into ham and spam.

- Find out which documents match a search most closely.

- Build a Naive Bayes classifier.

## Natural Language Processing

<br><details><summary>
What could computers do if they could read?
</summary>

1. Filter out email spam.<br>
2. Scan resumes.<br>
3. Detect plagiarism.<br>
4. Classify software bugs into different categories.<br>
5. Cluster news like Google News.<br>
6. Find out which headlines will get the most clicks.<br>
7. Find out which ad copy will get the most clicks.<br>
</details>

<br><details><summary>
What is NLP?
</summary>

1. NLP transforms unstructured text into vectors.<br>
2. These vectors can be used for machine learning applications.<br>
3. E.g. classification, clustering, regression, recommender systems, etc.<br>
4. Instead of just apply ML to numeric data with NLP we can apply it to text.<br>
</details>

<br><details><summary>
What is unstructured text? How is it different from structured text?
</summary>

1. Unstructured text is text without a schema.<br>
2. Structured text is text with a schema, e.g. CSV, JSON.<br>
3. A schema specifies column names and types for the data.<br>
4. Unstructured text has no columns, no specified types.<br>
5. Usually is just a blob of text.<br>
</details>

<br><details><summary>
What are some sources of unstructured text?
</summary>

1. Twitter, Facebook, social media.<br>
2. Legal documents.<br>
3. News stories, blogs, online comments.<br>
4. Voice recognition software , OCR, digitized documents.<br>
5. Bugs, code comments, documentation.<br>
</details>


## Text Classification

Suppose we want to classify email into spam and not spam. Consider
these two email messages.

### Email 1

> From: Joe    
> Subject: R0lex    
>     
> Want to buy cheap R0leXX watches?    

### Email 2

> From: Jim    
> Subject: Coffee    
>     
> Want to grab coffee at 4?    

<br><details><summary>
Which one of these is likely to be spam?
</summary>

Email 1.<br>
</details>


<br><details><summary>
Why?
</summary>

1. It contains words that are spammy.<br>
2. It contains misspellings.<br>
</details>

## Vectorizing Text

Now as humans we can figure this out pretty easily. Our brains have
amazing NLP. But we are not scalable. 

<br><details><summary>
How can we automate this process?
</summary>

1. Convert text into feature vectors.<br>
2. Train classifier on these feature vectors.<br>
3. Use output vectors `[1]` to mean spam, and `[0]` to mean not-spam.<br>
</details>

What is *vectorizing*?

- Vectorizing is converting unstructured raw text to feature vectors. 

Consider these two texts. 

- Text 1: `Want to buy cheap R0leXX watches?`

- Text 2: `Want to grab coffee at 4?`

<br><details><summary>
How can we vectorize them?
</summary>

1. Lowercase all words.<br>
2. Replace words with common base words.<br>
3. Count how many times each word occurs.<br>
4. Store as vector.<br>

</details>

## Vectorized Texts

Here is what the emails look like vectorized. This is also known as a
*bag of words*.

Index |Word     |Text 1   |Text 2
----- |----     |------   |------
0     |want     |1        |1
1     |to       |1        |1
2     |buy      |1        |0
3     |cheap    |1        |0
4     |r0lexx   |1        |0
5     |watches  |1        |0
6     |grab     |0        |1
7     |coffee   |0        |1
8     |at       |0        |1
9     |4        |0        |1

## Terms

Term         |Meaning
----         |-------
Corpus       |Collection of documents (collection of articles).
Document     |A single document (a tweet, an email, an article).
Vocabulary   |Set of words in your corpus, or maybe the entire English dictionary. 
Bag of Words |Vector representation of words in a document.
Token        |Single word.
Stop Words   |Common ignored words because not useful in distinguishing text.
Vectorizing  |Converting text into a bag-of-words.

## Building an NLP Pipeline

Lets build an NLP Pipeline to turn unstructured text data into
something we can train a classifier on.

```
import nltk
nltk.download('all')
```

```
# Using newsgroups data set, let's fetch all of it.
from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train')

# Subset the data, this dataset is huge.
cats = ['alt.atheism', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)
```

## Tokenizing

The first step is turning your raw text documents into lists of words.

```{.python}
from nltk.tokenize import word_tokenize
text = "This is a sentence in English. This is another one."

# Split the raw text into individual words.
document = word_tokenize(text)
print document
```

## Sentence Tokenizing

Sometimes you want to treat each sentence as a separate document.

```{.python}
from nltk.tokenize import sent_tokenize

# Split document in individual sentences
sentences = sent_tokenize(text)
print sentences

# Split individual sentences into words
corpus = []
for sentence in sentences:
    corpus.append(word_tokenize(sentence))
print corpus
```

## Question

<br><details><summary>
What are some use cases for sentence tokenizing?
</summary>

1. Classifying repetitive text that uses the same sentences.<br>
2. Classifying conversation between an airplane and a control tower.<br>
3. Classifying text generated by filling out a form.<br>
4. Breaking document down into sentences and treating each sentence as
   a document. For example, to give MPAA rating to a movie script.<br>
</details>

## Stop Words

NLTK has functionality for removing common words that show up in
almost every document.

```{.python}
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print stop_words
```

```{.python}
# Remove stop words

document = [w 
  for w in map(lambda x: x.lower(), document) 
    if not w in stopwords.words('english')]
print document
```

## Question

<br><details><summary>
What might be some applications where you don't want to remove stop
words from your text?
</summary>

1. Plagiarism detection.<br>
2. Investigating if dusty papers found in attic are a lost Shakespeare play.<br>
3. Identifying document types in Data Loss Prevention. E.g. resume, 
   insider information, legal contract, etc.<br> 
</details>

## Stemming and Lemmatization

<br><details><summary>
How will our code treat words like "watch" and "watches"?
</summary>

It will treat them as different words.<br>
</details>

<br><details><summary>
How can we fix this?
</summary>

1. Remove inflectional endings and return base form of word (known as the lemma).<br>
2. This is known as stemming or lemmatization.<br>
</details>

What is the difference between stemming and lemmatization?

- Lemmatization is more general.

- Converting *cars* to *car* is stemming.

- Converting *automobile* to *car* is lemmatization.

- Behavior depends on your toolkit.

In Python's NLTK:

- Stemming converts *cars* to *car*, but does not convert *children*
  to *child*.

- Lemmatization converts both.

## Stemming and Lemmatization Computation

Removing morphoglical affixes from words, and also replacing words with their
"lemma" (or base words: "good" is the lemma of "better").

- running -> run

- generously -> generous

- better -> good

- dogs -> dog

- mice -> mouse

Here is how to do this using NLTK. Don't try to write your own
functions for this.

```
from nltk.stem.porter   import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet  import WordNetLemmatizer

print SnowballStemmer('english').stem('running')
print WordNetLemmatizer().lemmatize('mice')
```

## N-grams

<br><details><summary>
Consider "rolex watch" vs "lets watch the game this weekend". Which
one is spam?
</summary>

The first one.<br>
</details>

<br><details><summary>
Why use N-grams?
</summary>

1. Sometimes context makes a difference.<br>
2. You want to see the words before and after.<br>
3. N-grams are strings consecutive words in your corpus.<br>
4. These are extra "features" in your data that contain more information that individual words.<br>
</details>

```
from nltk.util import ngrams

# An example of 2-grams in our "document" above.
document_bigrams = ngrams(document,2)
for p in document_bigrams: print p
```

## Bag-of-Words

How do you turn a document into a bag-of-words?

```
from sklearn.feature_extraction.text import CountVectorizer

# Divide our original text into sentences.
text = "This is a sentence in English. This is another one."
corpus = sent_tokenize(text)
print corpus

# Build a bag of words model.
c = CountVectorizer(stop_words='english')
print c.fit(corpus).vocabulary_
print c.fit_transform(corpus).toarray()
```

```
 # Building bag of words from newgroups_train text.
c = CountVectorizer(stop_words=stopwords.words('english'))
bag_of_words = c.fit_transform(newsgroups_train['data'])
print c.vocabulary_
```

## Bag-of-Words Limitations

<br><details><summary>
What are some limitations of the bag-of-words approach and
CountVectorizer?
</summary>

1. Longer documents weigh more than short documents.<br>
2. Does not consider uniqueness of words. Unique words should weigh more.<br>
3. We are losing a lot of structure. This is like a giant word grinder.<br>
4. We will address the first two issues. The third issue is part of the bargain we struck with the bag-of-words approach.<br>
5. Note: bag-of-words is not the only way to featurize text. It is simple, and surprisingly powerful.<br>
</details>

## L2 Normalization

<br><details><summary>
What is L2 normalization?
</summary>

1. Divide each vector by its L2-norm.<br>
2. Divide each vector by its magnitude.<br>
3. Divide each vector by square root of sum of squares of all elements.<br>
4. Makes long and short documents weigh the same.<br>
$$\frac{\vec{v}}{||v_i||}$$<br>
$$\frac{\vec{v}}{\sqrt[2]{\sum{v_i^2}}}$$
</details>

<br><details><summary>
What is L1 normalization? 
</summary>

Divide each vector by its L1-norm.<br>

$$\frac{\vec{v}}{\sum{|v_i|}}$$<br>
</details>

<br><details><summary>
What is L(n) normalization?
</summary>

Divide each vector by its L(n)-norm.<br>

$$\frac{\vec{v}}{\sqrt[n]{\sum{|v_i|^n}}}$$<br>
</details>

## Why L2?

<br><details><summary>
Why use the L2-norm?
</summary>

1. It makes dot products between vectors meaningful.<br>
2. Will see this later with cosine similarity.<br>
</details>

## Dot Product

<br><details><summary>
If two documents are highly similar what will the dot product of their
L2-normalized vectors be?
</summary>

The dot product will be 1.<br>
</details>

<br><details><summary>
What does a dot product of 0 indicate?
</summary>

There is no similarity between the documents.<br>
</details>

<br><details><summary>
What does a dot product of -1 indicate?
</summary>

This is not possible since all vector values are zero or positive.<br>
</details>

## TF-IDF Intuition

Intuitively, the idea of TF-IDF is this:

- Words that occur in every document are less useful than words that
  only occur in some documents.

- Instead of looking at the term frequency for each word in a document
  we want to scale up terms that are rare.

## Applications

<br><details><summary>
Which term is likely to be more significant in spam detection:
"hey", "rolex", and why?
</summary>

1. "Rolex" is going to be more significant.<br>
2. Because this is a unique word that does not occur in a lot of documents.<br>
3. "Hey" is a lot more common and is less likely to be a useful feature.<br>
</details>

## Inverse Document Frequency

How can we increase the weight of tokens that are rare in our corpus
and decrease the weight of tokens that are common?

- Use Inverse Document Frequency.

- Inverse Document Frequency or IDF is a measure of how unique a term
  is. 
  
- So we want to weigh terms high if they are unique.

What is the formula for IDF?

Suppose:

- *t* is a token

- *d* is a document

- *D* is a corpus

- *N* is the total number of documents in *D*

- *n(t)* is the number of documents containing *t*

$$idf(t, d) = \log{\left(\frac{N}{n}\right)}$$

## TF-IDF

What is TF-IDF?

- TF-IDF combines TF or the normalized token counts.
- Then it multiplies it with IDF.

What is the formula for TF-IDF?

Suppose:

- *t* is a token

- *d* is a document

- *D* is a corpus

- *N* is the total number of documents in *D*

- *n(t)* is the number of documents containing *t*

Then, TF-IDF is:

$$tfidf(t,d) = tf(t,d) * idf(t,d)$$

What is TF?

- TF is the number of times that the token $t$ appears in $d$ (often
  normalized by dividing by the total length of $d$).

$$tf(t, d) = freq(t, d)$$

What is IDF?

- IDF is a score for how unique a token is across the corpus.

$$idf(t, d) = \log{\left(\frac{N}{n}\right)}$$

- This is sometimes written with some smoothers like this:

$$idf(t, d) = \log{\left(\frac{N + 1}{n + 1}\right)} + 1$$

## Adding Ones

<br><details><summary>
Why are we adding 1's?
</summary>

1. This is called smoothing.
2. Adding 1 inside the log ensures that we never divide by 0.<br>
3. Adding 1 at the end ensures that *idf* is always non-zero.<br>
</details>


## Example

Consider a very small library with these books:

- Hadoop Handbook (HH)
- Beekeeping Bible (BB)

Here are the word frequencies.

Terms  |HH   |BB
-----  |--   |--
hadoop |100  |0
bees   |0    |150
hive   |20   |50

<br><details><summary>
Intuitively what do you expect the IDF scores of hadoop, bees, and
hive to be?
</summary>

1. Hadoop and bees should have a higher score.<br>
2. Hive should have a low score because it is not rare.<br>
</details>

<br><details><summary>
What are the IDF scores of hadoop, bees, and hive? Assume log base 2.
</summary>

1. Note these are independent of document.<br>
2. For hadoop: $N = 2, n = 1, \log(N/n) = \log(2) = 1$.<br>
3. For bees: $N = 2, n = 1, \log(N/n) = \log(2) = 1$.<br>
4. For hive: $N = 2, n = 2, \log(N/n) = \log(1) = 0$.<br>
</details>

## Computing  TF-IDF

```{.python}
import numpy as np

bag_of_words_matrix = bag_of_words.toarray()
document_freq = np.sum(bag_of_words_matrix > 0, axis=0)

# N is the number of documents
N = bag_of_words_matrix.shape[0]

# Divide each row by its l2 norm
l2_rows = np.sqrt(np.sum(bag_of_words_matrix**2, axis=1)).reshape(N, 1)
bag_of_words_matrix = bag_of_words_matrix / l2_rows

# Want a IDF value for words that don't appear in a document
idf = np.log(float(N+1) / (1.0 + document_freq)) + 1.0
print idf
```

```{.python}
from sklearn.preprocessing import normalize
tfidf = np.multiply(bag_of_words_matrix, idf)
tfidf = normalize(tfidf, norm='l2', axis=1)
print tfidf
```

It's probably easier just to do this:

```{.python}
from sklearn.feature_extraction.text import TfidfTransformer

z = TfidfTransformer(norm='l2')
print z.fit_transform(bag_of_words_matrix).toarray()
```

Or this:

```{.python}
from sklearn.feature_extraction.text import TfidfVectorizer

t = TfidfVectorizer(stop_words=stopwords.words('english'), norm='l2')
print t.fit_transform(newsgroups_train['data']).toarray()
```

## Cosine Similarity

We need a way to compare our documents. Use the cosine similary metric!

```{.python}
from sklearn.metrics.pairwise import cosine_similarity

# Use cosine similarity to measure similarity of 3 sentences in a corpus
corpus.append("English is my favorite language.")
cosine_similarity(t.transform(corpus))
```
## Hashing Trick

One of the limitations of CountVectorizer is that the vectors it
produces can be very large. 

<br><details><summary>
How can we fix this?
</summary>

1. Use `HashingVectorizer`.<br>
2. Hash words to collapse the vector.<br>
3. Vector still retains enough uniqueness to be useful.<br>
</details>

## Hashing Vectorizer

```{.python}
from sklearn.feature_extraction.text import HashingVectorizer
hv = HashingVectorizer(n_features=10)
features = hv.transform(corpus)
print features.toarray()
```

## Summarize

<br><details><summary>
What are some steps in vectorizing text?
</summary>

1. Tokenize.<br>
2. Stemming, lemmatization, lowercasing, etc.<br>
3. Count frequencies.<br>
4. Modify feature weights using TF-IDF<br>
5. Divide by L2 norm.<br>
6. Use hashing trick.<br>
</details>


