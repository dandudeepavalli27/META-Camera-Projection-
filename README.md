# META-Camera-Projection-
#Aim
To compute the 2D image coordinate from 3D world coordinates using the pinhole camera model.
General Objective
To understand the principles of camera geometry and how 3D world coordinates are projected onto a 2D image plane using the pinhole camera model, as applied in AR/VR systems.
Specific Objective
To apply the projection formula:
u
=
f
X
Z
u= 
Z
fX
​	
 
with:
f
=
600
f=600 (focal length)
X
=
3
X=3 (horizontal coordinate)
Z
=
6
Z=6 (depth)
Dataset
ETH3D Camera Dataset
Source: ETH3D
#Procedure
Define focal length 
f
f
Define 3D coordinates 
X
X and 
Z
Z
Apply projection formula
Compute pixel coordinate 
u
u
Display result
#Algorithm
Start
Input values 
f
,
X
,
Z
f,X,Z
Apply formula 
u
=
f
X
Z
u= 
Z
fX
​	
 
Compute value of 
u
u
Display result
Stop
#Result
The projected pixel coordinate on the image plane is:
u = 300 pixels
Industry Application
Camera projection is widely used in:
Augmented Reality (AR)
Virtual Reality (VR)
3D reconstruction
Robotics vision
Companies like Meta Platforms use this concept in:
AR glasses
VR headsets
Spatial computing systems
#Conclusion
The pinhole camera model successfully maps 3D world coordinates to 2D image coordinates, which is fundamental for AR/VR and computer vision applications.
