'''
		-------		Abhishek Raushan
				CSE Department
		Indian Institute of Information Technology, Guwahati
'''
#!/usr/bin/python

import os,sys
from math import sqrt,pow

# To find new Centroid from the cluster lists
def newCentroid(clusterList,centroid):
	newC=findMeanDist(clusterList,centroid)
	print "New Centroids: ",newC,"\n"
	return newC

# To find the mean distance in the clusters and output new or same centroid list		
def findMeanDist(clusterList,centroid):
	GetX=0
	GetY=0
	c1=[]

	for j in range(len(centroid)):
		GetX=0
		GetY=0
		if len(clusterList[j])!=0:
			for i in range(len(clusterList[j])):
				GetX += clusterList[j][i][0]
				GetY += clusterList[j][i][1]
			CentX = float(GetX) /  len(clusterList[j])
			CentY = float(GetY) /  len(clusterList[j])
			c1.append((CentX,CentY))
			#print c1
	return c1

#Find the cluster to which specific point belongs to	
def FindClusters(dist):
	p=[]
	for k in range(0,len(centroid)):
		p.append([]) 
	
	for i in range(0,len(dist)):
		if dist[i]!=[]:
			p[dist[i].index(min(dist[i]))].append(points[i])
			
		
	return p
	

def Kmeans( points , centroid ):
	arr = []
	for i in range(len(points)):
		arr.append([])
	for i in range(len(points)):
		for j in range(len(centroid)):
			arr[i]=EucledianDistance( points[i] , centroid[j] , arr[i] )
		#print arr
		clusterList=FindClusters(arr)
		for k in range(len(centroid)):
			print "cluster",k, "contains : ",clusterList[k]
		newC=newCentroid(clusterList, centroid)

# Measure the distance between points and centroids
def EucledianDistance( points , centroid , arr ):
	arr.append(sqrt(pow((points[0] - centroid[0]), 2) + pow((points[1] - centroid[1]),2) ) )
	return arr
	
# To find points belongs to which cluster , we need centroids and datas
# datas stored in list of lists
# centroid stored in list of tuples


if __name__ == '__main__':
	
	import csv
	points = []
	
	#Data reading from csv file
	f=open( 'cluster.csv' , 'r' )
	reader = csv.reader( f , delimiter="," )
	for line in reader:
		points.append( [ int(line[0]) , int(line[1])] )
	#print points
	
	c1=(185,72)
	c2=(170,56)
	centroid=[c1,c2]
	
	Kmeans( points , centroid )
