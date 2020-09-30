for i in range(len(input_table['Column'].values)) :
	if input_table['Column'].values[i] == "cluster_0" :
		input_table['Column'].values[i] = "0"
	if input_table['Column'].values[i] == "cluster_1" :
		input_table['Column'].values[i] = "1"

# Copy input to output
output_table = input_table.copy()
