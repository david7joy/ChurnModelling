### Survival Analysis 
This is generally defined as methods for analyzing data where the outcome variable is the time until the occurrence of an event of interest or it tries to predict time-to-event. The event can be death, occurrence of a disease, marriage, divorce, etc basically "an event of interest". 

The advantages of Survival analysis is that it : 
- Models time to failure or event
- Is able to account for censoring ( right, left or between)
- Compares survival between 2+ groups,segments or achetypes 
- Assess relationship between covariates and survival time

##### Kaplan-Meier Method: 

This works well for small data sets. Since we are using python, we can use Cam Davidson-Pilon's lifelines library to get started.This will help us estimate the 'Survival function, S(t) that defines the probability of surviving longer than time t'.
We can observe that approx 25% customers churn by 23 weeks who have single phone line whereas it takes 43 weeks for multiple phone line customers to churn. Thats pretty much an 18 weeks of revenue difference. The plot essentially provides the survival function across the timeline/tenure.
