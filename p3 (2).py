#!/usr/bin/env python
# coding: utf-8

# In[ ]:


{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "82c8479a",
   "metadata": {},
   "source": [
    "# Russian Doll recursive function ###"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8add28b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All dolls are opened\n"
     ]
    }
   ],
   "source": [
    "def openRussianDoll(doll):\n",
    "    if doll == 1:\n",
    "        print(\"All dolls are opened\")\n",
    "    else:\n",
    "        openRussianDoll(doll-1)\n",
    "\n",
    "\n",
    "openRussianDoll(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66ca09e7",
   "metadata": {},
   "source": [
    "## def recursionMethod(parameters):\n",
    "##     if  exit from condition satisfied:\n",
    "##         return some value\n",
    "##     else:\n",
    "##        recursionMethod(modified parameters)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "61d2e5b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am the fourth Method\n",
      "I am the third Method\n",
      "I am the second Method\n",
      "I am the first Method\n"
     ]
    }
   ],
   "source": [
    "def firstMethod():\n",
    "    secondMethod()\n",
    "    print(\"I am the first Method\")\n",
    "\n",
    "def secondMethod():\n",
    "    thirdMethod()\n",
    "    print(\"I am the second Method\")\n",
    "\n",
    "def thirdMethod():\n",
    "    fourthMethod()\n",
    "    print(\"I am the third Method\")\n",
    "\n",
    "def fourthMethod():\n",
    "    print(\"I am the fourth Method\")\n",
    "\n",
    "\n",
    "firstMethod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "da6c9762",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "n is less than 1\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "def recursiveMethod(n):\n",
    "    if n<1:\n",
    "        print(\"n is less than 1\")\n",
    "    else: \n",
    "        recursiveMethod(n-1)\n",
    "        print(n)\n",
    "\n",
    "recursiveMethod(4)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0a6b8a86",
   "metadata": {},
   "source": [
    " ### Recursion vs Iterarion###"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b7afdfd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def powerOfTwo(n):\n",
    "    if n == 0:\n",
    "         return 1\n",
    "    else:\n",
    "        power = powerOfTwo(n-1)\n",
    "        return power * 2\n",
    "\n",
    "print(powerOfTwo(4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80f0f66e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def powerOfTwoIt(n):\n",
    "    i = 0\n",
    "    power = 1\n",
    "    while i < n:\n",
    "        power = power * 2\n",
    "        i = i + 1\n",
    "    return power\n",
    "\n",
    "\n",
    "print(powerOfTwoIt(4))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d80d1efd",
   "metadata": {},
   "source": [
    " ### Factorial###"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c451bf58",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "def factorial(n):\n",
    "    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'\n",
    "    if n in [0,1]:\n",
    "        return 1\n",
    "    else:\n",
    "        return n * factorial(n-1)\n",
    "\n",
    "print(factorial(4))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fffc35d3",
   "metadata": {},
   "source": [
    "### Fibonacci###"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "778c030b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13\n"
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'\n",
    "    if n in [0,1]:\n",
    "        return n\n",
    "    else:\n",
    "        return fibonacci(n-1) + fibonacci(n-2)\n",
    "\n",
    "print(fibonacci(7))\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

