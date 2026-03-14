import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("dataset.csv")

questions = data["question"]
answers = data["answer"]

# Create TF-IDF model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Chatbot response function
def get_response(user_input):

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(user_vector, X)

    index = similarity.argmax()

    return answers.iloc[index]