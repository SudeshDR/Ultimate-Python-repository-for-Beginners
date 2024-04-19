def number_to_words(num):
    ones=[" ","one ","two ","three ","four ","five ","six ","seven ","eight ","nine "]
    tens=[" "," ","twenty ","thirty ","forty ","fifty ","sixty ","seventy ","eighty ","ninety "]
    teens=["ten ","eleven ","twelve ","thirteen ","fourteen ","fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]


    if num==0:
        return "zero"
    #HANDLING LESS THAN 20 AND MULTIPLE OF 10
    if num<10:
        return ones[num]
    elif num<20:
        return teens[num - 10]
    elif num<100:
        return tens[num // 10]+ " "+ ones[num%10]
    elif num<1000:
        return ones[num// 100]+"hundred "+number_to_words(num%100)
    elif num<1000000:
        return number_to_words(num//1000)+"thousand "+number_to_words(num%1000)
    elif num<1000000000:
        return number_to_words(num//1000000)+"million "+number_to_words(num%1000000)
    else:
        return "Number out of range"
#GET INPUT FROM USER
num=int(input("Enter a number: "))
#CONVERT NUMBER TO WORDS
words=number_to_words(num)
#PRINT THE RESULT
print("Number in words:" ,words)

    
