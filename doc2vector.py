import word2vec
import os
import nltk

vectorPath = './vectors.bin'
model = word2vec.load(vectorPath)
inputList = ''

# Single query
def cosDistance(query, n):
	indexes, metrics = model.cosine(query, n)
	return model.generate_response(indexes, metrics).tolist()

# The function do analogy: pos is +, neg is -, n is the number of the return
# analogy([query], [], n) is same as cosDistance(query, n) 
def analogy(q_pos, q_neg, q_n):
	indexes, metrics = model.analogy(q_pos, q_neg, q_n)	
	# return the result, the data type is python list
	return model.generate_response(indexes, metrics).tolist()

def rawInput():
	inputQList = []
	inputQnList = []
	inputQ = raw_input(">>> +: ")
	inputQn = raw_input(">>> -: ")
	inputQList = str(inputQ).split(' ')
	inputQnList = str(inputQn).split(' ')
	if(inputQnList[0] == ''):
		inputQnList = []
	return analogy(inputQList, inputQnList, 100)

def main():
	# for example 
	# print analogy(['clean', 'city', 'wifi'], [], 20)
	# print cosDistance('clean', 30)
	while(True):
		print rawInput()

if __name__ == "__main__":
    main()
