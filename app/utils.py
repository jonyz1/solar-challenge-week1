import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(countries):
    frames = []
    for country in countries:
        file = f"../data/{country.lower().replace(' ', '_')}_clean.csv"
        df = pd.read_csv(file)
        df["Country"] = country
        frames.append(df)
    return pd.concat(frames, ignore_index=True)

def plot_boxplot(df, metric):
    plt.figure(figsize=(6, 3))
    sns.boxplot(x="Country", y=metric, data=df, palette="Set2")
    plt.title(f"{metric} Distribution by Country")
    plt.ylabel(metric)
    plt.grid(True)
    fig = plt.gcf()
    return fig

def get_summary_table(df):
    summary = df.groupby("Country")[["GHI", "DNI", "DHI"]].agg(["mean", "median", "std"])
    summary.columns = ['_'.join(col) for col in summary.columns]
    return summary.reset_index()

def plot_avg_metric_bar(df, metric):
    avg_metric = df.groupby("Country")[metric].mean().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.barplot(x=avg_metric.values, y=avg_metric.index, palette="viridis", ax=ax)
    ax.set_title(f"Average {metric} by Country")
    ax.set_xlabel(f"Average {metric}")
    return fig
