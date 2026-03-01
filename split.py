def split(total, people):
    try:
        if total/people<people:
            raise ValueError("Number of people must be greater")
    except ValueError as e:
        print(e)
        return
    
    rem=total%people
    final_list=[total//people+(people-i)-(i-1) for i in range(1,people+1)]

    for i in range(rem):
        final_list[-(i+1)]+=1

    
    print(final_list)
    #print(sum(final_list))

total=int(input("Enter the total amount: "))
people=int(input("Enter the number of people: "))
        
split(total, people)
