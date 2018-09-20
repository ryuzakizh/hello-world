def merge_the_tools(string, k):
    # your code goes here
    num = int(len(string)/k)
    for i in range(num):
        mylist = []
        substr = string[i*k:i*k+k]
        for j in substr:
            if j not in mylist:
                mylist.append(j)
        print("".join(mylist))
