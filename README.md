Summary of the Data Science Cource by IBM

Let us start with Chapter 1 which treats the general question what exactly data science is.

As seen in Week 1, Data science is the field in which any given question is answered using data, and/or give recommendations. This data is usually explored, maniplulated and finally analyzed using certain techniques.

Big Data, 5 V's: Velocity, Volume, Variaty, Veracity, Value.
But when is some dataset called a big data set. usually then it is large enough, has enough velocity and volume and if it can not be handled traditionally.

Roles in Data science
 - Business analyst
 - Database engineer
 - Data analyst
 - Data engineer
 - Data scientist
 - Research engineer
 - Software engineer
 - Statistican
 - Product manager
 - Machine learning specialist

Data mining pipeline
 - Establish goals/Costs or ask the right questions
 - selecting data to ensure quality of the data
 - preprocessing data for the integrity, i.e. is there any data missing!
 - transform and storage data, e.g. format or reduce it
 - data mining using descriptive methods or using machine learning tecniques
 - evaluation in/out-sample forecast.

(Open Source) tools for Data scientist

Since commerercial tools are rather reserved for businesses, we omit them and solely concentrate on open source tools. Before we give any tools, it must be clear for what these tools are being used. Therefore we give a rough procecure what there is to do:
First we start with Data management which becomes useful for larger datasets. These are usually stored in databases, mostly in relational databases somewhat based on SQL. Thereby, one can make use of MySQL or PostgreSQL, or in the NoSQL case one can use mongoDB or coachDB. But, there is also the more unusual way of handling data with lots of files. They can be organized using Hadoop or coph.
Once the data is properly managed, we need to extract, load and transform (ELT) it. This phase is called data Integration. Besides techniques in Python which we usually use, one can make use of Apache Airflow or Kaffe or nifi, or use Spark SQL. It must be said, that this part takes a huge amount of time in the general data science methology! Let us move on to Data visualization. This can be done using Hue, kibana or Apache superset.
Regarding the acutual analysis, this is done in the Model deployment phase where predictionIO or Seldon might be tools to use. Afterwards,the models are monitored or assed  using ModelDB or Prometheus.
At last, one has to make a remark about Code Asset mangement. But this is a simple one since GitHub using git is the most common solution. 

As mentioned above, we will mostly work with the language Python as a part of Jupyter Notebooks. As they are server based, Skill Network Labs will provide us an interactive environment to write them. Besides Python, Jupyter Notebooks are also capable of understanding the more statistical orientated language R and Scala, which has its origin in scientific computing. Anyway, they are interactive meaning that they can be executed in chunks in contrary to the all-or-none approach.
Useful libaries in python can be
 - for scientific computing: NumPy and Pandas
 - for data visualization: matplotlib and seaborn
 - Machine and Deep learning: scikit-learn, keras
 - Deep learning: pytorch, tensorflow
Regarding R one can use Ggplot2.

Good datasets can be found on the following websites:
 - data.uno.org
 - data.gov
 - europeandataportal.eu
 - kaggle.com
 - research.google.com
 - datasetsearch.com

It must be mentionend that not all available data can be used without any more thinking as they are usually licenced. Most commenly the are licenced under the CDLA.
But it remains the question if the found data is of any quality or any accuracy.

A few words about Machine Learing without any technical details:
We differentiate between supervised, unsupervised and reenforced learning.. The first one is used for regression problems, e.g. problems where you want to predict a continous variable using a regression function based on all previous points. Besides regression, classification problems are also utterly useful to handle with applications to spam, fraud or image detection. At last, we remain with reinforced learning, the approach of try and error, 


