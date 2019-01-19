def get_even_list(l):
        l_new = []
        for i in l:
                if i % 2 == 0:
                        l_new.append(i)
        return l_new

# a = get_even_list([2, 5, 6, 7, 9, 6, 6])
# print(a) 
even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
