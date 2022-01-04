
def run():
    # my_list = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_list.append(i**2)
    # print(my_list)
    
    # squares = [i**2 for i in range(1,101) if i % 3 != 0]
    # print(squares)
    
    squares = [i  for i in range(1, 1000) if i % 4 == 0 and i % 9 ==0 and i % 6 == 0]
    print(squares)
    
    my_list = [i for i in range(1, 1000) if i % 36 == 0]
    print(my_list)
    
    my_list_two = [i**2 for i in range(1,6)]
    print(my_list_two)

if __name__=='__main__':
    run()