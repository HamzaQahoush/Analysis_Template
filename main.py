import  pandas as pd

data = {'Question1': ['yes', 'no', 'yes', 'don’t know', 'yes', 'no', 'don’t know']}
df = pd.DataFrame(data)



def compute_count_percent(df, column_name):
    # Get the value counts
    counts = df[column_name].value_counts()

    # Calculate the total number of responses
    total = len(df[column_name])

    # Calculate the percentage for each unique value
    percentages = (counts / total) * 100
    output = pd.DataFrame()

    # Create new columns for counts and percentages
    for value in counts.index:
        output[df[f"{value} count"]] = counts[value]
        output[[f"{value} %"]] = percentages[value]

    return output


df = compute_count_percent(df, 'Question1')