# Dynamic Website Design for a Manufacturing Company

### Webpage URL: http://aoashwin.student.saveetha.in:8000/
### git hub repo URL: https://github.com/aoashwin/companywebsitedynamic.git

## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <link rel = "icon" href ="{% static 'img/titleicon.png' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
        _______Silicon Private Limited
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contactus">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2020 Silicon Private Limited, Developed by Ao Ashwin.
    </div>
    </div>
</body>

</html>
```
### home.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building.jpg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
{% endblock  %}

```
### products.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="productcontent">    
        <h1>OUR PREMIUM PRODUCT</h1>
    </div>
    <div class="productitems">
        {% for product in products %}
        <div class="productitem"> 
            <div>
            <img src="{{ product.photo.url }}" alt="product image" width="200" height="200">
            </div>
            <div class="itemname"><h3>{{ product.itemname }}</h3></div>
            <div class="itemprice"><h4>Rs.{{ product.price }}</h4></div>
        </div>
        {% endfor %}
    </div>
{% endblock %}
```
### people.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="peoplecontent">
        <h1>Chief Officer's</h1>
    </div>
    <div class="peoplelists">
        {% for people in peoples %}
        <div class="peoplelist">
            <div class="peopleimage">
                <img src="{{ people.photo.url }}" alt="peopleimage" width="180" height="250">
            </div>
            <div class="peoplename"><h2>{{ people.membername }}</h2></div>
            <div class="peoplepost"><h3>({{ people.designation }})</h3></div>
        </div>
        {% endfor %}
    </div>
{% endblock  %}
```
### contactus.html
```
{% extends "website/base.html" %}

{% block content %}
    <div class="contactuscontent">
        <div class="contactbox">
            <div>
                <img src="/static/img/Contact-Us.png" alt="contactusimg">
            </div>
        </div>
        <hr/>
        <div class="contactemail"><h1>Email: aosiliconcompany@gmail.com</h1></div>
        <div class="contactphone"><h2>Phone: +91-9159425427</h2></div>
        <div class="contactphone"><h2>Address: © Silican pvt,Mountain View, California, United-States</h2></div>
        <hr/>
    </div>

{% endblock %}
```
## OUTPUT:
![output](./static/img/home.png)

![output](./static/img/product.png)

![output](./static/img/people.png)

![output](./static/img/contactus.png)

## ADMIN PAGE:
![output](./static/img/peopleadmin.png)

![output](./static/img/productadmin.png)

## CODE VALIDATION REPORT:
![output](./static/img/validhome1.png)

![output](./static/img/validproduct1.png)

![output](./static/img/validpeople1.png)

![output](./static/img/validcontactus1.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://aoashwin.student.saveetha.in:8000/. HTML code is validated.