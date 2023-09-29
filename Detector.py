import tensorflow as tf
import cv2
def run_detection():
# Load the model
    model = tf.saved_model.load('exported_models/my_model/')

    # Load the image
    image = cv2.imread('./screenshot.png')

    # Convert the image to a tensor
    image_tensor = tf.convert_to_tensor(image)

    # Add a batch dimension
    image_tensor = tf.expand_dims(image_tensor, axis=0)

    # Perform inference
    output_dict = model(image_tensor)

    # Get the detection boxes, scores, and classes
    boxes = output_dict['detection_boxes'][0].numpy()
    scores = output_dict['detection_scores'][0].numpy()
    classes = output_dict['detection_classes'][0].numpy()

    # Filter out low-confidence detections
    detections = []
    for i in range(len(boxes)):
        if scores[i] > 0.5:
            ymin, xmin, ymax, xmax = boxes[i]
            detections.append((xmin, ymin, xmax, ymax, classes[i]))
            
    coordinates = []
    # Print the detections
    for detection in detections:
        xmin, ymin, xmax, ymax, class_id = detection
        print('Detected {} at ({}, {}, {}, {})'.format(class_id, xmin, ymin, xmax, ymax))
        coordinate_center = ((xmin+xmax)/2, (ymin+ymax)/2)
        coordinates.append(coordinate_center)

    return coordinates