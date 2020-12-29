#Repeating letters in decending oder using dictonary
Str_in = str(input())
sorted_out={}
str_Dic = {}
def most_frequent(Str_in):
    for i in Str_in:
        if i in str_Dic:
            str_Dic[i] +=1
        else:
            str_Dic[i] = 1
    sorted_out = dict(sorted(str_Dic.items(), key = lambda item:item[1],reverse = True))
    for i in sorted_out:
        print(i+":"+str(sorted_out[i]))
most_frequent(Str_in)
