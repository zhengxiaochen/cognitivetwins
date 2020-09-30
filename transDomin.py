# 转换数据维度
import pandas

table = pandas.DataFrame()

for i in range(max(input_table['Iteration'])+1):
	#input_table_1.loc[input_table_1['Iteration']==i]
	#input_table_2.loc[input_table_2['Iteration']==i]
	print(i)
	if i == 0: 
		table = pandas.DataFrame(columns = [str(i)], data = input_table.loc[input_table['Iteration']==i]['value'].values)
		#print(table)
	else:
		table[str(i)] = pandas.DataFrame(columns = [str(i)], data = input_table.loc[input_table['Iteration']==i]['value'].values)

output_table = table
	