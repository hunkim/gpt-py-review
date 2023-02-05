# Review your code with chatgpt

## Install
pip install git+https://github.com/hunkim/gpt-py-review.git

## Review
Set enviroment variables: `OPENAI_API_KEY` and `GPT_ENGINE`.
If necessary, also set `REVIEW_PROMPT` and/or `TESTCASE_PROMPT`.


Then run `gpt-py-review yourcode.py`

It will create review comment in md and test cases in test.py.

## Example
### Original Code
```python
# Factorial of a number using recursion

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))

```

### Reviews
**[DOC] It would be better to include the name and the purpose of the function in the comment.**
**Calculates the factorial of a given number using recursion**

**[BUG] Test cases need to be included to make sure the function is working as expected.**

**[REFACTOR] It appears that the function is checking if n is equal to 1. However, it would be better to include a condition to check if n is less than or equal to 1 in order to handle the case where the input is 0 or less which would result in an error in the current implementation. **
```python
def recur_factorial(n):
   if n <= 1:
      return 1
   else:
      return n*recur_factorial(n-1) 
```     
**[Doc] Add test cases to verify the fixed implementation**
```python
def test_recur_factorial():
   assert recur_factorial(0) == 1 # [TEST] 0! is 1 
   assert recur_factorial(1) == 1 # [TEST] 1! is 1
   assert recur_factorial(2) == 2 # [TEST] 2! is 2
   assert recur_factorial(3) == 6 # [TEST] 3! is 6
   assert recur_factorial(5) == 120 # [TEST] 5! is 120

test_recur_factorial()
```

### Generated Test cases
```python
#Test case :1 the given number is  equals to 1 and output must be 1
def test_recur_factorial_1():
    assert recur_factorial(1) == 1

#Test case :2 the given number is  6 and output must be 720
def test_recur_factorial_2():
    assert recur_factorial(6) == 720

#Test case :3 the given number is  5 and output must be 120
def test_recur_factorial_3():
    assert recur_factorial(5) == 120

#Test case :4 the given number is  negative integer
def test_recur_factorial_4():
    assert recur_factorial(-5) == "It shoud not have negative interger"
    
#Test case :5 the given number is  0 
def test_recur_factorial_5():
    assert recur_factorial(0) == 1
```
## Content Right
The code and generated comments, test cases will be used by openai. Please do not use in commercial code. 

From:  https://openai.com/terms/
(a) Your Content. You may provide input to the Services (“Input”), and receive output generated and returned by the Services based on the Input (“Output”). Input and Output are collectively “Content.” As between the parties and to the extent permitted by applicable law, you own all Input, and subject to your compliance with these Terms, OpenAI hereby assigns to you all its right, title and interest in and to Output. OpenAI may use Content as necessary to provide and maintain the Services, comply with applicable law, and enforce our policies. You are responsible for Content, including for ensuring that it does not violate any applicable law or these Terms.
