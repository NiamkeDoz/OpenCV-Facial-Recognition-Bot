<h1>Open CV Facial Recognition</h1>
The following libraries will need to be installed with PIP
<ul>
<li>dlib</li>
<li>numpy</li>
<li>opencv-contrib-python</li>
<li>Pillow</li>
<li>cmake</li>
<li>image</li>
<li>Django</li>
<li>Face_recognition</li>
</ul>

To run files
`python3 face.py`
Window will display and program will continously take pictures when user's face is detected.

`python3 face-train.py`
Program will return images in array values to compare differences in images. 

`face_recognition ./known ./unknown`
This will take all images in unknown folder and known folder and compare for matches.
Returns filenames of images in known to the unknown images.



