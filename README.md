# Live object/Fashion detection and Recommendation
## With Tensorflow.JS
 
 I have used mobilenetV2 for object detection and localisation,
 
 If a person is detected using mobilenet then i have tried to 
 detect the top wear he/she is wearing using knn classifer 
 which comes with tensorflow.js for tranfer learning.
 
 Transfer Learning:  
 I have first passed the cropped image of the person from the canvas
 into mobilenetV1 to obtain inference then used the knn classifier to 
 predict the type of dress he is wearing.
 
 I have pre trained a knn classifer and saved its weights.
 These saved weights are loaded into the new knn classifier created 
 on the runtime

## Todo:
 * Improve Recomendation System
 * Improve Color Detection 