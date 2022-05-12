# Newyork_TLC_Datapipeline_Azure


#Problem Definition:

The city of New York provides historical data of "The New York City Taxi and Limousine Commission" (TLC). Your colleagues from the data science team want to create various evaluations and predictions based on this data. Depending on their different use cases, they need the output data in a row-oriented and column-oriented format. So they approach to you and ask for your help. Your colleagues only rely on a frequent output of the datasets in these two formats, so you have a free choice of your specific technologies.

#Tasks to be performed:

*Build a data pipeline that imports the TLC datasets for at least the last three years

*Enhance your pipeline in that way that it automatically imports future datasets

*Convert the input datasets to a column-oriented (e.g. Parquet) and a row-oriented format (e.g. Avro)

*Import or define a schema definition

*Structure the data in that way so that the data science team is able to perform their predictions:

	*The input data is spread over several files, including separate files for “Yellow” and “Green” taxis. Does it make sense to merge those input file into one?

	*You will notice that the input data contains “date and time” columns. Your colleagues want to evaluate data also on hour-level and day of week-level. Does that affect your output-structure in some way?

*To determine the correctness of your output datasets, your colleagues want you to write the following queries:

 	*The average distance driven by yellow and green taxis per hour

 	*Day of the week in 2019 and 2020 which has the lowest number of single rider trips

 	*The top 3 of the busiest hours
 	
Proposed Solution:
![](https://github.com/venu1807/Newyork_TLC_Datapiepeline_Azure/blob/main/Newyork_TLC_Dataset_Azure.png)
