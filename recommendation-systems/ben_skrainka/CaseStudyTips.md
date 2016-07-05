My advice is:

0. Understand that the case study will be frustrating because it is hard to beat GraphLab out of the box
1. Follow CRISP-DM — do some quick EDA and think about business problem: i.e, rating or ranking recommender
1. Get a basic recommender working
2. Read documentation and think about the best kind of recommender to use:  is a rating or a ranking recommender better for your business problem
3. Think about how to add side information.

The best solutions used a ranking factorization recommender: https://dato.com/products/create/docs/generated/graphlab.recommender.ranking_factorization_recommender.RankingFactorizationRecommender.html

Make sure they set the `unobserved_rating_value`.  They will need to play with this.  It can make a big difference.  Also, increasing `num_factors` above the default seemed to help.

By far the best solutions in our class were by Ellen Weir & Emily Spahn.
