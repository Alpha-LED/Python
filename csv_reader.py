#-*- coding: utf-8 -*-

"""

This script transform data from CSV file with '.txt' and '.csv' extensions to a 
table, represent the above data stored in html file '.html'.
First we need to add arguments to the commands line to give a sens to ower
data, these arguments are ,by order, file name or the path, number of columns and 
the separator '\t',';' and ',' .

"""
import sys


var = 0
file_name = ""
columns_numb = 7
separator = "\t"


html  = []
head  = ["<html>\n<head>\n"]
title = ["<title>Web Page From a CSV file</title>\n"]
style = ["<style>table, th, td{border: 1px solid black}\n th,td{padding: 15px; text-align: left}</style>\n"]
body  = ["</head><body>\n"]
table = ["<table style=\"width:100%\">\n"]
end   = ["</table>\n</body>\n</html>"]

def get_arguments():
	global columns_numb
	global file_name
	global separator

	arguments = sys.argv
	lengh = len(arguments)
	if arguments[lengh - 1] == ";" or arguments[lengh - 1] == ",":
		separator = arguments[lengh - 1]
	columns_numb = int(arguments[lengh-2])
	file_name = arguments[lengh-3]
	print(arguments)

def write_html_page():
	"""
	Write the HTML code into a file.

	"""
	if file_name.endswith(".txt"):
		file = file_name.replace(".txt",".html")

	elif file_name.endswith(".csv"):
		file = file_name.replace(".csv",".html")

	with open(file,"w") as file_html:
		file_html.writelines(html) 

def HTML():
	"""
	Initialize the HTML page base on a List of html code.

	"""
	global html
	html += head + title + style + body + table + end

def table_constractor(line):
	"""
	
	Create Lines and Coloumns using html Syntexe .

	"""
	global var
	
	if var == 0 :
		table.append("<tr>\n")
		for i in range(columns_numb):
			table.append("<th>"+line[i]+"</th>")
		table.append("</tr>")
		var = 1
	else :
		table.append("</tr>")
		for j in range(columns_numb):
			table.append("<td>"+line[j]+"</td>")
		table.append("</tr>")


def lines_constractor(list_words):
	"""

	Prepairing table's Lines to be coded in html.

	"""
	line=[]
	x = 0
	for i in range(int(len(list_words)/columns_numb)):
		for j in range(columns_numb):
			line.append(list_words[x])
			x += 1
		table_constractor(line)
		line=[]
		

def read_csv_file():
	"""

	Read File and Create a list that containe all words
	and eleminate the separator.

	"""
	list_words=[]
	with open(file_name,"r") as file_csv:
		list_lines = file_csv.readlines()
		for line in list_lines:
			list_words += line.split(separator)
		lines_constractor(list_words)
	


get_arguments()
read_csv_file()
HTML()
write_html_page()

