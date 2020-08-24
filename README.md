# Final Project for 2020 Georgia Tech Data Analytics Bootcamp

Have you ever watched a movie and ended up disappointed with the outcome? Our project focused on designing models to predict IMDB movie ratings based on genre, year of release, budget, duration, and director.

## Objective

For this project, we used various models to determine the best method for predicting the IMDB rating of a movie based on historical data. In order to conduct this predictive modeling endeavor, we sourced our data from [Kaggle.com](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset/) which featured a set of CSV files with information regarding movies rated by IMDB users dating back from 1906 to 2019.

Link to Dataset: https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset/

Prototype/Inspirations: https://netflix.com

Heroku app: https://clarke-imdb.herokuapp.com/

### Methods Used
* Data Cleaning
* Data Visualization

### Technologies
* Python
* Pandas
* Jupyter
* Javascript
* D3
* HTML
* CSS
* Machine Learning Models: 
  - Support Vector Model
  - Deep Learning
  - Logistic Regression 
  - Random Forest
* DataTables
* Flask
* PostgreSQL

## Project Description
### Site Design
Our site was designed using HTML and CSS. We wanted our site to be easily navigated, and fun to use. We highlighted important elements on our homepage and showed our project process through navigational links. 

### Data Cleaning


## Tableau Visualizations
We used Tableau to create dashboards with visualizations that looked at factors we believed would affect the movie's IMDB ratings. The concepts we focused on were Release Year, Genre, and Directors.

### Release Year Dashboard
Throughout our lives, we have heard that a movie was "ahead of its time." The year a movie was released can make or break the success of the film. In this dashboard, we used Tableau visualizations to see how the year a movie was released affected its' IMDB rating. We used a scatter plot to look at the total movie budgets for every year and we compared that to the average budget a movie received in that year. The first line graphed shows how many people voted every year. The last graph shows how many movies were released in total for that year. 

On average since IMDB was created in 1990 movies that have been out longer having received more interaction and more votes than newer released movies. Also since the data was scraped in 2019, most of the movies in 2019 were not able to get as much interaction as those released in earlier years. The early 2010s have the highest amount of voter interaction, highest total budget, and most movies released. However, the early 2000s and 2019 boasted a higher average budget for every movie. All of these factors affect the IMDB score on our prediction tool. 

![](static/Images/release_year.png)

### Genre Dashboard
A huge factor in a movie's success is the genre. This dashboard is split into three graphs each one looking at a different factor affecting the success of each genre. The options for the genre are Action, Adventure, Animation, Biography, Comedy, Crime, Drama, Family, Fantasy, Horror, Music, Musical, Romance, Sci-Fi, Sport, Thriller, and Western. The first graph shows the budget. For the most part, the genre's with the higher average budgets have larger amounts of good and excellent films and far fewer bad films. With some notable exceptions like Sci-Fi and Music.

The next bar graph visuals how the number of voter interactions or the popularity of a genre can affect its' success. Once again the left side of the graph shows that the more popular genres show more good and excellent films while the less popular genres have more red/bad movies represented. The last graph spanning the bottom half of the dashboard examines whether female or male voters make a difference in the average rating a movie in a particular genre receives. On average women give higher scores than men, the only exception being in the genre of Mystery.  
![](static/Images/genre_dashboard.png)

### Director Dashboard

The directors we have shown are the more popular directors with the most votes and data. We used directors as one of our elements for the prediction models as well. Here we are showing the director data comparison of gender vs rating and budget vs rating.

For gender vs rating showing green from 0-7.3 and blue 7.4 to 8. For these particular directors, we noticed that all of them are male and the male gender voted for the highest rated directors. But on the far left side of the gender vs rating, we have Martin Scorsese, who is known for The Godfather has the highest rating votes but not the highest budget for movies.

From the budget vs rating dashboard, we see Anthony Russo known for The Avengers and Captain America is showing the highest avg budget of 230 million with an average vote of 8 but he's not the highest-rated director. So we see just because someone has a higher budget doesn't mean they are the most popular voted director.

![](static/Images/directors_dashboard.png)
## Machine Learning Model

Given the analysis that we did in Tableau, we decided to predict the movie’s rating class based on release year, duration, budget, genre, and director. We started with a linear regression model and elasticnet, but the accuracy was around 10%. So we figured that no amount of hyper-parameter tuning would get us much higher than that. For some models, we tried only using the numerical features (year, duration, and budget) but the results were not better so we decided to move forward with both numerical and categorical data.

### Deep Learning

![](static/Images/dl-final.png)

### Support Vector Model (SVM)

For the SVM we cleaned the data with label and dummy encoder to get better accuracy for our target rating class for bad excellent and good. We have the SVM training accuracy at 0.91% and SVM testing accuracy at 0.64%. 

![](static/Images/svm-final.png)

### Logistic Regression

![](static/Images/lr-final.png)

### Random Forest

![](static/Images/rf-final.png)
![](static/Images/random_forest.png)
