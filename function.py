import io 
from math import log2

def Entropy(text_name,degree) : 

	with io.open(text_name, "r", encoding="utf-8") as f:
		text = f.read()

		# initialisation of text 
		text = text.rstrip()
		text = text.replace("\n"," ")
		text = text.lower()
		length = len(text)
	
		# create a list of all diferentes symboles in this text 
		alphabet_list = list()
		for alphabet in text :
		    if alphabet not in alphabet_list :
		        alphabet_list.append(alphabet)
		    else :
		        continue

		# calculate the cardinal of text ; sum of  symboles in this text 
		cardinal = len(alphabet_list)

		# calculate the sum of new symboles associated to the order 
		sum_symbols = length - degree

		# calculate the sum of new symboles associated to the previous degree 
		sum_symbols0 = length - (degree-1)

		# create a dictionairy of all different new symboles associated to degree = (m-1) as keys and thier probabilities of apparition in the text as values
		dict_proba_m0 = dict()
		for i in range(0,length-(degree-1)) :
		    if text[i:i+1+(degree-1)] in dict_proba_m0 :
		        dict_proba_m0[text[i:i+1+(degree-1)]] += (1/sum_symbols0)
		    else :
		        dict_proba_m0[text[i:i+1+(degree-1)]] = (1/sum_symbols0)
		 
		# create a dictionairy of all different new symboles associated to degree = m as keys and thier probabilities of apparition in the text as values
		dict_proba_m = dict()
		for i in range(0,length-degree) :
		    if text[i:i+1+degree] in dict_proba_m :
		        dict_proba_m[text[i:i+1+degree]] += (1/sum_symbols)
		    else :
		        dict_proba_m[text[i:i+1+degree]] = (1/sum_symbols)

		# calculating the entropy degree m of text 
		H = 0
		for symbole_m in dict_proba_m.keys() :
			for symbole0 in dict_proba_m0.keys() :
				if symbole_m[1:] == symbole0 :
					H += dict_proba_m0[symbole0]*((dict_proba_m0[symbole0]/dict_proba_m[symbole_m])*log2(dict_proba_m0[symbole0]/dict_proba_m[symbole_m]))
				else :
					continue
	return H



