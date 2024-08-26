# COMP9319 Exercises 05

**Solution :** See us at the consultations if there are questions with the answers below.

## Question 1

Construct the suffix array for string S = **panorama$** using the linear time construction algorithm discussed in the lectures.

What is its BWT?

> Ans: 8,7,5,1,6,2,3,0,4. amrpaan$o

## Question 2

Construct the suffix array for string S = **enhancement$** using the linear time construction algorithm discussed in the lectures.

What is its BWT?

> Ans: 11,3,5,6,0,8,2,7,4,1,9,10. thnc$mneaeen

## Question 3

Construct the suffix array for string S = **here_there_and_where$** using the linear time construction algorithm discussed in the lectures.

>  Ans: 20, 10, 4, 14, 11, 13, 19, 9, 3, 17, 7, 1, 16, 6, 0, 12, 18, 8, 2, 5, 15

## Question 4

In the linear time SA construction algorithm, why do we separate S positions from L positions? Why do we place L positions in front of other S positions for each bucket?

>  Ans: (i) To reduce the number of suffixes to be sorted. (ii) Consider the bucket for char x, S positions => the chars after x are larger, whilst L positions => the chars after x are smaller. Therefore, L suffixes are smaller than S suffixes within a bucket.