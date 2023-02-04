# How to use the code:
First store the folder you downloaded in a handy place, choose 2 images and places them in 1.jpg and 2.jpg, then go ahead and run the image_entropy.py file, and wait for results, as it may take a while. (use degree=0 for shortest amount of time)

# what is Entropy:
In information theory, the entropy of a text is the average level of "information", "surprise", or "uncertainty" inherent to each sequence of letters in the text. The entropy is calculated based on the probabilities of different sequences of symbols (of length m) appearing in the text. (Even spaces and special symbols like "'" and "." and so on, count in the entropy calculus ). An image can be represented as text by converting it to binary. 

# image_entropy.py:
This file serves the purpose of converting the two images to text files, calculating their entropies, and comparing them. 
We start by importing the image library for image processing, and the Entropy function that we defined in function.py. 
We define a new function called Entropy_image that takes as arguments the image file name and the degree of entropy. This function is going to be responsable for opening the image, converting it to gray scale (to reduce the representation of each pixel to a single value), converting it to binary, saving its binary representation in a text file called image_bin08.txt, and finally calculating the entropy of the resulting text file using the Entropy function that we defined in function.py. 
So we will do the same process twice, and compare the two entropies. So the code could tell if a minor edit to the image has occured or not, and give you a percentage of the similarity between the two images. 

# function.py:
function.py file contains all the calculations of the entropy of a given text, for a specific degree 'm' that the user choses.
We start by importing the io library for reading and writing data, and math library for use of log2 function. the Entropy function takes 2 
arguments: the name of the text and the degree of entropy. we read the text file using utf-8 encoding (due to its compatibility with ascii characters), we convert to lower case and remove any new line characters (so that they do not count as symbols), and define some variables that we are going to use later:
-length: length of the text file
alphabet_list: contains all symbols from the text
-cardinal: number of symbols of the alphabet_list / could be eventually used to verify if the entropy is correct (  0 &lt; H(s) &lt; log(cardinal) ; H(s) being the entropy )
-sum_symbols: length - degree
-sum_symbols0: length - (degree-1)
-dict_proba_m: dictionary of the symbols of length "m" as keys, and their probabilities as values (proba = frequency of apparition devided by sum of symbols), we proceed by slicing the text, each time a sequence of symbols is found we add to its value: 1/sum_symbols
-dict_proba_m0: dictionary of the symbols of length "m-1" as keys, and their probabilities as values, to fill the dictionary we proceed exactly like before.
-H: Entropy of the text of the degree 'm'