Matts Pandas and Matplotlib Lectures
====================================

These lectures introduce the pandas and matplotlib libraries.

## Morning: Pandas

This lecture is adapted from Ming Huang's, which seems to have a long history.  I cleaned up a few things, and added a few points I think are important, but the content from Ming's lecture is mostly unchanged.

### Objectives

- Create `Series` and `DataFrame`s from Python data types. 
- Create `DataFrame`s from on disk data.
- Index and Slice `pandas` objects.
- Aggregate data in `DataFrame`s.
- Join multiple `DataFrame`s.

## Afternoon: Matplotlib

I added this lecture in response to some consistent feedback I got from students across a couple of chorts.  This lecture gives a wide overview of good practice in matplotlib.  The

```python
fig, axs = plt.subplots(n_rows, n_columns, figsize=...)
```

pattern is emphasized, as this is very flexible.  We do not introduce shortcuts, but I do mention them verbally at the end of class.

### Objectives

- Import `pyplot` and set up a professional style.
- Create `fig` and `ax` or `axs` objects with `plt.subplots`.
- Make titles and labels.
- Draw scatterplots on an axis.
- Draw line plots on an axis.
- Draw a bar chart on an axis.
- Some shortcuts for common tasks from Pandas.
