{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#known data\n",
    "Month\n",
    "Offspringperpair\n",
    "\n",
    "#Fibonacci logic\n",
    "c = a + b\n",
    "d = b + c\n",
    "\n",
    "\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Fonction\n",
    "def Wabbits(n, k):\n",
    "    b = 2\n",
    "    if n==0:\n",
    "        wp = 0\n",
    "        return wp\n",
    "    if n==1:\n",
    "        wp0 = 1\n",
    "        return wp0\n",
    "    else:\n",
    "        return Wabbits(n-1, k) + int(Wabbits(n-2, k))*k"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14415648500221"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Wabbits(31, 5)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
