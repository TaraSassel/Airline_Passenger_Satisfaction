# Project 1 (Classification): Airline Passenger Satisfaction
## Overview
The data for this project was already divided into testing and training. However, in order to gain a better overview, they were combined. The table below provides an insight into the features available. Based on those features the passenger satisfaction was predicted which was either "satisfied" or "neutral or dissatisfied".

The pie-plot provides a very simple overview of the the percentage of satisfied and dissatisfied passanger. It becomes clear that the majority of the custommers is neutral or dissatisfied. In the initial phase, a random forest classifier and a logistic regression model will be trained. Following this, a feature selection process will be conducted, enabling the airline to identify and prioritize key features. This strategic approach allows the airline to focus on enhancing specific aspects of its service to drive passenger satisfaction.


<table align="center">
      <tr>
        <th>Feature</th>
        <th>Entries</th>
        <th>Mean</th>
      </tr>
      <tr>
        <td>Gender</td>
        <td>Female or Male</td>
         <td>NaN</td>
      </tr>
      <tr>
        <td>Customer Type</td>
        <td>Loyal Customer or Disloyal Customer</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>Age</td>
        <td>7-85</td>
        <td>39.43</td>
      </tr>
      <tr>
        <td>Type of Travel</td>
        <td>Business travel orPersonal Travel </td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>Class</td>
        <td>Eco, Eco Plus or Buisiness</td>
        <td>NaN</td>
      </tr>
      <tr>
        <td>Flight Distance</td>
        <td>31-4983</td>
        <td>1190.21</td>
      </tr>
      <tr>
        <td>Inflight wifi service</td>
        <td>0-5</td>
        <td>2.73</td>
      </tr>
      <tr>
        <td>Departure/Arrival time convenient</td>
        <td>0-5</td>
        <td>3.05</td>
      </tr>
      <tr>
        <td>Ease of Online booking</td>
        <td>0-5</td>
        <td>2.76</td>
      </tr>
      <tr>
        <td>Gate location</td>
        <td>0-5</td>
        <td>2.98</td>
      </tr>
      <tr>
        <td>Food and drink</td>
        <td>0-5</td>
        <td>3.21</td>
      </tr>  
      <tr>
        <td>Online boarding</td>
        <td>0-5</td>
        <td>3.25</td>
      </tr>   
      <tr>
        <td>Seat comfort</td>
        <td>0-5</td>
        <td>3.44</td>
      </tr> 
        <tr>
        <td>Inflight entertainment</td>
        <td>0-5</td>
          <td>3.36</td>
      </tr> 
        <tr>
        <td>On-board service</td>
        <td>0-5</td>
        <td>3.38</td>
      </tr> 
        <tr>
        <td>Leg room service</td>
        <td>0-5</td>
        <td>3.35</td>
      </tr> 
        <tr>
        <td>Baggage handling</td>
        <td>1-5</td>
        <td>3.63</td>
      </tr> 
        <tr>
        <td>Checkin service</td>
        <td>0-5</td>
        <td>3.30</td>
      </tr> 
        <tr>
        <td>Inflight service</td>
        <td>0-5</td>
        <td>3.64</td>
      </tr> 
        <tr>
        <td>Cleanliness</td>
        <td>0-5</td>
        <td>3.29</td>
      </tr> 
        <tr>
        <td>Departure Delay in Minutes</td>
        <td>0-1592</td>
        <td>14.64</td>
      </tr> 
      </tr> 
        <tr>
        <td>Arrival Delay in Minutes</td>
        <td>0-1584</td>
        <td>15.09</td>
      </tr>   
</table>

  

<!-- Figure -->

<p align="center">
  <img src="./figures/satisfaction_pieplot.png"  width="50%" height = "50%">
</p>

## Model Training
Two models were trained in parallel and evaluated against each other, a random forest classifier and a logistic regression model. These models were selected as the classification task was binary i.e. satisfied or dissatisfied. However, before training the data several steps had to be undertaken which were encoding the features that were non numerical using LabelEncoder and scaling the data using StandardScaler. After completing these steps the models were trained.

### Random Forest Classifier


<p align="center">
  <img src="./figures/Simplified_tree.png"  width="50%" height = "50%">
</p>

In a first instance a random forest classifier was trained the above figure represents a simplified decison tree from the random forest. 


<p align="center">
  <img src="./figures/confusion_matrix_rf1.png"  width="50%" height = "50%">
</p>

From the confusion matrix the recall, precision and specificity were calculated which were 0.94, 0.97 and 0.98, respectively. Please note that the dissatisfied passengers were taken as negative and satisfied clients were taken as positives. A high value in recall indicated that the model overall captured most positive cases, the precision was high as well indicating that the number of false positives was low. A very high value in specificity indicated that the model was very effective in capturing dissatisfied passengers which was very important for this project. Therefore, it can be said that the model performed well overall.

Furthremore, a random forest classifier was trained with selected features. Please refer to the notebook for more details.

### Logistic Regression 
 
<p align="center">
  <img src="./figures/confusion_matrix_lr.png"  width="50%" height = "50%">
</p>

In a second instance a logistic regression model was trained and the confusion matrix is shown above. For this model the 

### Model Evaluation
The figure below shows an ROC graph of the random forest and logistic regression model. It becomes clear that the random forest classifier outperforms logistic regression model. 

<p align="center">
  <img src="./figures/ROC.png"  width="50%" height = "50%">
</p>

## Conclusions/Suggestions 
From the model evaluation it was found that the random forest model performed best. Therefore, the feature importance was identified from this model. The figure below highlights the 10 most important features when identifying passenger satisfaction. Given that a majority of passengers expressed dissatisfaction, the recommendation for the airline is to prioritize enhancements in the following areas: Online boarding, inflight wifi service, inflight entertainment, seat comfort, ease of online booking, and leg room service. These specific features are directly managed by the airline and are essential features shaping overall passenger contentment.

<p align="center">
  <img src="./figures/feature_importance.png"  width="50%" height = "50%">
</p>
