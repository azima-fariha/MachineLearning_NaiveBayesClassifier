import csv
import pandas as pd
import numpy as np
import math
import argparse as ag
import os
from math import sqrt
import argparse
from functools import reduce

parser = argparse.ArgumentParser()
parser.add_argument("--data", help="INPUT TSV FILE PATH")
parser.add_argument("--output", help="Output File Path of TSV file for storing the results")
args = parser.parse_args()

input_file = args.data
output_file = args.output

#READ TSV FILE
with open(input_file,"r") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  row_count=0
  
  #INITIALIZING LISTS FOR 3 COLUMNS
  label_list=list()
  value_list_one=list()
  value_list_two=list()
  
  #CREATE LIST FOR EACH COLUMN  
  for row in reader:
    
    label_list.append(row[0]) #First column-Class Label A & B
    
    value_list_one.append(row[1]) #Second column for first feature
    
    value_list_two.append(row[2]) #Second column for second feature
    
    row_count+=1
    
  #print("Total no. of rows: ",row_count)
  #print(label_list)
  #print (value_list_one)
  #print(value_list_two)
    
  output_list_one_A=list()
  output_list_one_B=list()
  output_list_two_A=list()
  output_list_two_B=list()


  count=0

  for row in value_list_one:
        
    if label_list[count]=="A":
      output_list_one_A.append(value_list_one[count])
      count=count+1
    else:
      output_list_one_B.append(value_list_one[count])
      count=count+1  
  count_label_one_A=label_list.count('A')
 # print("Label A: ", count_label_one_A)
    
  count_label_one_B=label_list.count('B')
 # print("Label B: ", count_label_one_B)

  count=0

  for row in value_list_two:
        
    if label_list[count]=="A":
      output_list_two_A.append(value_list_two[count])
      count=count+1
    else:
      output_list_two_B.append(value_list_two[count])
      count=count+1  
  count_label_two_A=label_list.count('A')
  #print(count_label_two_A)
    
  count_label_two_B=label_list.count('B')
  #print(count_label_two_B)
    
    
  list_one_A=list(np.float_(output_list_one_A))  
  list_one_B=list(np.float_(output_list_one_B))  
  list_two_A=list(np.float_(output_list_two_A))  
  list_two_B=list(np.float_(output_list_two_B))  
    
  def Mean(list): 
    return sum(list) / len(list) 

  average_one_A = Mean(list_one_A)
  #print("Mean for column 1 label A: ",average_one_A)

  average_one_B = Mean(list_one_B)
 # print("Mean for column 1 label B: ",average_one_B)
    
  average_two_A = Mean(list_two_A)
  #print("Mean for column 2 label A: ",average_two_A)

  average_two_B = Mean(list_two_B)
  #print("Mean for column 2 label B: ",average_two_B)
    
  def Variance(list,mean):  
    return sum([(x-mean)**2 for x in list]) / float(len(list)-1)

  var_one_A= Variance(list_one_A,average_one_A)
  #print("Variance for columns 1 label A:  ",var_one_A)

  var_one_B= Variance(list_one_B,average_one_B)
  #print("Variance for columns 1 label B:  ",var_one_B)
    
  var_two_A= Variance(list_two_A,average_two_A)
  #print("Variance for columns 2 label A:  ",var_two_A)

  var_two_B= Variance(list_two_B,average_two_B)
  #print("Variance for columns 2 label B:  ",var_two_B)
    
  #CALCULATE PROBABILITY FOR EACH LABEL
  prob_label_A= count_label_one_A/row_count
 # print("Probability of Label A: ", prob_label_A)  

  prob_label_B= count_label_one_B/row_count
  #print("Probability of Label B: ", prob_label_B)  
    
  def Gauss(list,mean,variance):
    
     exponent = np.square([(x - mean) for x in list])
     exponent = -(exponent/(2 * variance))
     exponent = np.exp(exponent)
     result = 1 / np.sqrt(2 * np.pi * variance)
     result = result * exponent
     gauss_one.append(result)   
    # print("final step ",result)
     return result
  #list_one=list(np.float_(value_list_one)) 
   #list_two=list(np.float_(value_list_one)) 
    
    
  def Gauss1(list,mean,variance):
    
     exponent = np.square([(x - mean) for x in list])
     exponent = -(exponent/(2 * variance))
     exponent = np.exp(exponent)
     result = 1 / np.sqrt(2 * np.pi * variance)
     result = result * exponent
     gauss_two.append(result)   
    # print("final step ",result)
     return result
    
  gauss_one=list() 
  gauss_two=[]
  gauss_one_A= Gauss(list_one_A,average_one_A,var_one_A)
  gauss_one_B= Gauss(list_one_A,average_one_B,var_one_B)
  gauss_two_A= Gauss(list_two_A,average_two_A,var_two_A)
  gauss_two_B= Gauss(list_two_A,average_two_B,var_two_B)
  
  gauss_one_A1= Gauss1(list_one_B,average_one_A,var_one_A)
  gauss_one_B2= Gauss1(list_one_B,average_one_B,var_one_B)
  gauss_two_A3= Gauss1(list_two_B,average_two_A,var_two_A)
  gauss_two_B4= Gauss1(list_two_B,average_two_B,var_two_B)
  

  
  #print(gauss_one)
 # print("sdfdsfs ",gauss_one[0][1])  
  #print(gauss_one)
    
  col_one_A=list() 
  col_two_A=list() 
    

  #col_one_A.append(gauss_one[0])
  #col_two_A.append(gauss_one[2])
  
  #print("aaaaa  ",prob_A) 
  result_one=list() 
  result_two=list() 
    
  for i in range(len(list_one_A)):
    m=gauss_one[0][i]*gauss_one[2][i]
    result_one.append(m)
  #print("firt 200 A prob ",result_one)

  for i in range(len(list_one_A)):
    m=gauss_one[1][i]*gauss_one[3][i]
    result_two.append(m)
  #print("first 200 B prob ",result_two)
 
  result_label=[]
  count_mis=0
  for i in range(len(list_one_A)):
    if result_one[i]>result_two[i]:
      result_label.append("A")
    else:
      result_label.append("B")
      count_mis=count_mis+1
    
  #print(result_label)
  #print(count_mis)
        
        
        
  result_one1=list() 
  result_two1=list() 
    
  for i in range(len(list_one_B)):
    m=gauss_two[0][i]*gauss_two[2][i]
    result_one1.append(m)
  #print("last 200 A prob ",result_one1)

  for i in range(len(list_one_B)):
    m=gauss_two[1][i]*gauss_two[3][i]
    result_two1.append(m)
  #print("last 200 B prob ",result_two1)
 
  result_label1=[]
  count_mis1=0
  for i in range(len(list_one_B)):
    if result_one1[i]>result_two1[i]:
      result_label1.append("A")
      count_mis1=count_mis1+1
    else:
      result_label1.append("B")
      
    
  #print(result_label1)
  #print(count_mis1)
  
  missclassification=count_mis+count_mis1
  #print("Total Missclassification ", missclassification) 
  
  f = open(output_file, "w")

  f.write(str(average_one_A)+"\t")
  print(str(average_one_A)+"\t", end='')
  f.write(str(var_one_A)+"\t")
  print(str(var_one_A)+"\t", end='')
  f.write(str(average_two_A)+"\t")
  print(str(average_two_A)+"\t", end='')
  f.write(str(var_two_A)+"\t")
  print(str(var_two_A)+"\t", end='')
  f.write(str(prob_label_A))
  print(str(prob_label_A)+"\t", end='')
  f.write('\n')
  print('\n')
  f.write(str(average_one_B)+"\t")
  print(str(average_one_B)+"\t", end='')
  f.write(str(var_one_B)+"\t")
  print(str(var_one_B)+"\t", end='')
  f.write(str(average_two_B)+"\t")
  print(str(average_two_B)+"\t", end='')
  f.write(str(var_two_B)+"\t")
  print(str(var_two_B)+"\t", end='')
  f.write(str(prob_label_B))
  print(str(prob_label_B)+"\t", end='')
  f.write('\n')
  print('\n')
  f.write(str(missclassification))	
  print(str(missclassification)+"\t", end='')
  f.write('\n')
  print('\n')
 	
  f.close()
