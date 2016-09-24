## Experiment Overview: Free Trial Screener
In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. [This screenshot](https://www.google.com/url?q=https://drive.google.com/a/knowlabs.com/file/d/0ByAfiG8HpNUMakVrS0s4cGN2TjQ/view?usp%3Dsharing&sa=D&ust=1474680194082000&usg=AFQjCNGUT27DDlXrCKq-ZnsYukNrNIzMdQ) shows what the experiment looks like.



## Experiment Design
### Metric Choice
> #### List which metrics you will use as invariant metrics and evaluation metrics here.

* **Invariant metrics**: Number of cookies, Number of clicks, Click-through-probability
* **Evaluation metrics**: Gross conversion, Retention, Net conversion

> #### For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.

* **Number of cookies**: or, *Number of unique cookies to view the course overview page*. An ideal invariant metric as the cookie loads before the user sees the experiment page.
* **Number of user-ids**: or, *Number of users who enroll in the free trial*. Not a good invariant metric because the number of users who enroll in the free trial is dependent on the experiment. Also, not an good evaluation metric because the number of visitors may be different between the experiment and control groups.
* **Number of clicks**: or, *Number of unique cookies to click the "Start free trial" button*. An ideal invariant metric because the clicks happen before the user sees the experiment, and are thus independent of the groups.
* **Click-through-probability**: or, *Number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button*. Also a good invariant metric because the clicks happen before the user sees the experiment, and are thus independent of the groups.
* **Gross conversion**: or, *Number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button*. It is not a good invariant metric because if users have less than 5 hour time in a week, they are suggested not to enroll, so the number of user-ids will probably be decreased. A good evaluation metric since it's directly dependent on the effect of the experiment and also it shows the probability to succeed.
* **Retention**: or, *Number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout*. It is not a good invariant metric because if users have less than 5 hour time in a week are suggested not to enroll, this would decrease the  number of people who enroll and are less likely to pay, so retention would increase in experiment group. A good evaluation metric since it's directly dependent on the effect of the experiment and also it shows the probability to succeed.
* **Net conversion**: or, *Number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button*. It is not a good invariant metric because if users have less than 5 hour time in a week are suggested not to enroll, this would decrease the number of people who enroll and thus may decrease the number of people pay. A good evaluation metric since it's directly dependent on the effect of the experiment and also it shows the probability to succeed.


To launch the experiment, I will look at the Gross conversion that will decrease practically significant, which shows whether the cost will be lower by introducing the new screener, and Net conversion that will not decrease statistically significant, which shows how the screener affects our revenues.


### Measuring Standard Deviation
#### BaseLine Table
|                   | Value  | 
| ----------------------------- |:--------:| 
| Unique cookies to view page per day       | 40000   | 
| Unique cookies to click "Start free trial" per day            | 3200   |  
| Enrollments per day                        | 660   |
| Click-through-probability on "Start free trial"							  | 0.08   |
| Probability of enrolling, given click					  | 0.20625   |
| Probability of payment, given enroll				  | 0.53   |
| Probability of payment, given click           | 0.1093125    |


> #### List the standard deviation of each of your evaluation metrics.

```
Gross conversion: 0.0202
Net conversion: 0.0156
```

> #### For each of your evaluation metrics, indicate whether you think the analytic estimate would be comparable to the the empirical variability, or whether you expect them to be different.

Gross conversion and net conversion both using the number of cookies in their denominator, which is also our unit of diversion. So, the unit of diversion is equal to the unit of analysis which indicates the analytical variability would be comparable to the empirical variability. Therefore, we can proceed using an analytical estimate of the variance.

### Sizing
#### Number of Samples vs. Power

> #### Indicate whether you will use the Bonferroni correction during your analysis phase.

I would not use Bonferroni correction as I want both gross conversion significantly decrease and net conversion does not significantly decrease requirement fulfilled.

> #### Give the number of pageviews you will need to power you experiment appropriately.

* **alpha** = 0.05
* **beta** = 0.20
* **Gross conversion** (base conversion rate = 20.625%, dmin = 1%)
* **Net conversion** (base conversion rate = 10.93125%, dmin = 0.75%)

Using [this calculator](http://www.evanmiller.org/ab-testing/sample-size.html), I get samples

* **Gross conversion**:  25835 clicks for each group
* **Net conversion**: 27413 clicks for each group

So, I get the pageviews 

* **Gross conversion**:  322937.5 pageviews for each group
* **Net conversion**: = 342662.5 pageviews for each group

I will need 685325 pageviews to power the experiment with these metrics i.e., double the pageviews for both experiment and control groups. 

#### Duration vs. Exposure

> #### Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment.


With the daily traffic of 40000, I would direct 75% of my traffic (30000) to the experiment, so it would take approximately 23 days (685325/30000 = 23) for the experiment, which is a reasonable time for our needs.

## Experiment Analysis

### Sanity Checks

> #### For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check.


| Metrics                    | Lower bound  | Upper bound | Observed | Sanity check |
| ----------------------------- |:--------:| :-----------: | :-------: | :----------: |
| Number of cookies       		  | 0.4988   | 0.5012   | 0.5006 | Yes |
| Number of clicks             | 0.4959   | 0.5041   | 0.5005 | Yes |  
| Click-through-probability     | 0.0812   | 0.0830   | 0.0822 | Yes |
### Result Analysis

#### Effect Size Tests

> #### For each of your evaluation metrics, give a 95% confidence interval around the difference between the experiment and control groups. Indicate whether each metric is statistically and practically significant.

| Metrics                    | Lower bound  | Upper bound | Statistically significant | Practically significant|
| ----------------------------- |:--------:| :-----------: | :-------: | :----------: |
| Gross conversion       		  | -0.0291   | -0.0120   | Yes | Yes |
| Net conversion            | -0.0116   | 0.0019   | No | No |  

#### Sign Tests

> #### For each of your evaluation metrics, do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant

| Metrics                    | p-value | Statistically significant |
| ----------------------------- |:--------:| :-----------: | :-------: | :----------: |
| Gross conversion       		  |  0.0026   | Yes |
| Net conversion            |  0.6776   | No  | 

#### Summary

> #### State whether you used the Bonferroni correction, and explain why or why not. If there are any discrepancies between the effect size hypothesis tests and the sign tests, describe the discrepancy and why you think it arose.

I did not use Bonferroni correction because I want both gross conversion significantly decrease and net conversion does not significantly decreases requirement fulfilled. For both effect size hypothesis tests and the sign tests, gross conversion in experiment group is significantly less than gross conversion in the control group, net conversion in both groups has not significantly differed.

### Recommendation

Gross conversion turned out to be negative and practically significant, which means new change would significantly reduce enrollment that does not pay. Net conversion unfortunately ended up being statistically and practically insignificant and the confidence interval includes negative numbers so, I'm not sure that this experiment would not decrease net conversion. Therefore, there is a risk that the introduction of the trial screener may lead to a decrease in revenue.<br/>
Thus, I don't launch this experiment.

## Follow-Up Experiment

> #### Give a high-level description of the follow up experiment you would run, what your hypothesis would be, what metrics you would want to measure, what your unit of diversion would be, and your reasoning for these choices.


As a student, I know to complete any online program/courses we need a great motivation and will power to do something. But, before enrolling in any online program which takes a long time to complete like Nanodegree, some students need exposure about what's going on in the program, its material, about projects, study advisor, mentor. Thus, I suggest Udacity to launch a new initiative to help those students in need which is to include a mini-course required students to complete the project within that 14 days trial which would be doable if the students spent minimum 5-6 hours/week. Through this mini-course, the students know the knowledge and commitment required for Nanodegree  and also motivate the students to learn and able to complete the tasks.

**Null hypothesis** by creating such mini-course, it will not increase Retention by a practically significant amount.

The mini-course will be randomly assigned to a Control & Experiment Group. The whole courses for Control Group would not change and remained the same while courses for Experiment Group will have this one mini-course (which required them to finish within 14 days).

The **unit of diversion** will be the user-id, as this change only impacts what happens after a free trial account is created.

**Invariant metric** is number of cookies since unit of diversion is cookie, and because users are not exposed to this new course after hitting "Free Trials" screener button.


**Evaluation metric** is Net Conversion, whether rendering a "new mini-course" helps increase the ratio of users who make payment over those who decided only to try the program.

If the Net conversion is positive and practically significant at the end of the experiment, we can roll out this new course to the Data Analyst nanodegree program.


