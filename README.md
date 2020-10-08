## Taste Buds Dream or TBD

<img src="{{url_for('static', filename='images/homepage.png')}}">
<img src="{{url_for('static', filename='images/my_recipes.png')}}">
<img src="{{url_for('static', filename='images/thermomix.png')}}">
<img src="{{url_for('static', filename='images/about.png')}}">
<img src="{{url_for('static', filename='images/contact.png')}}">
<img src="{{url_for('static', filename='images/login.png')}}">

What is TBD?
TBD is for anyone who likes cooking: 
there is a large range a recipes, the public can read through and try themselves with.
The recipes are not only for regular home chef but also those who count the Thermomix appliance as part of their cooking appliance.
As opposed to other recipe site, where anyone can log in, edit, create, delete their recipes, TBD is a website dedicated to one user only, 
the owner, and is made for the public to enjoy looking at food, recipes and how they are made.
To sum up, anyone looking to spice up and level up their cooking style with or without the Thermomix should be interested in this site. 

UX
As a user, anyone whom enjoy cooking will first have the ability to search through a large range of recipes, those recipes are made for a certain number
of persons and have a preparation time displayed so to get better organised.
The search can either result in a thermomix or other type of recipe. Not restricting the user by selecting either/or will allow him/her to get inspired 
by any recipe instead of being specific unless they request so. In that case, the user is welcomed to use the 'thermomix' or 'other' criteria in their search.

The recipe cards provide a good bit of information to each user as a walkthrough to cook a specific meal. if however, a user is interested to
have it in writing, there is a download button offered to do so.

Apart from browsing each recipes or searching for a specific ingredients, type or category (vegan, gluten-free..), each
user can have a glimpse of what the thermomix offer. After all, the site owner is a thermomix advisor and want to share that experience with as many
potential customers as possible. 
Surfing through the thermomix page, a video welcomes the user, it is the official thermomix video and the owner's word on her own experience
will give a sense of similarity to the user.

Demos were available on site but since COVID19, the owner wants to set up live demos through Zoom which will be discussed in the feature for the future, but so far,
to get ahead and insite the visitors to come back, an agenda has been laid out on that page.

The About gives a good idea of whom the owner is and hope with those amazing characteristics: travel, culture, culinary experience, to be able to promote herself and 
the thermomix to convert traffic into demos lovers and eventually sales.

We are offering 2 ways for any user to contact the owner:
- a chat bubble which provides a sense of uniqueness to a recipe site but above all it brings it to a different level as any culinary or thermomix question can be answered
on the spot.
- a contact form, anyone not having the time to chat can leave a message which will be answered to at a later stage, however, the user gets a nice message letting him know that the owner
recieved his com.

That ends the first part of the site

The second part of the site is dedicated to the Creating, Editing, Deleting, Updating the recipes as well as encompasses the admin chat
It is very important to note at this stage the login holds a 'register' option for the purpose of the MS3 project required by the Code 
Institute, however this option will be delete as soon as the project is scored.

After logging in, the user has the option to:
--Edit an existing recipe which leads to updating it in the database or canceling the action which will bring her back to all the options view.
--Creating new recipe and saving it or reseting the form or cancelling this action which will bring her back to all options
--Deleting the existing recipe, a confirmation message will pop just to make sure it is the right action meant to be taken

--Creating a new category (vegan...) which leads to creating a new category or chosing editing category option
--Editing the existing categories will give her the option to delete them or edit if there is a typo. Upon deletion a confirmation message will pop up to make sure it 
is the right action meant to be taken.

--Opening the admin chat. As it is a one person owning the website, it is on her to control the admin chat. The only way to the admin chat is 
through the login. The chat admin will open in a new window, and it gives the option to choose which conversation to answer first.

Once all required changes are made, the owner can log out, a message will appear confirming that action.

## Wireframes

## Features

Currently and as already discussed, TBD offers:

1 -- Search form: for any visitors to search by recipe name, ingredients, type(vegan...), thermomix or other
2 -- Recipe cards: offers a picture of the recipe in question, the recipe method, preparation time, number of people, type, category as well as a DOWNLOADABLE RECIPE CARD
3 -- Video: Thermomix official youtube video
4 -- Chat bubble and its admin chat: to interact directly with every user who wnats to discuss the site, a recipe, the thermomix
5 -- Email form: for anyone to reach out by email
6 -- login credentials to enter the CRUD capabilities
7 -- Registering option: which will be deleted as discussed above
8 -- CRUD capabilities:
        -- Creating, Deleting, Updating and Editing any recipes
        -- Creating, Deleting, Updating and Editing any categories (vegan..)
10 -- Log out
11 -- Live calendar
12 -- linking with social media

## Features Left to Implement

Interactive Calendar -- Zoom live demo integration
We will be looking in the near future to implement a Live Zoom Demo center in the site which will be linked to the calendar.
In fact, the calendar will show the Demo events, and we will give the ability for 5 lucky user to join. The demos are mainly thermomix centered.

Integrate with Facebook calendar as soon as it is completed to give more visibility to the site.

A possibility to change the number of people per meal so that the recipes ingredients align.

In a longer future: an eventual calorie counter will be added to the recipes

## Technologies Used

HTML, or Hyper Text Markup Language
CSS, or Cascading Style Sheets
Materialize
Javascript
Python
Flask
Pusher
Pymongo
MongoDB
Cloudinary
Fullcalendar.io
Gitpod
Git
GitHub
Chrome DevTools:
W3C Markup Validation Service
Heroku for deplyoment

## Testing

http://ami.responsivedesign.is/ has been used to see how the site performs on different Apple devices and their viewports, all pages, links, icons performed as expected on all devices.
Desktop
Google Chrome, Internet Edge & Mozilla Firefox browsers; all pages, links on those pages, and footer icon links perform well on all viewport sizes. Developer tools were also used on 
all browsers for the various viewport sizes.
Mobile
used Huawei CLT-L09, Samsung Note 9, Iphone 4 and 5 to check every pages and links, all performs well on all devices.

Issues:


## Deployment
Deployment was made with Heroku:
Working with Github, the workplace is created and all files worked on gitpod.

## Credits
Credit to the API fullcalendar.io which was very easy to use and the walkthrough as well as demos easy to understand. Couple of 
codepens were visited to get inspired for the js code.

Full credit to the Pusher chat widget https://pusher.com/tutorials/chat-widget-python#prerequisites

w3schools for some hints on smoth scrolling top with href and id

## media
Am I Responsive web site for checking responsiveness on all Apple devices screen sizes; http://ami.responsivedesign.is/

https://stackoverflow.com/ w3schools Used as a resource for finding answers to all types of coding problems.

JSHint to check my javascripts codes

W3 validator to check html and css codes


## Acknowledgements

All of the Code institute members whom have provided great opinions, insights on my project and especially Kevin for the great tutoring session.
My super mentor Adeye Adegbenga for his time, great advices and all the support provided to achieve this project.
My family for giving me the precious time to study, work on the projects and keep it up






To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
