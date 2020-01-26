"""Author: Brandon Trabucco, Copyright 2020, MIT License"""


from pixelcnn import conditional_pixelcnn_plus_plus
import tensorflow as tf


if __name__ == "__main__":

    model = conditional_pixelcnn_plus_plus(
        32,     # conditional_vector_size
        256,    # output_size
        conditional_height=4,
        conditional_width=4,
        image_height=32,
        image_width=32)

    inputs = tf.random.normal([12, 4, 4, 32])
    images = tf.random.uniform(
        [12, 32, 32],
        maxval=256,
        dtype=tf.dtypes.int32)

    logits = model([images, inputs])

    loss = tf.keras.losses.sparse_categorical_crossentropy(
        images,
        logits,
        from_logits=True)
    loss = tf.reduce_mean(loss)

    print("loss {}: logits shape: {}".format(
        loss.numpy(), logits.shape))
