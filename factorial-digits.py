import sys

user_input = int(sys.argv[1]) 

def main():

    result = [None] * 100000
    
    result[0] = 1
    result_size = 1
    answer = 0
    
    x = 2
    while x <= user_input:
        result_size = multiply(x, result, result_size)
        
        x = x + 1
     
    i = result_size-1
    while i >= 0 :
        answer = answer + result[i]
        i = i - 1
    #print("Answer is ")
    sys.stdout.write(str(answer))
        
def multiply(x, result,result_size) :
     
    carry = 0 

    i = 0
    while i < result_size :
        prod = result[i] * x + carry
        result[i] = prod % 10;
        
        carry = prod // 10; 
        i = i + 1
 
    while (carry) :
        result[result_size] = carry % 10
       
        carry = carry // 10
        result_size = result_size + 1
         
    return result_size

main()

