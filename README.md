# Introduction

Cinema has been the cornerstone of entertainment for humans since the 20th Century. It has shaped way for innovations in film making, digital graphics and made acting a profession to be reckoned with great popularity. We have often wondered what makes for a great film, there isn't a generic recipe for success. It takes good acting, direction, cinematography, great collaboration between cast & crew and a script that can invoke emotions in people. However, there a certain parameters that can help us estimate if a film will do well (financially) even before it's release, based on audience and critics reception. This is what we are trying to achieve in our project, to predict how well a movie will do given the data about the user and critic's rating, the sentiment of the Twitter and Youtube feed and much more.

# Set-up 

We have used IMDB and Rotten tomatoes rating as they are known to be reliable and can be used as a yardstick to gauge how well a movie has fared. We have used Seaborn for visualization, to understand the correlation between the ratings and the gross worldwide collections. In addition to it we have used sentiment analysis on the tweets about the movie as well as the Youtube's Comments. We have also captured the ratio of the views to likes and dislikes on the trailer of the movie in Youtube to better undertand the expectations from the audiences. 

# Results

We have used GradientBoostingRegressor to predict the worldwide collection and achieved an r2_score of 0.98.


