T = int(input())

for _ in range(T):
    stack_A = []
    A = input()
    new_A = ""
    for a in A:
        if a != ')':
           stack_A.append(a) 
           continue
           
        if len(stack_A) == 0:
            new_A += a
            continue

        if 3 > len(stack_A):
            while stack_A:
                new_A += stack_A.pop(0)
            new_A += a
            continue
            

        previous_1 = stack_A[len(stack_A) - 1]
        previous_2 = stack_A[len(stack_A) - 2]
        previous_3 = stack_A[len(stack_A) - 3]

        if previous_1 == 'x' and previous_2 == 'x' and previous_3 == '(':
            stack_A.pop()
            stack_A.pop()
            stack_A.pop()
            stack_A.append('x')
            stack_A.append('x')
        else:
            while stack_A:
                new_A += stack_A.pop(0)
            new_A += a
    
    while stack_A:
        new_A += stack_A.pop(0)
        
    
    stack_B = []
    B = input()
    new_B = ""
    for b in B:
        if b != ')':
           stack_B.append(b) 
           continue
           
        if len(stack_B) == 0:
            new_B += b
            continue

        if 3 > len(stack_B):
            while stack_B:
                new_B += stack_B.pop(0)
            new_B += b
            continue
            

        previous_1 = stack_B[len(stack_B) - 1]
        previous_2 = stack_B[len(stack_B) - 2]
        previous_3 = stack_B[len(stack_B) - 3]

        if previous_1 == 'x' and previous_2 == 'x' and previous_3 == '(':
            stack_B.pop()
            stack_B.pop()
            stack_B.pop()
            stack_B.append('x')
            stack_B.append('x')
        else:
            while stack_B:
                new_B += stack_B.pop(0)
            new_B += b
    
    while stack_B:
        new_B += stack_B.pop(0)

    if new_A == new_B:
        print('Yes')
    else:
        print('No')
            
            
        

    