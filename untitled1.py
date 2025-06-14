import tensorflow as tf

# Load the Keras model (replace '1.keras' with the actual filename of your model)
model = tf.keras.models.load_model('1.keras')  # Replace '1.keras' with your model's file name

# Print the model summary to confirm it's loaded
model.summary()

# Convert the model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted model as 'model.tflite'
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Model converted to TFLite format successfully and saved as 'model.tflite'")
