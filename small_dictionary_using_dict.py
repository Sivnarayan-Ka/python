#lets create a dictionary with few values and which returns its values 
# after taking input from user assuming the user only inputs words which is there in your dict

dict = {"demand":"the need for something","cost":"the price of some commodity for buying or getting",
        "teaching":"to make someone learn something","student" : "the person who learns"}

word = input("enter a number to look up in dictionary")
if word.lower().strip() in dict.keys():
    print(f"the meaning of {word} is {dict[word.strip()]}")
else:
    print("the word is not found in dictionary")