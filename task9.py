#duplicate_letter.py

def check_duplicate_letters(sentence):
      # words split into two

    try:
        words = sentence.split()
        for word in words:
            if len(word) != len(set(word)):
                return True
        
        return False

    except Exception as e:
        #input is not string
        print(f"Invalid input the input is must be string :{e} ")
        return False
    
sentence1 = 'hi i am rahul'
result1 = check_duplicate_letters(sentence1)
print(result1)  # f

sentence2 = "hello i am python"
result2 = check_duplicate_letters(sentence2)
print(result2)  # T

sentence3 = 12345
result3 = check_duplicate_letters(sentence3)
print(result3)
