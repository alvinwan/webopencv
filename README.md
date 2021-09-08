# webopencv
Using WebRTC, stream live video feed from a webpage to a server-side OpenCV Python script. This is primarily written for educational purposes, **giving students the ability to work with a webcam, without installing anything on their computers**. Most importantly, this library enables larger-scale, remote computer vision courses that make use of the webcam.

This sidesteps a major issue with most computer vision tutorials that make use of the webcam: (1) Installing the necessary Python packages is already a major barrier. (2) Webcam access is finicky at best. Instead, this library allows you to (1) automatically install Python packages on a clean docker image and (2) only requires well-established web-based video protocols. 
