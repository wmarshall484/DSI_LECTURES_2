## NMF Lecture

I setup NMF on the board. Since we do SVD the day before, it's an easy jump to NMF (just remove the singular value matrix, declare k, and require all values are non-negative).

Now that we have the setup, why is it cool? Talk about how to interpret it and how to use the latent factors to find item-item or user-user similarities using cosine similarity. Notice this is a sort-of dimensionality reduction thing.

Now talk about how to solve NMF using ALS.

Then show [this notebook](nmf-example.ipynb) to drive it all home. Props to Zach Alexander for building this notebook!

Also, tell the students if they are interested in this model, read the [NMF Paper](nmf_nature.pdf).

