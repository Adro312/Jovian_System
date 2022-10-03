# Jovian System
In order to run this web application from a local server, you need to have the following installed:
* Python 
* django 
* Pillow 
* OpenCV 
* Numpy
* Image Magrek
* Matplotlib
* Wand

Before starting a local server to be able to view it, you need to execute these two command lines to migrate the project:

```
py manage.py makemigrations
```
then
```
py manage.py migrate
```
and finally, you can run the command to generate a local server and IP address to display it in the browser:
```
py manage.py runserver
```
