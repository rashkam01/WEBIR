# WEBIR
Project for Web IR


3.3 Topic Evolution 


3.3.1 Introduction to Topic Evolution 


In this part we study the topic evolution of NIPS dataset to find out the top topics of the NIPS papers and how it evolves during the course from year 1987 to 2016. We find out the evolution using Dynamic Topic Modelling, it involves dividing our papers into specific time frames. Let us consider 5 years i.e. 1987 -1991 as one-time frame which gives us 6-time slices. Suppose we have the following keywords for the 1st time slice “Learning, speech, neural, model, time, …” which are the words in a topic that fit the first-time slice, so we can consider the key theme of the topic to be “Neural Networks”. Depending on our documents in 2nd time slice the topic and words might change and hence we find the evolution. 


We have referred to the Dynamic Topic Models paper by David M. Blei and John D. Lafferty to understand analysis of time evolution of topics in large document collection. We used genism, an open source topic modelling toolkit for implementing the Dynamic topic modelling in python. 


We can identify the semantic structure of documents by examining the words contained in the documents using genism. Let us consider the requirements to run our DTM model and discuss each in detail. 


3.3.2 Preparation for our DTM model: 
List of Documents: Our NIPS dataset a total of 6561 documents which are nothing but a collection of words. We fist started by splitting each word based on the year the document it is contained in was published.

Cleansing the Document: In this section, we tokenize the documents by removing the common words and the stop words by using existing python package. Such that we have left with a bag of words which are unique. 

Dictionary Creation: This is a process of assigning unique tokens to each of the words contained in our set of documents. 

Vector Interpretation: In order to mathematically manipulate our we represent each document as a vector, each document in our case will be represented as n-dimensional vector. The vector in generating tf-idf model to return a list of tuples which looks something like (26, 0.646778345) which provides us with probability of occurrence of the word in the document. 


Corpus: A collection of digital document which is the input to gensim. 
	
dtm_path: This is basically a path to our DTM executable. In the form of dtm-win64.exe
	

time_seq: It is the slices in which we want to consider our documents. Suppose we have 30 documents in our NIPS dataset and we provide the time_seq as 5,5,5,5,5,5. Then the first 5 documents of our file will be considered in first time slice, the second 5 in the 3rd time slice and so on. 

Therefore, we have counted the documents in each of the year, e.g. If we consider first 5 years to be one-time frame then we count the number of documents from 1987 to 1991 and put them in 1st time_seq. It is very important to note that our time-seq length should match with the length of our corpus in order for our DTM model to work. 
Once we have prepared the all the required inputs for the DTM model we can simply go ahead and use the method “DtmModel” gensim provides us to find our topic evolution. Depending on the number of topics you need for each time_seq the same can be provided to get the appropriate result. 


The show_topic method of our gensim “DtmModel” gives us output in the form of 2tuples (word probability, word). The higher the word probability of a word the more number of times it has occurred in the time slice. We can also select the number of topics and words per each topic that need to be output per time slice. 


3.3.3 Analysis of Output
For the ease of our analysis let us consider the following example where we consider a time slide of 5 years. We find the same topics evolved smoothly during a time period and yet the content remains the same. In the below flow we see how the words in a topic change over time. Considering the word learning and plotting a graph using python we can visualize the following 〖figure〗^1.

We can see the following trend for the word learning in an increasing curve probably because of the increasing usage of it for the terms “machine learning”, “deep learning” etc. which has seen a growing trend in our NIPS dataset. 


3.3.4 Plotting of graph 
The output of the DtmModel is saved externally in a csv file, where file contains time slice wise probability and words for the top topics. The same csv file is read from in python using “Matplotlib” a library in python used for plotting 2D graphs. 

References: 
	Dynamic Topic Models - David M. Blei & John D. Lafferty-  ICML '06 Proceedings of the 23rd international conference on Machine learning
	Gensim – Python library 
