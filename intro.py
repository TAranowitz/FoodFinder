import sys

def DataCollection():
    print("Welcome to Food Finder for all your food reccommendation needs!")
    print("Let's collect some data! What type of cuisine do you enjoy?\n")
    cuisine_types = ["Japanese","Chinese","Italian","Indian","Mexican","French","Thai","Spanish","Greek","Korean","Vietnamese","Polish","Filipino"]
    for index, cuisine in enumerate(cuisine_types):
        print(f"{index}: {cuisine}", end = " ")
    print("Type your answers in the example format: 3 7")
    
    input_str = input()
    cuisine_pref = input_str.split(" ")
    cuisine_index = []
    for num in cuisine_pref:
        if int(num) < len(cuisine_types) and int(num) >= 0:
            cuisine_index.append(int(num))
    
    return cuisine_index


def main():
    DataCollection()


if __name__ == "__main__":
    main()