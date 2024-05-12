# s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
# l=[]
# p=s.split(" ")
# for i in p: 
#     if i.isnumeric(): 
#         l.append(int(i)) 
# flag =0
# for i in range(len(l)-1): 
#     if l[i] >= l[i+1]:  
#         flag =1     
# if flag ==1 : 
#     return False
# else :    
#     m=[]
#     for i in l: 
#         m.append(i) 
#     m.sort() 
#     if m== l: 
#         return True  


# word = "xyxzxe"
# ch = "z"

# if ch in word : 
    
#     p= word.index(ch)   
#     l=[]
#     for i in range(p+1): 
#         l.append(word[i])  
#     m=[]
#     for i in range(p+1,len(word)): 
#         m.append(word[i]) 
#     k1="".join(m)
#     p=l[::-1]
#     k="".join(p) 

#     done =k+k1 
#     return done  
# else : 
#     return word


# nums = [4,4,4,9,2,4]
# l=[]
# for i in nums: 
#     if i%2==0: 
#         l.append(i)  
# print(l) 

# k=[]
# for i in l: 
#     k=i.count() 
#     m.append(k) 
# print(m)


# nums1 = [1,3]
# nums2 = [2,4] 

# p=nums1+nums2
# p.sort() 

# print(p) 

# if len(p)%2!=0: 
#     mid=p[len(p)//2] 
# else : 
#     mid =(p[len(p)//2-1] +p[len(p)//2])/2
#     print(mid) 

# x = 120
# l=[] 

# for i in str(x): 
#     l.append(i)   
# if '-' not in l: 
#     p=l[::-1]  
#     if '0' not in p:
#         m="" 
#         for i in p: 
#             m+=str(i)    
#         print(int(m))  
#     else : 
#         p.remove('0')
#         m="" 
#         for i in p: 
#             m+=str(i)    
#         print(m) 
        
# else:
      
#     p=l[::-1] 
#     if '0' not in p:
#         m=""
#         for i in range(len(p)-1): 
#             m+=p[i]    
#         print("-"+m)  
#     else : 
#         p.remove('0')
#         m=""
#         for i in range(len(p)-1): 
#             m+=p[i]    
#         print("-"+m)
     
     
# s = "     -42"
# l=[]
# k=[]
# s=s.strip()

# for i in s : 
#     l.append(i)
#     if s[0].isnumeric() !=False: 
#         if i.isnumeric(): 
#             k.append(i)
#     else : 
#        print(0)  
# s="" 
# for i in k: 
#     s+=i 
# if '-' in l: 
#     print(int("-"+s)) 
# else : 
#     print(int(s))    


# s = "aa"
# p = "a*"

# if len(s) == len(p): 
    
#phonenumber  
# from itertools import product

# d = {
#     2: ['a', 'b', 'c'],
#     3: ['d', 'e', 'f'],
#     4: ['g', 'h', 'i'],
#     5: ['j', 'k', 'l'],
#     6: ['m', 'n', 'o'],
#     7: ['p', 'q', 'r'],
#     8: ['s', 't', 'u'],
#     9: ['w', 'x', 'y', 'z'],
# }

# p = 23
# p_str = str(p)

# digits = [int(i) for i in p_str]

# digit_values = [d[digit] for digit in digits]

# combinations = list(product(*digit_values))

# print(combinations)
 
 
# list1 = [1,2,4] 
# list2 = [1,3,4]

# list3 =list1+list2   
# list3.sort() 
# print(list3)          
            
            
# nums = [3,2,2,3]
# val = 3
# l=[]
# for i in nums : 
#     if i!=val : 
#         l.append(i) 
# print(len(l))


# haystack = "leetcode"
# needle = "leeto"  

# if needle in haystack: 
#     print(haystack.index(needle)) 
# else: 
#     print(-1)
    
# dividend = -2147483648
# divisor = -1
# if dividend== (-2147483648) and divisor==(-1) : 
#     print(-2147483647) 
# else : 
#     print(round(dividend/divisor))


# nums = [5,7,7,8,8,10]
# target = 8 
# l=[]
# p=nums.index(target) 
# print(p)
# nums.pop(target) 
# m=nums.index(target) 
# print(m)
        
# nums = [1,3,5,6]
# target = 2

# if target in nums: 
#     print(nums.index(target)) 
# else : 
#     nums.append(target) 
#     nums.sort() 
#     print(nums.index(target))
      
# nums = [7,8,9,11,12]

# s=""
# if 1 not in nums : 
#     print(1) 
# else : 
#     nums.sort() 
#     for i in range(nums[0],len(nums)+1):  
#         if i not in nums : 
#             s+=str(i) 
#     print(int(s))
 
# num1 = "2"
# num2 = "3" 

# print(int(num1)*int(num2))

    
# from itertools import permutations

# nums = [1, 2, 3]

# permutations_list = list(permutations(nums))

# result = [list(permutation) for permutation in permutations_list]

# print(result) 

# from itertools import permutations 

# nums =[1,2,3] 

# per_list=list(permutations(nums)) 
# print(per_list) 
# result = [list(permutations) for permutations in per_list]  

# print(result)

# from itertools import permutations   

# nums = [1,2,3] 

# per_list=set(permutations(nums)) 

# result=[list(permutations) for permutations in per_list] 

# print(result)


# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# l=[]
# transposed_matrix = [list(row) for row in zip(*matrix)] 
# for i in transposed_matrix: 
#     p=i[::-1] 
#     l.append(p)
#     matrix=l
# print(matrix)


# words = ["abc","bcd","aaaa","cbc"]
# x = "a" 
# l=[]
# for i in range(len(words)): 
#     if x in words[i]: 
#        l.append(i) 
# print(l)     

# words = ["one.two.three","four.five","six"]
# separator = "." 

# result = []

# for word in words:
#     split_words = word.split(separator)
#     result.extend(split_words)

# print(result)

# num = "51230100" 
# while (num[-1]=='0'):
#     num = num[:-1] 
# print(num)

# s = "ABFCACDB" 
# while('AB' in s or 'CD' in s): 
#     s = s.replace("AB", "").replace("CD","") 
# print(len(s))

# details = ["7868190130M7522","5303914400F9211","9273338290F4010"] 
# l=[]
# for i in details: 
#     l.append(int(i[-4:-2])) 
# count =0
# for i in l: 
#     if i>60: 
#         count+=1 
# print(count)

# word="aaaaab"
# uni_word= set(word) 
# if len(uni_word)==1 : 
#     print(len(word)*2)  
# elif len(uni_word)==2: 
#     print(((len(word)-2)*2)+1)
# else: 
#     print(0)

# word="aaaaab"
# ans = 0
# i = 0
# while i < len(word):
#     if word[i] == 'a':
#         i += 1
#     else:
#         ans += 1
        
#     if word[i] == 'b':
#         i += 1
#     else:
#         ans += 1
        
#     if word[i] == 'c':
#         i += 1
#     else:
#         ans += 1
        
# print(ans)

# nums = [1,5,-2,-4,0]
# nums.sort()
# print(nums)
# p=list(set(nums)) 
# print(p)
# p.sort()
# if nums != p : 
#     print(True) 
# else : 
#     print(False)

# n = 16
# count =0 
# while n//2==1: 
#     count+=1
#     n//=2  
# print(count)

# n = 6
# l = []
# other_num = [4, 7, 8, 9]

# for i in range(1, n):
#     if n % i == 0:
#         print(i)
#         l.append(i)

# if 2 in l or 3 in l or 5 in l:
#     print("f")
# elif any(num in l for num in other_num):
#     print("True")
# else:
#     print("False")


# nums = [9,6,4,2,3,5,7,0,1] 
# for i in range (len(nums)+1): 
#     if i not in nums: 
#         print(i)

# nums = [0,1,0,3,12] 
# z=[] 
# p=[]
# for i in nums : 
#     if i != 0 : 
#         z.append(i) 
#     else : 
#         p.append(i) 
# m=z+p                        
# print(m)




# num = 123
# ones=['one','two','three','four','five','six','seven','eight','nine']
# tens = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
# # Output: "One Hundred Twenty Three" 
# for i in str(num): 
#     if i /


# pattern = "aaaa"
# s = "dog cat cat dog"

# s = s.split()
# a=len(set(pattern))
# b=len(set(s))
# c=len(set(zip(pattern,s)))
# if a==b and b==c:
#     print(True) 
# print(False)  

# n = 45
# count=0
# if n<=0: 
#     print(False)
# flag =0
# while (n!=1): 
#     if n%3==0: 
#         n//=3  
#         flag =1 
# if flag ==1 :     
#     print(True)
    
# s = ["h","e","l","l","o"] 
# print(s[::-1])

# a=12 
# b=23  
# # a=a+b   # 35        
# # b=a-b    
# # a=a-b   
# a=a^b              
# b=b^a  
# a=a^b          

# print(a,b)

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# nums2=set(nums2)
# p=[]
# for j in nums1:
#   for i in nums2: 
#     if i == j : 
#          p.append(i) 
# print(p)

# num = 14
# if num**0.5 == int(num**0.5): 
#     print(True)  
# else : 
#     print(False)  

# s = "aabb"

# f={} 
# for i in s: 
#     if i in f: 
#         f[i]+=1 
#     else : 
#         f[i]=1  
# print(f)
# p=[] 

# for key,value in f.items(): 
#     if value == 1 : 
#      p.append(key)  
# if len(p)<1: 
#     print(-1) 
# else:
#     print(s.index(p[0]))      
    
# s = "abc"
# t = "ahbgdc"

# p=[]
# m=[]

# for i in s : 
#     p.append(i)
# for i in t : 
#     if i in s : 
#         m.append(i) 
# print(p) 
# print(m)
# if p == m: 
#     print(True) 
# else : 
#     print(False)

# nums = [3,2,1]
# uni_array=[]
# for i in nums : 
#     if i not in uni_array: 
#         uni_array.append(i) 

# if len(uni_array) <=2 : 
#    print(max(uni_array)) 
# elif len(uni_array) >=3: 
#     print(uni_array[2]) 
# elif len(uni_array)<=1: 
#     print(uni_array[0])

# sys.set
# num1 = "11"
# num2 = "123" 
# num1 = int(num1)
# num2 = int(num2) 
# print(num1+num2)



# s = "Hello, my name is John"
# count = 0
# inside_segment = False

# for char in s:
#     if char != ' ' and not inside_segment:
#         count += 1
#         inside_segment = True
#     elif char == ' ' and inside_segment:
#         inside_segment = False

# print(count)


# nums = [1,1]
# l=[]
# for i in range (1,len(nums)+1): 
#     if i not in nums: 
#         l.append(i) 
# print(l)

# g = [1,2]
# s = [1,2,3] 

# for i in s : 
#     for j in s : 
#         p=i+j  
# print(p)

# import textwrap
# s = "abab"
# l=[]
# for i in s : 
#     if i not in l: 
#         l.append(i)
# j="".join(l)
# m=[]
# d= textwrap.wrap(s,len(l)) 
# print(d) 
# for i in d : 
#     if i == j: 
#         m.append(True)
#     else : 
#         m.append(False) 
# if False in m: 
#     print(False ) 
# else : 
#     print (True) 

# from itertools import product   

# a=list(map(int,input().split())) 
# b=list(map(int,input().split())) 

# combo = list(product(a,b)) 

# print(*combo)  

# a="qwertyuiop"
# b="asdfghjkl"
# c="zxcvbnm"  
# a1=[]
# for i in a : 
#     a1.append(i)  
# a1.sort() 
# a11="".join(a1) 
# print(a11)
# b1=[]
# for i in b : 
#     b1.append(i) 
# b1.sort()
# b11="".join(b1)  
# print(b11)
# c1=[]
# for i in c : 
#     c1.append(i) 
# c1.sort()
# c11="".join(c1)   
# print(c11)

# nums = [1, 1, 0, 1, 1, 1]
# p = "".join(map(str, nums))
# l = ""

# for i in p:
#     l += str(i)

# result_list = l.split('0')
# m=[] 
# for i in result_list : 
#     m.append(len(i)) 
# print(max(m))


# num = 99999992
# count =0
# for i in range(1,num) : 
#    if num%i==0:  
#        count += i             
# if count == num : 
#     print (True) 
# else : 
#     print(False)

# a=0  
# b=1 
# print(a,b)
# for i in range(1,10): 
#     c=a+b  
#     print(c)           
#     a=b
#     b=c
    
# word = "Usa" 
# if word.isupper(): 
#     print(True) 
# elif word.islower(): 
#     print(True) 
# elif word.capitalize() == word : 
#     print(True) 
# else : 
#     print(False)

# s = "Let's take LeetCode contest" 
# l=[]
# p=s.split() 
# s=[]
# for i in p: 
#     s.append(i.split()) 
# print(s)
# for i in s : 
#     l.extend(i) 
# print(l) 
# k=[]
# for i in l: 
#     k.append(i[::-1]+" ") 
# print(k) 
# t="".join(k) 

# list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
# list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# list1_set = set(list1)
# list2_set = set(list2)

# common_elements = list(list1_set.intersection(list2_set))

# print(common_elements)


# s = "abcdefg"
# k = 2
# # Output: "bacdfeg"
# l=[i for i in s] 
# p=l[k-1]
# l.remove(l[k-1]) 
# c="" 
# c+=p + "".join(l) 

# print(c)

# flowerbed = [1,0,0,0,1] 
# n = 2
# l=[]
# for i in range(len(flowerbed)): 
#     if flowerbed[i]  == 1: 
#         l.append(i) 
# print(l) 
# if (n-1) in l: 
#     print(True) 
# else : 
#     print(False)


# nums = [1,2,3,4] 
# multi =1  
# nums.sort(reverse=True)  
# for i in nums[:3]: 
#     multi*=i          
# print(multi)
        
# sentence = "I speak Goat Latin" 
# p=sentence.split() 
# print(p) 
# for i in p: 
#     if 'a' in i  or 'e' in i or 'i' in i or 'o' in i  or 'u' in i  : 
        
# grid = [[1,3],[2,2]]
# # Output: [2,4] 

# p=[] 
# for i in range(len(grid)): 
#     p.append(*grid[i]) 
# print(p)

# a="kawdjfkj11wdf" 

# if "111" in a : 
#     print("accepted") 
# else : 
#     print('not')


# s="-123"  
# if not s.isdigit(): 
#     print(-1) 
# else : 
#     print(s) 

# s = "Hello, my name is John" 
# p=s.split() 
# print(len(p))



# Type 1 
# s = ""
# t = "y"

# s1=set(s)
# t1=set(t) 
# if len(s1)>len(t1): 
#     p=s1.difference(t1)  
#     print(str*(p)) 
# else : 
#     p=t1.difference(s1)
#     print(str*(p))

# Type 2   

# s = "abcd" 
# t = "abcde" 

# l1=list(s)
# l2=list(t)
# for i in l2:
#     if i in l1:
#         l1.remove(i)
#     else:
#         return i 

# grid = [[1,3],[2,2]]
# Output: [2,4]  


# Input: 
# l1 = [2,4,3]
# l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807. 
# p=""
# q=""
# for i in l1[::-1]: 
#      p+=str(i)    
# for i in l2[::-1]: 
#      q+=str(i)    

# k =str(int(p)+int(q) )

# l=[]
# for i in k[::-1]: 
#     l.append(int(i)) 
# print(l)


# Input:
# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
# # Output: true 
# l=[]
# for i in  word: 
#    l.append(i) 
# print(l)
# for i in board: 
#     print(i)

#     for i in l: 
#         if i in  board: 
#             print(True) 
         

nums = [3,0,1] 

p =len(nums) 

for i in range (p): 
    if i not in nums: 
        print(i)



