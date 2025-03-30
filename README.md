# Lung diseases dataset documentation

## Thoughts
this is my first ML project, that I decided to work on. Here, i am using the dataset provided by [@a3amat02](https://www.kaggle.com/a3amat02) on kaggle. 

The dataset includes patient data, and here is an overview:
|     |Column           |Non-Null Count  |Dtype|
|-----|-----------------|----------------|-------|
| 0   |Age              |4900 non-null   |float64|
| 1   |Gender           |4900 non-null   |object|
| 2   |Smoking Status   |4900 non-null   |object|
| 3   |Lung Capacity    |4900 non-null   |float64|
| 4   |Disease Type     |4900 non-null   |object|
| 5   |Treatment Type   |4900 non-null   |object|
| 6   |Hospital Visits  |4900 non-null   |float64|
| 7   |Recovered        |4900 non-null   |object|

although the dataset is not a very large one, and the resulting trained model won't be the most accurate, there is, it could serve a **_"fun"_** purpose for those, who are willing to try and see some predictions about ones risks and chances on the topic lung diseases.

So it well **neither** be an **exact, nor** a **trustworthy** estimator **for** one's condition as complex as **_health_**, but it could spread some awareness, that is based on pure statistics, for curiosity reasons.

## First of all, lets find our goals for the project

---

1.  **Find out gender spread lung diseases**
1. **Find out which diseases are the most dangerous and otherwise**
1.  **Find the best treatment for each disease**
1.  **Train a ML model on the given data to predict further chances based on new data**
1.  **Build a simple hosted application and host the model with the statistics and input field for user data to check on their chances for the selected stochastic model**

---

<details>
    <summary>The stochastic model will include:</summary>
   
    1. What disease does the patient tend to have #TODO

    2. Chances to survive the disease (done)
    
    3. What treatment is better for the patient regarding his data and disease #TODO
    
    4. How smoking influences his chances #TODO
    
    5. Optimal hospital visits for his disease #TODO

</details>



#### TODO's
This model will not be my main focus, becaus the dataset is not the best one for high accuracy, but i still want to add some features like:

    1. What disease does the patient tend to have #TODO
    
    2. What treatment is better for the patient regarding his data and disease #TODO
    
    3. How smoking influences his chances #TODO
    
    4. Optimal hospital visits for his disease #TODO

### Remarks
 - If you have some suggestions, or find errors, feel free to add some pull requests, and i will review them ASAP :)
 - The project is completely open-source and u can use it however you like
