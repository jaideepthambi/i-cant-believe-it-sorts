# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:03:57 2021

@author: JaideepThambi
"""

A = [5, 9, 3, 5, 7, 5, 8, 23, 1, 2, 5, 23]

for i in range(0, len(A)):
    for j in range(0, len(A)):
        if A[i] < A[j]:
            print(i, j)
            print(A[i], A[j])
            print("Swapping")
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
            print(A)

print("\n\nThe sorted array:")
print(A)
