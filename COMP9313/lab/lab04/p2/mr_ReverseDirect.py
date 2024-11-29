### We use value-to-key conversion to do this task, and let Hadoop do the sorting for us.
### Unfortunately, there is no GroupingComparator in MRJob. We have to process each pair in one reduce function.

from mrjob.job import MRJob
from mrjob.step import MRStep

class ReverseEdgeDirection(MRJob):

    def mapper(self, _, value):
        fromNode, neighbor = value.split("\t", 1)
        nodes = neighbor.strip().split(" ")

        #MRJOB has a wierd bug, the first field of the key cannot be sorted by numeric values
        #We have to add a useless first field...
        #No need to do this if you do not sort the first field by numeric values
        for node in nodes:
            yield "a," + node + "," + fromNode, ""    
    
    def reducer_init(self):
        self.neighbor=[]
        self.curNode=""
    
    # Note that the reduce design is based on the fact that the pairs come in order.
    def reducer(self, key, values):
        a, node, fromNode = key.split(",")
        if(node == self.curNode):
            self.neighbor.append(fromNode)
        else:
            if self.curNode!="":
                yield self.curNode, " ".join(self.neighbor)
            self.neighbor=[]
            self.neighbor.append(fromNode)
            self.curNode=node
            
    def reducer_final(self):
    	# Do not forget the last node
        yield self.curNode, " ".join(self.neighbor) 
    
    SORT_VALUES = True

    def steps(self):        

        JOBCONF = {
          'stream.num.map.output.key.fields':2,
          'mapreduce.map.output.key.field.separator': ',',
          'mapreduce.job.reduces':2,
          'mapreduce.partition.keypartitioner.options':'-k1,2',
          'mapreduce.job.output.key.comparator.class':'org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator',
          'mapreduce.partition.keycomparator.options':'-k2,2n -k3,3n'
        }
        return [MRStep(jobconf=JOBCONF, mapper=self.mapper, reducer=self.reducer, reducer_init= self.reducer_init, reducer_final=self.reducer_final)]


if __name__ == '__main__':
    ReverseEdgeDirection.run()
