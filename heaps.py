#I will be implementing a heap using an array      
class MinHeap:
    def __init__(self,capacity):
        self.storage=[0]*capacity
        self.capacity=capacity
        self.size=0 #This will be the number of element in our array

    #HERE WE HAVE TO DEFINE OTHER HELPER METHODS   
    def getParentIndex(self,index):
        return (index-1)//2

    def getLeftChildIndex(self,index):
        return 2*index+1

    def getRightChildIndex(self,index):
        return 2*index+2

    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size

    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size

    #THE BELOW HELPER METHODS HELPS US TO GET VALUES OF THE VARIOUS NODE 
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]

    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self,index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size==self.capacity 

    def swap(self,index1,index2):
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp

    #THIS IS HOW WE WILL INSERT AN ELEMENT INTO OUT HEAP(THIS IMPLEMENTATION IS A FOR A MIN HEAP)
    #THIS IS THE IMPLEMENTATION FOR AN ITERATIVE APPROACH 
    # def insert(self,data):
    #     if self.isFull():
    #         raise("Heap is full")
    #     self.storage[self.size]=data
    #     self.size+=1
    #     self.heapifyUp()

    # def heapifyUp(self):
    #     index=self.size-1
    #     while(self.hasParent(index) and self.parent(index)>self.storage[index]):
    #         self.swap(self.getParentIndex(index),index)
    #         index=self.getParentIndex(index)


    #THIS IS THE RECURSIVE IMPLEMENTATION 
    #THIS APPROACH IS MOSTLY RECOMMENDED SINCE MOST IMPLEMENTATION OF TREES METHODS USES THE CONCEPT OF RECURSSION 
    def insert(self,data):
        if self.isFull():
            raise("Heap is full")
        self.storage[self.size]=data
        self.size+=1
        self.heapifyUp(self.size-1)

    def heapifyUp(self,index):
        if(self.hasParent(index) and self.parent(index)>self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index=self.heapifyUp(self.getParentIndex(index))


    #FOR THIS I WILL GO AHEAD AND IMPLEMENT THE RECURSIVE APPROACH 
    def removeMin(self):
        if self.size==0:
            raise('Empty Heap')
        data=self.storage[0]
        self.storage[0]=self.storage[self.size-1]
        self.size-=1
        self.heapifyDown(0)
        return data

    def heapifyDown(self,index):
        smallest=index
        if (self.hasLeftChild(index) and self.storage[index]>self.leftChild(index)):
            smallest=self.getLeftChildIndex(index)

        if (self.hasRightChild(index) and self.storage[smallest]>self.rightChild(index)):
            smallest=self.getLeftChildIndex(index)

        if (smallest!=index):
            self.swap(index,smallest)
            self.heapifyDown(smallest)