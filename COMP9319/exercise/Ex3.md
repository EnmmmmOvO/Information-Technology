# COMP9319 Exercises 03

**Solution :** Talk to us at the consultations if you have questions with the answers below.

## Question 1

Suppose that the BWT encoded string BWT(S) = n$rsoocimpse

Derive the original string S.

>  Ans: compression$

## Question 2

Suppose that the BWT encoded string BWT(S) = e$mcoosrmho

Derive the original string S.

> Ans: chromosome$

## Question 3

Suppose that the original string S = ogloge

Since the given string ends with a unique symbol e, assume you do not need to introduce a psuedo end symbol such as $. Derive BWT(S).

>  Ans: google

## Question 4

The Boyer-Moore Example (1) in Lecture Week 3 takes 11 comparisons to find the match of **rithm** on **a pattern matching algorithm**

Apply the Brute Force search and KMP to this example. How many comparisons are needed for each case? Which one (BF, KMP or BM) performs the worst?

> Ans: both need 29 comparisons, so both are worse than BM.

## Question 5

From the Boyer-Moore Example (2) of Lecture 3: find the pattern P: **abacab** from T: **abacaabadcabacab**

As mentioned in the lecture in Week 3, the steps shown in Boyer-Moore Example (2) do not consider the Good Suffix Rule for shifting. It only uses the last occurrence function (also called the bad character rule) for shifting.

Derive the good suffix table and apply the complete Boyer-Moore algorithm (i.e., with bad character and good suffix rules) to Example (2). How many comparisons are needed to find the match?

>  Ans: 15

## Question 6

From the KMP Example of Lecture 3: find the pattern P: **abacab** from T: **abacaabaccabacab**

Apply the complete Boyer-Moore algorithm (i.e., with bad character and good suffix rules) to the KMP Example above. How many comparisons are needed to find the match?

> Ans: 15