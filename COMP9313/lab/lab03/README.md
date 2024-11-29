# Lab03

Put files:
```shell
hdfs dfs -put pg100.txt input
```

Running python code with hadoop steaming:
```shell
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -input input -output output -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py
```

Remeber to delete output directory if exist.

Running `mrjob` code:
```shell
python3 mr_CoTermNSStripe.py -r hadoop hdfs://localhost:9000/user/comp9313/input/pg100.txt -o hdfs://localhost:9000/user/comp9313/output
```
`-o` indicates the output directory