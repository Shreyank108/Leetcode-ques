# a="shreyank" 
# for i in range(0,len(a),2): 
#     print(a[i:i+2]) 

# for i in range(int(input())): 
#     a,b= map(int,input().split()) 
#     if a <6 : 
#         print(b)
#     elif (a>6): 
#         p=round(a/6) 
#         print(p*b)


# l=[]
# for i in range (int(input())): 
#     x= int(input())
#     l.append(x) 
# count_even=0 
# count_odd=0
# for i in l: 
#     if i%2==0: 
#         count_even+=1 
#     elif i%2!=0: 
#         count_odd+=1 
# if (count_odd<count_even): 
#     print("READY FOR BATTLE") 
# else : 
#     print("NOT READY")




# 4
# 1 5
# 2 6
# 4 3
# 3 5
# count =0
# for _ in range(int(input())): 
#     a,b=map(int,input().split()) 
#     c=a*b
#     while((c-4)!=0):
#            count+=1 
#            print(count)



# 4
# 5 3
# 1 1
# 4 1
# 2 1
# for _ in range (int(input())): 
#     a,b=map(int,input().split()) 
#     if(((b/a)*100)>50): 
#         print("Yes") 
#     else : 
#         print("NO") 
        
        
# for _ in range(int(input())) :
#     n =input() 
#     m=int(n[::-1]) 
#     p[rint()]  




    





# 4
# 4 3
# 5 3 1 2
# 3 2
# 1 3 4
# 4 2
# 2 1 2 4
# 5 6
# 1 2 3 4 5


# for _ in range(int(input())): 
#     a, b = map(int, input().split()) 
#     p = list(map(int, input().split())) 
#     count = 0
#     for i in p: 
#         if i >= b:
#             count += 1 
#     print(count)


# p={
#     'A' : 'T',
#     'T' : 'A',
#     'C' : 'G',
#     'G' : 'C'
# } 

# l=[]     
# k=input() 
# for i in k: 
#     l.append(i) 
# m=[]
# for i in l: 
#     for key, value in p.items(): 
#         if ( key == i): 
#              m.append(value) 
# print("".join(m))        
             
             
# l=list(map(int,input().split())) 
# print(len(l)) 
# if len(l) %2 != 0 :  
#     print(-1) 
# else : 
#     count =0 
#     for i in l: 
#         count +=i         
#     if count ==0 : 
#         print(0)  
#     else: 
#         print(count//2)

# nums = [1,2,3,4,5,6,7]
# k = 3 

# n=len(nums) 
# k=k%n      
# print(nums[-k:]+nums[:-k])

# Input:
# Output: 5 
# prices = [2,4,1]
# k=[] 
# m= prices.index(min(prices)) 
# for i in range(m,len(prices)): 
#     k.append(prices[i]) 
# print((max(k) - min(k)))

# Input: 
# ransomNote = "aab"
# magazine = "baa"

# ransomNote= ''.join(sorted(ransomNote))
# magazine= ''.join(sorted(magazine))
# # Output: false 
# if ransomNote in magazine : 
#     print("true") 
# else : 
#     print("false") 
# if len(ransomNote)< 2:   
#     if ransomNote in magazine : 
#         print("true") 
#     else : 
#         print("false") 
# else : 
#     p=[]
#     for i in ransomNote: 
#         p.append(i) 
# for i in p: 
#     if i in magazine: 
#         print("True") 
#         break
#     else : 
#         print("False") 


# 'U', 'D', 'L' and 'R'. 

# Input:
# moves = "UD"
# # Output: true 
# p=[]
# for i in moves: 
#     p.append(i) 
# for i in range(len(p)): 
#     if p[i] == p[i+1]: 
#          print(False) 
#     else : 
#         print(True)


# nums = [1,3,5,4,7]
# # Input:
# if not nums:
#     print(0)

# max_length = 1
# curr_length = 1

# for i in range(1, len(nums)):
#     if nums[i] > nums[i - 1]:
#         curr_length += 1
#         max_length = max(max_length, curr_length)
#     else:
#         curr_length = 1
# print(max_length)


# Input:
s = "abca"
# Output: true
# Explanation: You could delete the character 'c'. 
# for i in range(len(s)): 
#       m= s[:i]+s[i+1:] 
#       if m == m[::-1]: 
#           print(True)
  
# left = 0   
# right = len(s)-1   

# while left < right : 
#     if s[left] != s[right] : 
#         print ( checkkrepallin(s,left+1,right) or checkkrepallin(s,left,right-1) ) 
#     left+=1  
#     right -=1   
# print(True) 

# def checkkrepallin(s,left,right): 
#     while left < right : 
#         if s[left] != s[right]  : 
#             print(False) 
#     print(True)





# QUE 682
# Input:
# ops = ["5","2","C","D","+"]
'''Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30. '''
# Hint 
'''An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.''' 


# # Input:
# n = 25
# # Output: 1389537 
# n1=0  
# n2=1  
# count = 0
# for i in range (n): 
#     c= n1+n2 
#     count +=c
#     n1=n2   
#     n2=c    
# print(count) 


# Input:  
# left = 1
# right = 22
# w=[]
# c=0
# for i in range(left,right+1,1):
#     c=0
#     s=str(i)
#     for j in s:
#         j=int(j)
#         if j!=0 and i%j==0:
#             c+=1
#     if c==len(s):
#         w.append(i) 
# print(w)

# Input:
# nums = [1, 2, 3, 4]
# n = []

# # Find the maximum value and its index
# m = max(nums)
# k = nums.index(m)

# # Remove the maximum value from the list
# nums.remove(m)

# # Double each remaining value and store in the list n
# for i in nums:
#     n.append(i * 2)

# # Iterate through the doubled values
# for i in n:
#     # Check if the doubled value is less than or equal to the original maximum value
#     if i <= m:
#         # Print the index of the original maximum value
#         print(k)
#     else:
#         # If the doubled value is greater than the original maximum value, print -1
#         print(-1)





# words = ["gin", "zen", "gig", "msg"]
# morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# binder = dict(zip(alphabet,morse)) 

# for alpha, morse in binder.items(): 
#     print(f"{alpha}:{morse}") 
    
# alternate_list=[] 
# for word in words : 
#     morse_regenrate=""  
#     for letter in word  :
#         if letter.lower() in binder : 
#             morse_regenrate+=binder[letter.lower()]
#     alternate_list.append(morse_regenrate) 
# print(alternate_list) 
# p={}
# for i in alternate_list:  
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1  
# count =0   
# for i in p: 
#     count +=1  
# print(count)
    
    
    
# Input: 
# sentence = "I speak Goat Latin"
# # Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa" 
# '''
#     vowel -> last m ma 
#     consonent -> remove frirst char and put it on last and add ma   
#     increase one by one a in last  
# ''' 
# l=sentence.split(" ") 
# print(l)
# p={}
# for key,value in enumerate(l): 
#    p[key]= value   
# print(p) 
# vowels="aeiouAEIOU"  
# x=""
# for index,i in enumerate(l,start=1): 
#     if i[0] in vowels: 
#          x+=i +"ma" +" "
#     else : 
#         x+=i[1:] + i[0] + "ma" +"a"*index +" " 
# x=x.rstrip()
# print(x) 

     
        
    
# Input:
# image = [[1,1,0],[1,0,1],[0,0,0]]
# # Output: [[1,0,0],[0,1,0],[1,1,1]] 
# flip_mapping = {0: 1, 1: 0}
# flipped_image = []
# for row in image:
#     flipped_row = []
#     reversed_row = list(reversed(row))
#     for pixel in reversed_row:
#         flipped_pixel = flip_mapping[pixel]
#         flipped_row.append(flipped_pixel)
#     flipped_image.append(flipped_row)
# print(flipped_image)


# Input:
# s = "a#c"
# t = "b"

# # Output: true
# # Explanation: Both s and t become "ac". 
# m=""
# k=""
# if "#" in s : 
#     p=s.index("#")  
#     m+=s.replace(s[p-1:p+1],"")
# print(m)
# if "#" not in s: 
#     m+=s
# if "#" in t : 
#     p1=t.index("#")  
#     k+=t.replace(t[p1-1:p1+1],"") 
# if "#" not in t: 
#     k+=t
# print(k) 
# if m==k : 
#     print(True)
# else : 
#     print(False)     
    
    
    
# Input: 
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# # Output: [[1,4,7],[2,5,8],[3,6,9]]   
# # print(list(zip(*matrix))) 
# t_m=[]
# for i in zip(*matrix): 
#      t_m.append(list(i)) 
# print(t_m)


# Input:
# nums = [6,5,4,4]
# p = list(nums)
# if nums == sorted(nums) or nums == sorted(nums, reverse=True):
#     print(True)
# else:
#     print(False)
     
# Input:
# nums = [3,1,2,4]
# # Output: [2,4,3,1]
# # Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted. 
# l=[]
# for i in nums: 
#     if i%2==0: 
#         l.append(i) 
# for i in nums: 
#     if i%2!=0: 
#         l.append(i) 
# print(l)


# Input:
# deck = [1,1,1,2,2,2,3,3]
# # Output: true
# # Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]. 
# p={}
# for i in deck: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1  
# print(p)
# count_of_two =0 
# for i in p.values(): 
#     print(i)
#     if i %2==0 : 
#         count_of_two+=1  
# print(count_of_two) 
# if count_of_two == len(deck)//2 : 
#     print(True) 
# else : 
#     print(False)

# Input:
# nums = [4,2,5,7]
# # Output: [4,5,2,7]
# # Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted. 
# l=[]
# for i in nums: 
#     if i%2==0:  
#         l.append(i) 
# else : 
#         l.append(i) 
# print(l) 

# Input:
# arr = [6,3,2,1]
# max_index = arr.index(max(arr))

# left_part = arr[:max_index]
# right_part = arr[max_index + 1:]

# is_left_sorted = left_part == sorted(left_part)
# is_right_sorted = right_part == sorted(right_part, reverse=True)

# if is_left_sorted and is_right_sorted:
#     print("True")
# else:
#     print("False")


# Input:
# nums = [1,2,3,3]
# # Output: 3 
# p={}
# for i in nums : 
#    if i in p: 
#        p[i]+=1 
#    else : 
#        p[i]=1   
# print(p)  
# max_value = max(p.values())

# for key,values in p.items(): 
#     if values == max_value: 
#         print(key)
    
    
# Input:
# nums = [-7,-3,2,3,11]
# l=[]
# # Output: [0,1,9,16,100] 
# for i in nums : 
#     l.append(i**2) 
# print(sorted(l))
    
# Input:
# num = [1,2,0,0]
# k = 34
# # Output: [1,2,3,4]
# # Explanation: 1200 + 34 = 1234 
# p="" 
# for i in num: 
#     p+=str(i)    
# p=int(p)  
# x= p+k  
# print(x)
# another_list=[]  
# for i in str(x): 
#     another_list.append(int(i)) 
# print(another_list)


# Example 1:

# Input:
# words = ["bella","label","roller"]
# # Output: ["e","l","l"]
# # Example 2:

# # Input:
# # words = ["cool","lock","cook"]
# # Output: ["c","o"] 
# for i in words: 
    
    
# nums = [0,1,1] 
# p={1:False,0:True} 
# p=[nums] 
# print(*p)

# Input:
# heights = [1,1,4,2,1,3]
# # Output: 3
# # Explanation: 
# # heights:  [1,1,4,2,1,3]
# # expected: [1,1,1,2,3,4]
# # Indices 2, 4, and 5 do not match. 
# count =0
# for i in range(len(heights)-1): 
#     for j in range(1,len(heights)): 
#         if (heights[i]>heights[j]): 
#             count+=1  
# print(count)
             
             
# Input:
# str1 = "ABCABC"
# str2 = "ABC"
# # Output: "ABC"
# result ="" 
# p=set() 
# for i in str2: 
#     if i not in p : 
#         result +=i 
#         p.add(i) 
# print(result)



# Example 1:

# Input:
# text = "alice is a good girl she is a good student"
# first = "a"
# second = "good"
# # Output: ["girl","student"]
# # Example 2:
# # Input: text = "we will we will rock you", first = "we", second = "will"
# # Output: ["we","rock"] 
# words = text.split()
# result = []
# for i in range(len(words) - 2):  # We iterate until the third last word
#     print(words[i])
#     if words[i] == first and words[i + 1] == second:
#         result.append(words[i + 2])
# print(result)
        
        
# Input:
# arr = [1,0,2,3,0,4,5,0]
# # Output: [1,0,0,2,3,0,0,4] 

# l=[] 
# for i in arr: 
#     if i ==0: 
#         arr.append(0)


# Input: 
# address = "1.1.1.1"
# # Output: "1[.]1[.]1[.]1" 
# m=address.replace(".","[.]") 
# print(m)


# Input: 
# arr1 = [2,3,1,3,2,4,6,7,9,2,19]
# arr2 = [2,1,4,3,9,6]
# # Output: [2,2,2,1,4,3,3,9,6,7,19]  
# counts={} 
# for i in arr1: 
#     if i in counts: 
#         counts[i]+=1 
#     else : 
#         counts[i]=1 
# result = []
# for num in arr2:
#     result.extend([num] * counts[num])
#     counts.pop(num, None)

# for num, freq in sorted(counts.items()):
#     result.extend([num] * freq)

# print(result)
        

# Example 1:

# Input:
# dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# # Output: 1
# # Example 2:

# # Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# # Output: 3
# m=[]
# for i in dominoes: 
#     m.append(sorted(i))
# print(m)
# s=[] 
# for i in m: 
#    k= m.count(i)  
#    s.append(k) 
# print(max(s))
     
     
# Example 1:

# Input:
date = "2019-02-10"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019. 

# y,m,d = map(int,date.split("-")) 
# print(y)
# print(m)
# print(d) 

# days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31] 

# day_in_year= sum(days_in_month[:m])+d                

# if m>2 and ((y%4==0 and y%100!=0) or  y%400 == 0): 
#     day_in_year+=1  

# print(day_in_year)
   
   
   
# Example 2:

# # Input:
# text = "nlaebolko"
# # Output:2
# # ballon 
# l=[] 
# for i in text: 
#     l.append(i)  
# print(l)
# p={}
# for i in l: 
#     if i in p: 
#         p[i]+=1 
#     else : 
#         p[i] =1   
# print(p)
# count =0
# for key,value in p.items: 
#     if 'b' ==1 and 'a' ==1 and 'l' ==2 and 'o'==1 and 'n' ==1  : 
#         count +=1  
# print(count)


# Input: 
# arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences. 
# p={}
# for i in arr: 
#     if  i in p: 
#         p[i]+=1 
#     else : 
#         p[i]=1 
# print(p) 
# if len(set(p.values())) == len(p.values()):
#     print(True)
# else:
#     print(False)


# # Input: 
# lists = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# # Merge the lists using zip
# merged_lists = []
# for a, b in zip(lists, lists[1:]):
#     merged_list = a.copy()  # Make a copy of the first list
#     merged_list.append(b[1])  # Append the second element of the next list
#     merged_lists.append(merged_list)

# # Print the merged lists
# for merged_list in merged_lists:
#     print(merged_list) 

# Input: 
# moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# # Output: "A"
# # Explanation: A wins, they always play first.
# l=[] 
# for i in range(0,len(moves),2) : 
#     l.append(moves[i]) 
# print(l) 
     
     
# Input: 
n = 234
# Output: 15 
# count =1   
# count1 =0 
# while n!=0: 
#      p=n%10
#      print(p)  
#      count*=p                
#      count1+=p
#      n//=10 
# print(count,count1) 
# print(count-count1) 
# count1=1   
# count=0 
# for i in str(n): 
#     count1*=int(i) 
#     count+=int(i) 
# print(count1-count)


# Input: 
# arr = [1,2,2,6,6,6,6,7,10]
# # Output: 6 
# p={}
# for i in arr: 
#     if i in p: 
#        p[i]+=1  
#     else : 
#         p[i] =1   
# print(p)   
# max_value = max(p.values())
# for key,value in p.items(): 
#     if value == max_value: 
#         print(key)


# Input:
# nums = [12,345,2,6,7896]
# # Output: 2 
# count =0
# l=[]
# for i in nums: 
#     l.append(str(i)) 
# for i in l:  
#     if len(i) % 2==0  : 
#         count +=1   
# print(count)

# Input:
# n = 5
# # Output: [-7,-1,1,3,4]
# # Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4]. 
# l=[]
# if n==1: 
#     print ([0] )
# l=[] 
# if n%2!=0: 
#     l.append(0) 
# for i in range(1,(n//2)+1): 
#     l.extend([i,-i]) 
# print(l)



# Input: 
# num = 38
# n=num
# while n >= 10:
#         # Sum the digits of the number
#         digit_sum = 0
#         while n > 0:
#             digit_sum += n % 10
#             n //= 10
#         n = digit_sum
# print(n)


# Input:
# n = 10000
# # Output: [2,9]
# l=[]
# p=[] 
# for i in range(1,n): 
#     for j in range(i): 
#         if i+j == n: 
#            l.append(i)
#            l.append(j)  
# if 0 in l: 
#     l.pop(0)
    
# p.append(l[0]) 
# p.append(l[1]) 
# print(p)

# Input: 
num = 9669
# Output: 9969 
l=[]
for i  in str(num): 
    l.append(int(i)) 
m=0
print(l)   
for i in l: 
    if i == 6: 
        m=(l.index(i)) 
print(m) 
l[m]=9 
s=""
for i in l :  
    s+=str(i) 
print(s)