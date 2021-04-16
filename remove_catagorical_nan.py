subset = []
for col in dataset.columns:
    if dataset[col].dtype.name == 'object':
        subset.append(col)
dataset.dropna(subset = subset)
