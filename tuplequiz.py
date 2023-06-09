# -*- coding: utf-8 -*-
"""TupleQuiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sGTI363WqGRPWKlp5YbpZ930f-mNnQyF
"""

#   Created by Elshad Karimov on 23/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Tuple Interview Questions

# Q-1. What will be the output of the following code block?
# Answer: D. Exception

init_tuple = ()
print (init_tuple._len_())

# Q-2. What will be the output of the following code block?
# Answer: D. True
init_tuple_a = 'a', 'b'
init_tuple_b = ('a', 'b')

print (init_tuple_a == init_tuple_b)

# Q-3. What will be the output of the following code block?
# Answer: B.  (‘1’, ‘2’, ‘3’, ‘4’)

init_tuple_a = '1', '2'
init_tuple_b = ('3', '4')

print (init_tuple_a + init_tuple_b)

# Q-4. What will be the output of the following code block?
# Answer:  C. 10

init_tuple_a = 1, 2
init_tuple_b = (3, 4)

[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

# Q-5. What will be the output of the following code block?
# Answer: B. 6

init_tuple = [(0, 1), (1, 2), (2, 3)]
result = sum(n for _, n in init_tuple)

print(result)

# Q-6. Which of the following statements given below is/are true?
# Answer:  C. Tuples are immutable, lists are mutable.

# Q-7. What will be the output of the following code block?
# Answer:  D. Runtime Exception.

l = [1, 2, 3]
init_tuple = ('Python',) * (l._len_() - l[::-1][0])

print(init_tuple)

# Q-8. What will be the output of the following code block?
# Answer: B. <class ‘str’>

init_tuple = ('Python') * 3

print(type(init_tuple))

# Q-9. What will be the output of the following code block?
# Answer:  D. TypeError: ‘tuple’ object does not support item assignment

init_tuple = (1,) * 3
init_tuple[0] = 2
print(init_tuple)

# Q-10. What will be the output of the following code block?
# Answer: C. 4

init_tuple = ((1, 2),) * 7
print(len(init_tuple[3:8]))