## Spatial and Textual Similarity Join (22 marks)

**Background**: Similarity join is an important task in data mining. In this project, you will do the spatial and textual similarity join. Each record R=(L, S) has two attributes: the spatial location in the 2D space (i.e., R.L is a coordinate (x, y)), and the textual description (i.e., R.S is a set of terms). 

Given a set of records, the task is to find all pairs of records such that they are close to each other and have a high textual similarity. Formally, each result pair must satisfy the following two conditions:

- Their Euclidean distance is smaller than a given threshold **d**, that is: 

$$
\sqrt{(R_1.L.x - R_2.L.x)^2 + (R_1.L.y - R_2.L.y)^2} \leq d
$$

- Their Jaccard Similarity is larger than a given threshold **s**, that is:

$$
\frac{|R_1.S \cap R_2.S|}{|R_1.S \cup R_2.S|} \geq s
$$

Given the following example (see the sample file), and set d = 2 and s=0.5, 

| id   | location | terms   |
| ---- | -------- | ------- |
| 0    | (0, 0)   | a d e f |
| 1    | (4, 3)   | b c f   |
| 2    | (1, 1)   | d e f   |
| 3    | (1, 2)   | a d f   |
| 4    | (2, 1)   | b e f   |
| 5    | (5, 5)   | c e     |

we can get the result pairs below:

| pair   | distance | similarity |
| ------ | -------- | ---------- |
| (0, 2) | 1.414214 | 0.75       |
| (2, 3) | 1.0      | 0.5        |
| (2, 4) | 1.0      | 0.5        |

**Output Format:** The output file contains all the similar records together with their similarities. The output format is 

```
(record1.id,record2.id):distance value, jaccard similarity value
```

Each pair must have *record1.id < record2.id*. For the distance and similarity values, **round the results to 6 decimal places** (using the round() function). There should be no duplicates in the output results. The pairs are sorted in ascending order (by the first and then the second). Given the sample dataset above with the distance threshold 2 and similarity threshold 0.5, the output result should be:

```
(0,2):1.414214, 0.75 
(2,3):1.0, 0.5 
(2,4):1.0, 0.5
```

**Code Format:** The code template has been provided. Your code should take three parameters: the input file, the output folder, the distance threshold d and the similarity threshold s. You need to use the command below to run your code: 

```
$ spark-submit project3.py input output d s
```

## **Some notes**

- You need to design an exact approach to finding similar records (*Please revisit Week 8 slides for more tips*).
- Check the paper mentioned in slides if you want to know more details [Efficient Parallel Set-Similarity Joins Using MapReduce. SIGMOD’10](https://flamingo.ics.uci.edu/pub/sigmod10-vernica.pdf)
- **You cannot compute the pairwise similarities directly!!!**
- Regular Python programming is not permitted in project3.
- When testing the correctness and efficiency of submissions, all the code will be run with *two local threads* using the default setting of Spark. Please be careful with your runtime and memory usage.

## **Marking Criteria**

Your source code will be inspected and marked based on readability and ease of understanding. The efficiency and scalability of this project are very important and will be evaluated as well.

- Submission can be compiled and run on Spark => +6 

- Accuracy (no unexpected pairs, no missing pairs, correct order, correct distance and similarity values, correct format) => +6           

- Efficiency (rules are shown as follows) => +10 

  The rank of runtime on the largest test case using two local threads, and correct and incorrect submissions will be ranked separately: 

  - *Correct results (e.g., top 10% => 10):*
    $$
    10 - \left\lfloor \frac{\text{rank percentage} - 1}{10} \right\rfloor
    $$

  - *Incorrect results:* 
    $$
    0.4 \cdot \left( 10 - \left\lfloor \frac{\text{rank percentage} - 1}{10} \right\rfloor \right)
    $$
    