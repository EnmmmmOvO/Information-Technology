# COMP9319 Exercises 02

Final answers are provided below for your checking only. If you have issues to work out the answers, please come to the online consultations.

## Question 1

Adaptive Huffman Coding (Vitter's) is used to encode a string with a vocabulary of three letters a, b, c.

The initial coding before any transmission is: a=01100001, b=01100010, c=01100011.

Derive the encoded bitstream produced by the encoder for the string **abcbaaa**. Draw the adaptive Huffman trees after each letter is processed.

>  Ans: 01100001 001100010 1001100011 10 10 11 0

## Question 2

Adaptive Huffman Coding (Vitter's) is used to encode a string with a vocabulary of three letters a, b, c.

The initial coding before any transmission is: a=01100001, b=01100010, c=01100011.

Derive the encoded bitstream produced by the encoder for the string **bcaaabbb**.

> Ans: 01100010 001100011 1001100001 01 0 011 11 11

## Question 3

Given an Adaptive Huffman (Vitter's) encoded bitstream: **011000010011000100111101** (Looks familiar?)

The initial coding before any transmission is: a=01100001, b=01100010.

Derive its corresponding decoded message (i.e., the output produced by its corresponding decoder).

> Ans: abaaaaab