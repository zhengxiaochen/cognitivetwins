import tensorflow as tf
from TFModel import TFModel
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Get the training data from the table
x_train = input_table.iloc[:,:-3].values

y_train = input_table.iloc[:,-2:].values

# Set some training varibales
batch_size = 30
epochs = 1000
learning_rate = 0.001

# Get some handy variables
num_classes = y_train.shape[1]
num_samples = x_train.shape[0]
num_batches = int(np.ceil(num_samples/batch_size))

print('Training for {} epochs on {} batches of size {}.'.format(epochs, num_batches, batch_size))

# Use the session from the TFModel
with input_network.session as sess:
	
	# Get the input tensor
	x = input_network.inputs['input']
	
	# Get the output tensor
	y_hat = input_network.outputs['output']
	
	# Define the ground truth tensor
	y = tf.placeholder(dtype=tf.float32, shape=(None,num_classes),name='y')
	
	# Define the loss
	loss = tf.losses.mean_squared_error(y, y_hat)
	
	# Define optimizer and training op
	optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate)
	train = optimizer.minimize(loss,name='train')

	# Initialize all variables
	sess.run(tf.global_variables_initializer())

	for epoch in range(epochs):
		# The average loss for this epoch
		avg_loss = 0

		# Loop over all batches
		for i in range(num_batches):
			# Extract batch
			fr = int(i*batch_size)
			to = int(np.minimum((i + 1)*batch_size, num_samples))
			x_batch = x_train[fr:to,...]
			y_batch = y_train[fr:to,...]

			# Run training op
			_, l = sess.run([train, loss], feed_dict={x: x_batch,
													  y: y_batch})
			# Compute average loss
			avg_loss += l / num_batches

		# Display logs per epoch step
		print("Epoch: {}, loss={:.9f}".format(epoch, avg_loss))
	print("First Optimization Finished!.")
	
	# Create the output network
	# NOTE: The whole session is passed to the model (to save the variables)
	#       This needs to be called before the session is closed
	output_network = TFModel(inputs=x, outputs=y_hat, session=sess)