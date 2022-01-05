# flask-image-server
Simple Flask image server saving images over POST requests

**POST** /image/upload
````
@param image_file 
````
Return Example
````
{
    "status": "success",
    "image_path": "http://127.0.0.1:5000/static/upload/coming-soon-logo.png"
}
````