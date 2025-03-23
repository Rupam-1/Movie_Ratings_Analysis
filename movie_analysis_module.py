import pandas as pd

def read_data(file_path):
    encodings = ["latin1", "ISO-8859-1", "cp1252"]
    for enc in encodings:
        try:
            data = pd.read_csv(file_path, encoding=enc)
            break
        except UnicodeDecodeError:
            continue
    return data

def cleanup_data(data):
    cleaned_data = data.drop_duplicates()
    cleaned_data = cleaned_data.dropna(subset=['Name'])

    cleaned_data['Year'] = cleaned_data['Year'].fillna(data['Year'].median())
    cleaned_data['Rating'] = cleaned_data['Rating'].fillna(data['Rating'].median())

    cleaned_data['Votes'] = pd.to_numeric(cleaned_data['Votes'], errors='coerce')
    cleaned_data['Votes'] = cleaned_data['Votes'].fillna(0)

    cleaned_data['Year'] = cleaned_data['Year'].astype(int)

    cleaned_data['Duration'] = cleaned_data['Duration'].str.replace('min','')
    cleaned_data['Duration'] = pd.to_numeric(cleaned_data['Duration'], errors='coerce')
    cleaned_data['Duration'] = cleaned_data['Duration'].fillna(cleaned_data['Duration'].median())

    columns = ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']
    for col in columns:
        cleaned_data[col] = cleaned_data[col].fillna('Unknown')

    return cleaned_data

def analyze_data(cleaned_data):
    data_trends = {
        "Total Movies": len(cleaned_data),
        "Average Rating": float(cleaned_data["Rating"].mean()),
        "Median Rating": float(cleaned_data["Rating"].median()),
        "Average Duration": float(cleaned_data["Duration"].mean()),
        "Median Duration": float(cleaned_data["Duration"].median()),
        "Oldest Movie Year": int(cleaned_data["Year"].min()),
        "Newest Movie Year": int(cleaned_data["Year"].max())
    }

    best_year = cleaned_data.groupby("Year")["Rating"].mean().idxmax()
    best_year_avg_rating = cleaned_data.groupby("Year")["Rating"].mean().max()

    duration_rating_corr = cleaned_data["Duration"].corr(cleaned_data["Rating"])

    top_10_movies = cleaned_data.nlargest(10, "Rating")[["Name", "Year", "Rating", "Votes"]]
    top_movies_per_year = cleaned_data.loc[cleaned_data.groupby("Year")["Rating"].idxmax(), ["Year", "Name", "Rating", "Votes"]]

    movies_per_year = cleaned_data["Year"].value_counts()

    top_voted_movies = cleaned_data.nlargest(10, "Votes")[["Name", "Year", "Rating", "Votes"]]
    top_voted_per_year = cleaned_data.loc[cleaned_data.groupby("Year")["Votes"].idxmax(), ["Year", "Name", "Rating", "Votes"]]

    top_directors = cleaned_data["Director"].value_counts().head(10)
    actor_columns = ["Actor 1", "Actor 2", "Actor 3"]
    all_actors = pd.concat([cleaned_data[col] for col in actor_columns])
    top_actors = all_actors.value_counts().head(10)

    results = {
        "Data Trends": data_trends,
        "Best Year": int(best_year),
        "Best Year Average Rating": float(best_year_avg_rating),
        "Duration vs Rating Correlation": float(duration_rating_corr),
        "Top 10 Movies Overall": top_10_movies,
        "Top Movies Per Year": top_movies_per_year.head(10),
        "Movies Per Year": movies_per_year.head(10),
        "Top Voted Movies Overall": top_voted_movies,
        "Top Voted Movies Per Year": top_voted_per_year.head(10),
        "Top Directors": top_directors,
        "Top Actors": top_actors
    }
    return results

def final_results(file_path):
    file_data = read_data(file_path)
    cleaned_data = cleanup_data(file_data)
    results = analyze_data(cleaned_data)
    return results
    
# if __name__ == "__main__":
#     file_path = "C:\\Users\\RUPAM\\Downloads\\IMDb_Movies_India.csv"
#     a=final_results(file_path)
#     print(a)
    

