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

A few words about Machine Learing without any technical details (for now):
We differentiate between supervised, unsupervised and reenforced learning.. The first one is used for regression problems, e.g. problems where you want to predict a continous variable using a regression function based on all previous points. Besides regression, classification problems are also utterly useful to handle with applications to spam, fraud or image detection. At last, we remain with reinforced learning, the approach of try and error, which is usually used in game developement for enhancing KI opponents.
A separate point to mention is Deep learning, a machine learning technique which imitate the human brain as it is modeled via nodes which represents neurons. It is used to analyze human languages, most noteable known is the GPT-3 model in ChatGPT, images, audios and videos, forecast time series. But it requires a large amount of datasets which might become costly.
A general pipeline for the model deployment process might look like this: First we prepare the data as seen in the previous steps. Then we build the model with whatever machine learning or classical (regression) techniques seems suitable. Thereafter, we train the model given the accessible dataset, usually one splits the dataset into a training and a test set. Lastly, we deploy/export the model and make use of it.
Actually, we have missed the evaluation step in which the model's accuracy is measured by some metric and potentually one has to improve the model such that the accuarcy is suitable maximized.

Data Science methodology

One can describe the general procedure as follows: At first, a problem has to be defined which can be approched via the given requirements and using the data collection. Obviously, it has to checked if the questions is, if ever, answerable. The next step for the data scientist would be to understand the question and its setting in which it is embedded in. This leads naturally in some preparation which needs to be done and goes over to modeling and eventually to evaluation. Finally, there is feedback required from the deployment if the presented model does do its intended job.
Let us precise the aforementions general procedure as follows:  In a very first stage, usually a business meeting is (einberufen) where the question is discussed with the executives. (Dabei) it should give a clear and foremost precise question/goal to set. Anyway, let us move on to the analytic approach where the general structure for the task is set. This might vary between a very simple descriptive analysis or an easy diagnostic statistical analysis to more sophisticated methods like predictive algorithms like machine learning techniques. The latter should even more be specified: If probabilites are reqires then a predictive model is the way to go, If it is necessary to show any sort relationship between variables a more simple descriptive model suffices, and if the task is a seemingly simply yes-or-no-question than a classification model/algorithm is needed. We proceed with the data requirement step in which it is set which data is needed to manage to solve the task. This step go in hand in hand with the next step of data collection, since the latter might be difficult to handle which lends to an adaptation of the data requirements. To answer the subquestion if the found data is sufficent a visualization or a descrptive analysis is useful to manifest if the features are meaningful and uncorrelated. Once this step is completed, we move on to the data understanding step, in which univariate statistices play a key role since they determine if quality of the data like min/max, correlations, mean, median or a histogram to find quality indicators. Naturally, this step is connected to the data preparation step in which it is secured that there is no missing data and that all the data is correctly formated, and that all the data can be accessed in a proper way. Here, it might be useful to make use of domain knowledge and (hinzuberufen) any experts in the given working field. We need to note that this step takes the most amount of time in the whole methodology process. But the actually core step is modelling (80-20-rule). Here, we (umsetzen) the goals as set in the early beginnings of the project which might be either a descriptive or a predictive model. Once the model is properly set up using the training dataset, it is time to evalulate the build model if it does answer the question purposely or if the models require more (parameter) tuning. Thereby, this step is (bezogen) on the last one. A techniqual device to answer this is to make use of the ROC curve, the curve of (ToDo) and/or to setup a confusion matrix, a matrix about the true/false-positive/negative rate in the model. As oneself is satisfied with the model, we can deploy it in the model deployment stage and adapt it for the stakeholders which means for example if the they are familiar/can be familiarized with the new tool. Obviously, this can a iterative step and requires naturally the feedback of them. Lastly, the feedback stages finished the whole procedure in which is is set to answer if the model does successfully answer the given question/goal. If not then there is refinement necessary or if even a total new model which lends to remodelliing.


Python

Since my knowledge about object orientated programming languages is fairly decent I might omit some parts, or just examine them briefly. Most notably, in Python there is no need to explicitly declare the type of a variable. But, it might be usefult to cast a type using the functions
 - int( ), float( ), str( )
A interesting standard operation is the modulo operation which is expressed via //. Working with strings is similar to the other dividing and slicing techniques for  Python lists/arrays. Notably are: + for concatination, str[-1] for the whole string and multiplication. Moreover, we have lists and tupels where the latter is immutable. On both concepts can be applied the same slicing techniques as for strings. Then there are dictionaries which links keys to some value, i.e. dic = {"key1":3,...}. Notable functions are .del(...), .keys(), .values(). In contrary to all the datatypes before sets are unordered and simply noted as set = {a,2,...}. There are similar set operations as usual, like .union(set2), .intersect(set2), .add(elem), .remove(elem) or .issubset().
Conditions are introduced with an if statement and comparisions can be made with common operations and be connected with an and or an or keyword. Worth mentioning is the else if case with is abbreviated with elif. Most commenly used are for loop to iterate over the aforementioned datatypes, p.ex. for x in  ... :, or as a normal iteration one can use for i in range(1,N): while alternatively while-loops are used for conditional-based iterations. As known from other languages functions are used to reuse numerously a code block indicated with the def fct(par): beginning. The most known functions are len(...), sum(...), sorted(...), .sort(), .reverse(), As known from Java, one can treat exeptions using a try:... except:... statement. Since Python is object-orientated one can define classes with the class Name(obj) statement with is further defined using the def __init__(self, var1, ...): statement. Lastly we proceed with the stock handling of files for which an import os statement is needed. Then files can be opened using open(path, mode) where the mode varies between "r", "w" or "a". Note that a file needs to be closed using the .close() statement. Notable functions are .readline(), .write("..."), .tell() for the curser position or .seek(offset, from).
Now, we move on more external libaries and we start with pandas. It is a library to handle tables or generally speaking datasets more easily in Python. For this end, data is loaded from files using the .read_csv(path) command, or similary .xlsx files or SQL databases can also be read which will be np.identity(4)stored as a dataframe, usually called df. We navigate through a dataframe either through its columns, i.e. with df.columns and the indicies, i.e. df.index.values, in the form of df.loc[ind,col], or one can view a dataframe as a n*m-grid and thereby use the grid position as positioning, i.e. df.iloc[x,y]. Also here, slicing operations can be useful. To generate an empty dataframe with given column structure, one can use df = pd.DataFrame() df = pd.concat([df,pd.DataFrame(columns=list)]) and can finally add data via df.loc[index] = data. Moreover, one can add columns with data as follows df['col1'] = data.
In a more scientific setting is the numpy library senseful as they can easiliy handle multidimensional arrays, for example via np.array[] and in a one-dimensional case via np.arange(1, 7) or via np.linspace(1, 10, 7). Useful are as well np.ones((2, 3)) or np.zeros((2, 3)) or np.identity(4). Anyway, it provides also common mathematical functions like sin(), exp() or prod(). At last we cover library which are used for webscraping and start with requests to establish an HTML connection most notable are the .get(url) and the .text() commands. After the data is obtained one needs to navigate thorugh the html file in a good way for which BeautifulSoup is used, i.e using soup = BeautifulSoup(data, 'html.parser'). Then one can look for any kind of HTML object for example for tables using the .find_all('table') command.

SQL
SQL the most common language to manage relational databases. A query has the following structure: 
 - SELECT col1, col2 FROM table WHERE col1 <, <=, >, >=, LIKE value/ BETWEEN ... AND ...
As most of the keywords are clear by definition we simply move on giving a list of examples. Mostly we omit the WHERE clause.
- SELECT COUNT(col1) FROM table 
- SELECT DISTINCT col1 FROM table 
- SELECT * FROM table LIMIT 10 
- CREATE TABLE (col1 datatype, ...)
- ALTER TABLE table 	ADD COLUMN col1 datatype
			ALTER COLUMN col1 SET datatype
			DROP COLUMN col1
- INSERT INTO table VALUES (...)
- UPDATE table SET col1 = '...'
- DELETE FROM table
- DROP TABLE table
- TRUNCATE TABLE table -> clears all data while remains structure
- SELECT * FROM table ORDER BY col1 (DESC)
- SELECT COUNT(col1) FROM table GROUP BY col1
- SELECT * FROM table HAVING count(col1) > value
Notable functions to mention are MIN(), MAX(), AVG(), ROUND(), LENGHT(), UCASE(), LCASE()
Moving on, we touch on dates which may have different formats like YYYY/MM/DD. Useful functions are DAY(), MONTH() or YEAR(), and CURRENT_DATE(). Similary for times and timestamps.
Clearly, one can write nested sequences like ... WHERE (SELECT col3 FROM table3 ...) or SLEECT * FROM (SELECT col4* FROM table2) ....
Lastly, we need to somewhat clearify the API between SQL and Python but this depends heavily on the precise data mangement system one uses, like MySQL, PostgreSQL, etc.


Data analysis



Data visualization

Machine learning


Timeseries analysis

Anomaly detection: https://neptune.ai/blog/anomaly-detection-in-time-series
Pattern recognition: https://www.iese.fraunhofer.de/blog/pattern-recognition/ and
https://stumpy.readthedocs.io/en/latest/Tutorial_The_Matrix_Profile.html
i.e. use stumpy in Python
Overview paper for change point detection: http://www.laurentoudre.fr/publis/TOG-SP-19.pdf


Capstone project