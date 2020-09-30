# variable name of the output network:  output_network

import tensorflow as tf
from TFModel import TFModel
rowNum = int(flow_variables['Column 0'][3:]) + 1
input_shape = (None,rowNum)
num_classes = 2

# Create a graph
graph = tf.Graph()

# Set the graph as default -> Create every tensor in this graph
with graph.as_default():

	# Create an input tensor
	x = tf.placeholder(tf.float32,shape=input_shape, name='input')
	
	# Dense Layer
	# Dense Layer
	dense1 = tf.layers.dense(inputs=x, units=100, activation=tf.nn.tanh)
	dense2 = tf.layers.dense(inputs=dense1, units=800, activation=tf.nn.tanh)
	dense3 = tf.layers.dense(inputs=dense2, units=2000, activation=tf.nn.tanh)
	dense4 = tf.layers.dense(inputs=dense3, units=500, activation=tf.nn.tanh)
	dense5 = tf.layers.dense(inputs=dense4, units=50, activation=tf.nn.tanh)
	
	# Create an output tensor
	y = tf.layers.dense(dense5, num_classes, activation=tf.nn.softmax, name='output')

# Create the output network
output_network = TFModel(inputs={'input': x}, outputs={'output': y}, graph=graph)