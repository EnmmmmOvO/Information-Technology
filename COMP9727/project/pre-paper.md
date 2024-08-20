The Neural Collaborative Filtering (NCF) model we use combines collaborative and content-based filtering. It employs embeddings for users and news items, capturing latent features from their interactions. The model processes TF-IDF vectors of the user's reading history and the current news article, calculated as the mean over title, abstract, category, and subcategory. These features are then combined to create a rich representation of user preferences and item characteristics. The final output is a probability score, predicting the likelihood of a user clicking on a specific news article. Both user IDs and news IDs are encoded using label encoders to ensure consistency. This approach effectively leverages comprehensive user interaction data and rich news content for accurate recommendations.





We also have a simple deep learning model, we employed the TF-IDF method with a maximum of 5000 features, combining news titles and abstracts for vectorization. we also extracted entities from each news article and used pre-trained entity embeddings. By averaging these embeddings, we obtained a semantic representation for each article, and then we merged the TF-IDF vectors with the entity embedding vectors. This approach captures both statistical and semantic information, providing a rich feature set for each news article.

For user profile modeling, we averaged the feature vectors of all the news articles a user clicked on, representing the user’s interests. This method captures overall interest distribution and is computationally suitable for large-scale recommendation systems.

In the recommendation generation step, we used cosine similarity to match user profiles with news articles. To improve system performance, we introduced a deep learning model using PyTorch. This feedforward neural network includes an input layer, two hidden layers with Batch Normalization and ReLU activation, and Dropout layers to prevent overfitting. This model aims to learn complex relationships between user interests and news content, enhancing recommendation accuracy.



This is the result of we can see that the NCF is the best, MF and Deep Learning model relatively low. The other two we don't have a result for now due to the amount of training we're doing. But we thinks it is better than other.

The context of news recommendation, the TF-IDF and entity embedding combined with a deep learning model requires manual feature design and extraction, which can be labor-intensive and might struggle to capture complex relationships.

Matrix Factorization (MF) handles sparse and incomplete data well, reduces the dimensionality and complexity of the data, and is effective in modeling latent factors in user-item interactions. However, it can suffer from overfitting and underfitting problems, which may affect the accuracy.



Neural Collaborative Filtering (NCF) is able to understand high-dimensional sparse data, and its embeddings can capture interactions and extract features, providing a deep learning approach to co’llaborative filtering.



LibFM (Factorization Machines) performs well with high-dimensional sparse data and captures feature interactions, providing more expressiveness than linear models.

GNNs (Graph Neural Networks) excel in capturing complex high-order relationships between users and news articles, modeling deeper interactions through message-passing mechanisms.

That is all of our presentation. If there are any issues, we are willing to correct, thanks for listening.