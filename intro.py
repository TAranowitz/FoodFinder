import sys

def DataCollection()->set:
    print("Welcome to Food Finder for all your food reccommendation needs!")
    print("Let's collect some data! What type of cuisine do you enjoy?\n")
    cuisine_types = ["Japanese","Chinese","Italian","Indian","Mexican","French","Thai","Spanish","Greek","Korean","Vietnamese","Polish","Filipino"]
    for index, cuisine in enumerate(cuisine_types):
        print(f"{index}: {cuisine}", end = " ")
    print("Type your answers in the example format: 3 7")
    
    input_str = input()
    cuisine_pref = input_str.split(" ")
    cuisine_index = set()
    for num in cuisine_pref:
        if int(num) < len(cuisine_types) and int(num) >= 0:
            cuisine_index.add(int(num))
    
    return cuisine_index

def save_cuisine_index(index_set:list) -> None:
    with open("saved_data.txt", "w") as file:
        for index in index_set:
            file.write(f"{str(index)}\n")

def load_cuisine_index()-> list:
    return_set = set()
    with open("saved_data.txt", "r") as file:
        for line in file:
            return_set.add(int(line))
    return return_set

def give_non_visited(index_set:list)->set:
    cuisine_types = ["Japanese","Chinese","Italian","Indian","Mexican","French","Thai","Spanish","Greek","Korean","Vietnamese","Polish","Filipino"]
    
    non_visited = set()
    for i in range(len(cuisine_types)):
        if i not in index_set:
            non_visited.add(i)
    return non_visited


def main():
    #index_set = DataCollection()
    #save_cuisine_index(index_set)
    my_list = load_cuisine_index()
    print(give_non_visited(my_list))


if __name__ == "__main__":
    main()