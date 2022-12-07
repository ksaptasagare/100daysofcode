#calculating the mean, median, mode

#calculating the mean - average value of all the values in a dataset
#calculating the median - middle value among all the values in sorted order
#calculating the mode - frequently occurring value among all the values

#defining a class for statistic calculation
#assuming that the data passed is going to be a list

class stat:
    def __init__(self, l1):
        self.list1 = l1

    #method to calculate the mean
    def mean(self):
        mean = sum(self.list1)/len(self.list1)
        return mean

    #method to calculate the median
    def median(self):
        lst1 = self.list1
        lst1.sort()
        if len(lst1) % 2 == 0:
            m1 = lst1[len(lst1)//2]
            m2 = lst1[len(lst1)//2 - 1]
            median = (m1 + m2)/2
        else:
            median = lst1[len(lst1)//2]
        return median

    #method to calculate the mode
    def mode(self):
        freq = {}
        for ele in self.list1:
            freq.setdefault(ele,0)
            freq[ele]+=1
        
        frequent = max(freq.values())
        for k,v in freq.items():
            if v == frequent:
               mode = k
        return mode

#defining a list
list1 = [32,15,54,54,21,9,35,20,12,20]

#creating an object of class
exmp = stat(list1)

#calling all the various methods
print("Mean: ", exmp.mean())
print("Median: ", exmp.median())
print("Mode: ", exmp.mode())
