list=[12,3,4,5,12,5,61,33]
#Is the given list divisible by 3 or not
div=[x for x in list if x%3==0]
n_div=[x for x in list if x%3!=0]
print("Divisible by 3:",div)
print("Not divisible by 3:",n_div)

#Square of even numbers in a list
sq=[x**2 for x in list if x%2==0]
print("Square of even numbers in a list:",sq)

#Sum of digits of all the even number
all_even=[x for x in list if x%2==0]
sum=0
for i in all_even:
    sum=sum+i
print("Sum of all even numbers are:",sum)

#Remove duplicates in a list
dict={}
for x in list:
    if x in dict:
        dict[x]=dict[x]+1
    else:
        dict[x]=1
new_list=[x for x in dict if dict[x]==1]
print("Old list which has duplicates:",list)
print("New list which does not have duplicates",new_list)



#Create a dictionary to store the details of your company employees (name as key and
#birthdate as value).
#{ ‘Virat Kohli’: ‘5 November 1988’, ‘Umesh Yadav’: ‘25 October 1987’, ‘Manish Pandey’:
#‘10 September 1989’, ‘Rohit Sharma’: ‘30 April 1987’, ‘Ravindra Jadeja’: ‘6 December
#1988’, ‘Hardik Pandya’: ‘11 October 1993’ }
#Write a function birthDate() that takes the full name of your employees(as a string) and
#displays the given employee’s birthdate.
#>>>birthDate(‘Rohit Sharma’)
#‘30 April 1987’

def birth_date(n):
    dict={ 'Virat Kohli': '5 November 1988', 'Umesh Yadav': '25 October 1987', 'Manish Pandey':
          '10 September 1989', 'Rohit Sharma': '30 April 1987', 'Ravindra Jadeja': '6 December 1980', 'Hardik Pandya': '11 October 1993' }
    flag=0
    for x in dict:
        if n in dict:
            print("Date of Birth of"+n,"is:",dict[n])
            flag=1
            break
    if(flag==0):
        print('Not present in the dictionary')
birth_date('Virat Kohli')