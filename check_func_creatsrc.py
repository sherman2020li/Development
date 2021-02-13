import sys
import os
import re
import linecache
import xlrd

xlsfile = "arch_index.xlsx"

def func_rd_txd():
   path = os.getcwd()
   print("hahaha"+path)
   txt = open("linelist.txt",'r')
   for row in txt:
      ilnelist = row.split(",")
      print(ilnelist)
      if("heat" in row):
         print("true")
         break
#-------------------------------------
def test_string_split():
   X1 = re.split('\W+', 'runoob, runoob, runoob.')
   print(X1)
   X2 = re.split('(\W+)', ' runoob, runoob, runoob.') 
   print(X2)
   X3 = re.split('\W+', ' runoob, runoob, runoob.', 1) #split once
   print(X3)
   
def   fun_Write_csource():
   txt = open("temp.c",'w+')
   testStr = "hello world, Sherman Li Marked"
   sta = txt.write(testStr)
   if (sta):
      print("write success")
   else:
      print("write failed")


def fun_readExl():
   src_set = None
   hdr_set = None
   xlswb = xlrd.open_workbook(xlsfile)
   sheet1 = xlswb.sheet_by_name("service")
   print("row number is : ",sheet1.nrows)
   print("column number is : ",sheet1.ncols)
   rowv = sheet1.row_values(2)
   #print(rowv)
   src_index_col = 4
   f_dec_col = 11
   f_def_col = 14

   rowlines = sheet1.nrows
   for line_index in range(rowlines):
      srcname = sheet1.cell_value(line_index,src_index_col)# c file name
      hdrname = sheet1.cell_value(line_index,src_index_col+1) # header file name
      celltype = sheet1.cell(line_index,src_index_col).ctype
      # print("line index: ",line_index)
      # print("col index: ",src_index_col)
      #nameRet = re.search("*.c",str(srcname))

      if(celltype == 1):# cell content type is string
         print("c file is : ",srcname)
         if(".c" in srcname):
            src_set = open(srcname,'w+')#open file in append mode
            hdr_set = open(hdrname,'w+')#open file in append mode
      else:
         print("not not")
         
      hasFuncDef = sheet1.cell(line_index,f_dec_col+3).ctype
      if(hasFuncDef == 1):# cell content type is string
         f_def_record = sheet1.cell_value(line_index,f_dec_col+3) # read line by line
         f_dec_record = sheet1.cell_value(line_index,f_dec_col)
         if(src_set):
            src_set.write(f_def_record+"\n"+"\n") #write append
            hdr_set.write(f_dec_record+"\n") #write append
         else:
            print("oops None")

#-------------------------------------
#test_string_split()
#fun_Write_csource()
#func_rd_txd()
fun_readExl()
