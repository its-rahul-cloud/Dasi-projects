Face-detection algorithms focus on the detection of frontal human faces. It is analogous to image detection in which the image of a person is matched bit by bit. Image matches with the image stores in database. Any facial feature changes in the database will invalidate the matching process.[3]

A reliable face-detection approach based on the genetic algorithm and the eigen-face[4] technique:

Firstly, the possible human eye regions are detected by testing all the valley regions in the gray-level image. Then the genetic algorithm is used to generate all the possible face regions which include the eyebrows, the iris, the nostril and the mouth corners.[3]

Each possible face candidate is normalized to reduce both the lighting effect, which is caused by uneven illumination; and the shirring effect, which is due to head movement. The fitness value of each candidate is measured based on its projection on the eigen-faces. After a number of iterations, all the face candidates with a high fitness value are selected for further verification. At this stage, the face symmetry 
is measured and the existence of the different facial features is verified for each face candidate.[5]

see (https://en.wikipedia.org/wiki/Face_detection) for more info

#you can use this by
import pydaisi as pyd
emotion_detection = pyd.Daisi("rahul007/Emotion detection") 