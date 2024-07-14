# models/collaborative_filtering.py
from surprise import SVD, Dataset, Reader

def train_collaborative_filtering(data):
    reader = Reader(rating_scale=(1, 5))
    dataset = Dataset.load_from_df(data[['user_id', 'content_id', 'rating']], reader)
    trainset = dataset.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    return algo

if __name__ == "__main__":
    data = pd.read_csv('data/user_interactions.csv')
    model = train_collaborative_filtering(data)
    print("Collaborative Filtering model trained successfully!")
