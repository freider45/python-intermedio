
def run():
    # my_dict1 = {}
    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict1[i] = i**3
    # print(my_dict1)
    
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)
    print()
    dictionary_row = {i:round((i**(1/2)),2) for i in range(1,101) if i % 3 !=0}
    print(dictionary_row)

if __name__=='__main__':
    run()