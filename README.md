# Soilmate Plants - Introduction

Project milestone 5 for Code Institute Full-stack development program: Django Framework.<br>
Soilamate Plants is an E-commerce shop where users can find and buy plants and search for
products by filtering different categories. They can also register by filling in their personal
information on the website’s profile page. All the visitorsare welcome to drop a service review
and help the site admin to improve the service. The application has agood appearance with an easy,
clear and concise site navigation.

[Live Project Here](https://soilmate-plants-a1626f09724b.herokuapp.com/)

## Table Content

- [Soilmate Plants - Introduction](#soilmate-plants---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
    - [The Scope](#the-scope)
    - [Main Site Goals](#main-site-goals)
    - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Database Diagram](#database-diagram)
    - [Features](#features)
    - [Home Page](#home-page)
    - [Our Plants Page](#our-plants-page)
    - [Products Details](#products-details)
    - [Add Product](#add-product)
    - [Edit/ Delete Product](#edit-delete-product)
    - [Shopping Bag](#shopping-bag)
    - [Update Bag](#update-bag)
    - [Products Checkout](#products-checkout)
    - [Products Checkout - Success](#products-checkout---success)
    - [Service Reviews under the product](#service-reviews-under-the-product)
    - [Service Reviews Page](#service-reviews-page)
    - [Add/Edit Service Review Page](#addedit-service-review-page)
    - [Delete Review](#delete-review)
    - [Profile Page](#profile-page)
    - [About us](#about-us)
    - [Blog Page](#blog-page)
    - [Contact Page](#contact-page)
    - [More](#more)
    - [Signup Page - Verify Email](#signup-page---verify-email)
    - [Signup Page - Confirm Email](#signup-page---confirm-email)
    - [Login Page](#login-page)
    - [Logout Page](#logout-page)
    - [Reset Password Page](#reset-password-page)
    - [Change Password Page](#change-password-page)
    - [Page 404 - Page Not Found](#page-404---page-not-found)
    - [Messages and Interaction with Users](#messages-and-interaction-with-users)
    - [Navbar](#navbar)
    - [Navigation - User Not Logged In](#navigation---user-not-logged-in)
    - [Footer](#footer)
    - [Admin Panel / Superuser](#admin-panel--superuser)
    - [Marketing and Social Media](#marketing-and-social-media)
    - [Facebook Page](#facebook-page)
    - [Instagram](#instagram)
    - [Privacy Policy](#privacy-policy)
    - [Search Engine Optimization](#search-engine-optimization)
    - [AWS Setup Process](#aws-setup-process)
    - [AWS S3 Bucket](#aws-s3-bucket)
    - [Stripe Payments](#stripe-payments)
    - [Technologies Used](#technologies-used)
    - [Creating the Django app](#creating-the-django-app)
    - [Deployment of This Project](#deployment-of-this-project)
    - [Final Deployment](#final-deployment)
    - [Forking This Project](#forking-this-project)
    - [Cloning This Project](#cloning-this-project)
    - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
    - [Acknowledgements](#acknowledgements)


## User Experience - UX

### User Stories

- As a website user, I can:

1. Navigate around the website and easily find the desired content.
2. See a list of products and choose a desired product.
3. Search products and be able to find a specific product.
4. Click on a product to find more details about it.
5. Register for an account to be able to use the services offered to members.
6. View product comments so that I can read other users' opinions.
7. Buy a product by using the website checkout system.
8. I can find more information about products on a website blog.

- As a logged in website user, I can:

1. Leave my review on the website about the purchased product.
2. Delete my previous reviews.
3. Edit my previous reviews.
4. Save my data under my personal profile.
5. Update my profile details.
6. Log out of the website.
7. Buy a product using my personal profile, through the website checkout system.

- As a website Superuser, I can:

1. Create and publish a new product.
2. Create a draft of a new product so it can be finalized later.
3. Create a new user, products, and categories.
4. Delete users, products, categories, and reviews.
5. Approve user's reviews.
6. Change a user’s permissions on the website.
7. Create and upload new posts to be shown on the website.
   
### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://https://github.com/KamilaAzul/Soilmate-Plants/issues)

[Back to top](<#contents>)

### The Scope

### Main Site Goals

- To provide users with a good website experience with watches and clocks on display.
- To provide users with a visually pleasing website that is intuitive and easy to navigate.
- To provide a website with a clear purpose.
- To provide tools that allow users to search for products.
- To provide users with an easy and safe way to buy their products.

### Design

#### Colours

![Colours Palete](./assets/readme/extras/watches_clocks_color_palete.png)<br>

- Since the website is a shop that sells flowers, the colors refer to the theme. The colors are warm and inspired by nature, dominated mainly by various shades of green and white.The contrast is maintained so that the content is clearly visible and easy to find, and the website is pleasant to use.

### Typography

- The Lato font is used as the main font for the whole project. The Kaushan font is used to
display the website logo. Font-family: Josefin Slab was used to display product name on the product page.

### Imagery

- All the images on the website are . The product images are
uploaded by the admin panel. 

[Back to top](<#contents>)

### Database Diagram

![Database Diagrama]()<br>

### Features

### Home Page

* Hero image

- The photo is a greeting for the user. It allows the user to go to shopping sites using the "Shop now" button.

* Plants Quality

- This part of the website tells where the plants are imported from and briefly explains why the plants are of the best quality

* Repotting

- Informs the user that the replanting process is performed in the shop on-site and gives details of the process.

*Delivery

- Provides information about the delivery process, special packaging for flowers and what determines the speed of delivery.

*Newsletter

- The user has the option of subscribing to the newsletter to receive information about the latest promotions, sales, etc.

### Our Plants Page

- In this feature users, can see a selection of plants on sale. The sale items are chosen by the website admin. Adding a product to sale is completed through the admin panel or from the website front-end.<br>

[Back to top](<#contents>)

### Products Details

- This feature is at the top of the Product Details Page. Here users can see the plants image and plants
information such as price, category, care level, safty and rating. If the user is interested in the specific plant they can add the product to their shopping bag, and add product quantity. Also, the user can continue shoping by pressing the button "Keep Shopping".
They can see the review under the product information; when they are loged in they can leave their own review.

### Add Product

- If the user is a superuser it is possible to add a new product after clicking on Product Management.
The product can be added as well from the admin panel.

### Edit/ Delete Product 

- Both on the page with all products and on the page for each product, there are two buttons: edit and delete. superuser can edit or delete the product on the website or from the administration panel.

[Back to top](<#contents>)

### Shopping Bag

- Here, users can add products and quantities. Check the total price, and delivery costs and go 
to the secure checkout to finish the order. The user can also leave this page by pressing the button "Keep Shopping".<br>

### Update Bag
-The user can change the quantity od the products and remove unwanted products.

### Products Checkout

- On the checkout page, users will have to fill out the form and add the credit/debit card details to finish the purchase.<br>

### Products Checkout - Success

- Once the user have successfully purchased products, a confirmation message will appear and a confirmation email will be sent.

### Service Reviews under the product

-Uder the product, a user with a valid registration account and logged in can add or edit their own personal service reviews.<br>

### Service Reviews Page

- On this page, users can see all reviews left by website users. The page admin will first have to approve a review before it will appear on the website. <br>
 
### Add/Edit Service Review Page

- A user with a valid registration account and logged in can add or edit their own personal service reviews. The edit and delete buttons will appear only for the user who created a particular review.

### Delete Review

- User can delete unwanted review.

[Back to top](<#contents>)

### Profile Page

- On this page a logged in user (with a valid registration account) can add or edit their own personal details and also check previous orders.<br>

### About us

- On this page user can find more information about the company. This website was created so that the user could get to know the company better, feel more confident and safer when purchasing products on this website.
The user knows who he is talking to and who can help him if necessary.

* Company
  
- Short story of the company accompanied by a photo of the founder.

* OutTeam
  
- Three people working in the company are presented, a short description of each of them, a photo, and what tasks they deal with within the company.

* Gallery
  
- In this section, the user can see photos of employees at work, a photo of the store, and where all the plants come from.

### Blog Page

- On this page users can read all posts.
They will be posted regularly and users can expand their knowledge about the plants they purchase and how to care for them.

### Contact Page

- From this page, the user can send a form with a specific inquiry. After sending the message, he will be redirected to the "ThankYou" page with a thank you message and information that someone will contact him as soon as possible.

### More

* Customer Reviews
  
- On this page user can see all reviews written by users.
the six newest comments are displayed, at the bottom of the page there is a "Next" button that will redirect to the next page where the user can see older comments.

* Design Services
  
- On this page the user can find more information about the service the company offers.

* Newsletter
  
- Every user can sign up to receive a newsletter with useful information about promotions, sales, etc.

- On this page User must fill in the Signup form.<br>


### Signup Page - Verify Email


- After submitting the Signup form, the user will be redirected to this page, advising them to check the link sent to their email box.<br>

[Back to top](<#contents>)

### Signup Page - Confirm Email

- Once the user clicks on the link sent to their email box, it will redirect the user to this page which confirms their email.<br>

### Login Page

- On the Login Page, users can log in to the website by inputting their username and password. The user is now
registered and will have access to the Registered User website services.<br>

### Logout Page

- On the Logout Page, users can confirm that they want to exit the website.<br>
  
### Reset Password Page

- Users can use this page to reset their login password. The user adds their email address in the input field and clicks on the button "Reset Password".<br>

### Change Password Page

- Users will get a link to reset their password and after clicking on the link it will redirect the user to this page where they can set a new password.<br>

### Page 404 - Page Not Found

- The user will see this feature when the page that the user is looking for, does not exist or for any typing URL error.<br>  

[Back to top](<#contents>)

### Messages and Interaction with Users

- Some interactive messages are added to the project to make the navigation on the website easier and to improve the user's experience.

### Navbar

- The navigation bar includes the same basic options for the user (logged in or not logged in). 
  If the user is logged in as an administrator the sub-menus look different.
 
#### Navigation - User Not Logged In

**Home**- Lets the user find information about: **Plants Quality**, **Repotting**, **Delivery**, **Newsletter**.
**Our Plants** - Lets the user sort/view the products by **All Plants**, **Potted trees**, **Potted plants**, **Hanging Plants**, **For Beginners**, **Exotic** and **By Rating**,
**Special Offers** -Lets the user sort/view the products by the tags **new arrivals** and **product of the month** and **Sales**
**About us** - Lets the user find information about the company.
**Blog** - Lets the user see the posts about different subjects related to plant care.
**Contact** - Allows the user to send a message to the company with a specific inquiry
**More** - Allows the user to see **Customer Reviews** and **Desing Services**. Superuser can add **Newsletter** to send it to subscribed users. 
**Search Box** - Lets the user search for products on the page.
**My Account** - Lets the user either **register an account** or **login**
**Cart** - Views the total cost of the cart when the user starts adding to it. When the user clicks on it the **bag** template opens up.
**Search Box** - Lets the user search for products on the page.

**Navigation - User Logged In**

When user is logged in the **my account** gets more available options, **my profile**.

**My Profile** - On the profile page the user can change delivery information and see the order history (and confirmations from earlier purchases).

[Back to top](<#contents>)

### Footer

On the website footer, users can see basic information about the Soilmate Plants. The information includes contact, social media, blog, copyright, newsletter.<br>
 
### Admin Panel / Superuser

![Admin Panel / Superuser]

- On the Admin Panel and as an admin/superuser I have full access to CRUD functionality. This means I can view, create, edit and
  delete the following apps:

1. Blog
2. Checkout
3. Products
4. Profiles
5. Reviews
6. Subscribers

- As admin/superuser I can also approve reviews.<br>

### Marketing and Social Media

- Social Media marketing is a great tool to promote the company. Soilamate Plants has a presence on social media through the platforms Facebook and Instagram. It helps Soilmate Plant to communicate with both existing customers but also potential new ones. Through social media, its created engagement, and interaction with a customer. The plant's sale is being made on the site that's why it is very important to use social media platforms to increase the traffic to the website. <br>

* Marketing- emails

- E-mail marketing One form of reaching out to customers in an effective way is through e-mail marketing.Soilmate Plants gives a customers a possibility to sign up for a newsletter on the company site. The newsletter it's a good way to let to know what is happening at Soilmate Plants. The content can include advertisment for new blog posts, product of the month, sales, and discount codes.

* Facebook Page 

* Instagram

### Privacy Policy

- In order to add a page with the Soilmate Plants Privacy Policy I used the service [Privacy Policy Generator](https://www.privacypolicygenerator.info/) to ensure that the website is compliant with the European Privacy Policy Rules.<br> 

### Search Engine Optimization

* sitemap.xml

- A sitemap file with a list of important URLs was added to ensure that search engines are able to easily navigate through the site and understand its structure. This was made using XML-sitemaps.com by following the steps:

1. Paste the URL of the deployed site into XML-sitemaps
2. Download the XML sitemap file
3. Add the file into the projects root folder, named as sitemap.xml<br>

* robots.txt

- A robots.txt file was created to tell search engines where not to go on the website and increase the quality of the site, ultimately improving the SEO rating.

![Robots.txt]<br>

* Sitemap Google Registration
- To ensure that the Google engine will check the website sitemap file I have registered the Watches & Clocks URL on the Google Search Console.

![Sitemap Google Registration]<br>

[Back to top](<#contents>)

### AWS Setup Process

The deployed site uses AWS S3 Buckets to store the webpages static and media files. More information on how you can set up an AWS S3 Bucket can be found below:

1. Create an AWS account [here](https://portal.aws.amazon.com/).
2. Login to your account and within the search bar type in "S3".
3. Within the S3 page click on the button that says "Create Bucket".
4. Name the bucket and select the region which is closest to you.
5. Underneath "Object Ownership" select "ACLs enabled".
6. Uncheck "Block Public Access" and acknowledge that the bucket will be made public, then click "Create Bucket".
7. Inside the created bucket click on the "Properties" tab. Below "Static Website Hosting" click "Edit" and change the Static website hosting option to "Enabled". Copy the default values for the index and error documents and click "Save Changes".
8. Click on the "Permissions" tab, below "Cross-origin Resource Sharing (CORS)", click "Edit" and then paste in the following code:

  ```
    [
        {
            "AllowedHeaders": [
            "Authorization"
            ],
            "AllowedMethods": [
            "GET"
            ],
            "AllowedOrigins": [
            "*"
            ],
            "ExposeHeaders": []
        }
    ]
  ```

9. Within the "Bucket Policy" section. Click "Edit" and then "Policy Generator". Click the "Select Type of Policy" dropdown and select "S3 Bucket Policy" and within "Principle" allow all principals by typing "*".
10. Within the "Actions" dropdown menu select "Get Object" and in the previous tab copy the "Bucket ARN number". Paste this within the policy generator within the field labelled "Amazon Resource Name (ARN)".
11. Click "Add statement > Generate Policy" and copy the policy that's been generated and paste this into the "Bucket Policy Editor".
12. Before saving, add /* at the end of your "Resource Key", this will allow access to all resources within the bucket.
13. Once saved, scroll down to the "Access Control List (ACL)" and click "Edit".
14. Next to "Everyone (public access)", check the "list" checkbox and save your changes.

### AWS S3 Bucket

* IAM Set Up

1. Search for IAM within the AWS navigation bar and select it.
2. Click "User Groups" that can be seen in the side bar and then click "Create group" and name the group 'manage-your-project-name'.
3. Click "Policies" and then "Create policy".
4. Navigate to the JSON tab and click "Import Managed Policy", within here search "S3" and select "AmazonS3FullAccess" followed by "Import".
5. Navigate back to the recently created S3 bucket and copy your "ARN Number". Go back to "This Policy" and update the "Resource Key" to include your ARN Number, and another line with your ARN followed by a "/*".
   
- Below is an example of what this should look like:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

```

1. Ensure the policy has been given a name and a short description, then click "Create Policy".
2. Click "User groups", and then the group you created earlier. Under permissions click "Add Permission" and from the dropdown click "Attach Policies".
3. Select "Users" from the sidebar and click "Add User".
4. Provide a username and check "Programmatic Access", then click 'Next: Permissions'.
5. Ensure your policy is selected and navigate through until you click "Add User".
6. Download the "CSV file", which contains the user's access key and secret access key.

* Connecting AWS to the Project

1. Within your terminal install the following packages by typing 

```
  pip3 install boto3
  pip3 install django-storages 
```  

2. Freeze the requirements by typing:

```
pip3 freeze > requirements.txt
```

3. Add "storages" to your installed apps within your settings.py file.
4. At the bottom of the settings.py file add the following code:

```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'insert-bucket-name-here'
    AWS_S3_REGION_NAME = 'insert-your-region-here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
```
5. Add the following keys within Heroku: "AWS_ACCESS_KEY_ID" and "AWS_SECRET_ACCESS_KEY". These can be found in your CSV file.
6. Add the key "USE_AWS", and set the value to True within Heroku.
6. Remove the "DISABLE_COLLECTSTAIC" variable from Heroku.
7. Within your settings.py file inside the code just written add: 

```
  AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
```
8. Inside the settings.py file inside the bucket config if statement add the following lines of code:

```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
```

9. In the root directory of your project create a file called "custom_storages.py". Import the following at the top of this file and add the classes below:

```
  from django.conf import settings
  from storages.backends.s3boto3 import S3Boto3Storage

  class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

  class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

10. Navigate back to you AWS S3 Bucket and click on "Create Folder" name this folder "media", within the media file click "Upload > Add Files" and select the images for your site.
11. Under "Permissions" select the option "Grant public-read access" and click "Upload".

### Stripe Payments

* Payments 
- To set up stripe payments you can follow their guid [here](https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details)

* Webhooks

1. To set up a webhook, sign into your stripe account and click 'Developers' located in the top right of the navbar.
2. Then in the side-nav under the Developers title, click on "Webhooks", then "Add endpoint".
3. On the next page you will need to input the link to your heroku app followed by /checkout/wh/. It should look something like this:
   
    ```
    https://your-app-name.herokuapp.com/checkout/wh/
    ```

4. Then click "+ Select events" and check the "Select all events" checkbox at the top before clicking "Add events" at the bottom. Once this is done finish the form by clicking "Add endpoint".
5. Your webhook is now created and you should see that it has generated a secret key. You will need this to add to your heroku config vars.
6. Head over to your app in heroku and navigate to the config vars section under settings. You will need the secret key you just generated for your webhook, in addition to your Publishable key and secret key that you can find in the API keys section back in stripe.
7. Add these values under these keys:
   
    ```
    STRIPE_PUBLIC_KEY = 'insert your stripe publishable key'
    STRIPE_SECRET_KEY = 'insert your secret key'
    STRIPE_WH_SECRET = 'insert your webhooks secret key'

    ```
8. Finally, back in your settings.py file in django, insert the following near the bottom of the file:  
    ```
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```
- Below is a screenshot of the Watches & Clocks - Stripe dashboard.

![ Stripe Payments]<br>
[Back to top](<#contents>)
## Technologies Used

### Languages Used

- [HTML 5](https://en.wikipedia.org/wiki/HTML/)
- [CSS 3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://www.javascript.com/)
- [Django](https://www.python.org/)
- [Python](https://www.djangoproject.com/)<br>


### Django Packages

- [Gunicorn](https://gunicorn.org/) as the server for Heroku
- [Dj_database_url](https://pypi.org/project/dj-database-url/) to parse the database URL from the environment variables in Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) as an adaptor for Python and PostgreSQL databases
- [Summernote](https://summernote.org/) as a text editor
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) for authentication, registration and account 
   management
- [Stripe](https://pypi.org/project/stripe/) for processing all online and credit card purchases on the website
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style the forms
- [Pillow](https://pypi.org/project/Pillow/) to process and save all the images downloaded through the database<br>

[Back to top](<#contents>)

### Frameworks - Libraries - Programs Used

- [Bootstrap](https://getbootstrap.com/)
- Was used to style the website, add responsiveness and interactivity
- [Jquery](https://jquery.com/)
- All the scripts were written using jquery library
- [Git](https://git-scm.com/)
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
- [GitHub](https://github.com/)
- GitHub is used to store the project's code after being pushed from Git
- [Heroku](https://id.heroku.com)
- Heroku was used to deploy the live project
- [PostgreSQL](https://www.postgresql.org/)
- Database used through Heroku.
- [codeanyapp.com](https://codeanyapp.com/)
- Codeanyapp was used to create and edit the website
- [AWS](https://aws.amazon.com/)
- was used to host the static files and media<br>
- [Lucidchart](https://lucid.app/)
- Lucidchart was used to create the database diagram
- [Pycodestyle](http://pep8online.com/)
- Pycodestyle was used to validate all the Python code
- [W3C - HTML](https://validator.w3.org/)
- W3C- HTML was used to validate all the HTML code
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)
- W3C - CSS was used to validate the CSS code
- [Fontawesome](https://fontawesome.com/)
- Was used to add icons to the website
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- To check App responsiveness and debugging
- [Google Fonts](https://fonts.google.com/)
- To add the 2 fonts that were used throughout the project
- [CANVA](https://www.canva.com/)
- To build the logos for the project

### Testing

Testing results [here](TESTING.md)

[Back to top](<#contents>)

### Creating the Django app

1. Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
2. Click on Use This Template
3. Once the template is available in your repository click on Gitpod
4. When the image for the template and the Gitpod are ready open a new terminal to start a new Django App
5. Install Django and gunicorn: pip3 install django gunicorn
6. Install supporting database libraries dj_database_url and psycopg2 library: pip3 install dj_database_url psycopg2
7. Create file for requirements: in the terminal window type pip freeze --local > requirements.txt
8. Create project: in the terminal window type django-admin startproject your_project_name
9. Create app: in the terminal window type python3 manage.py startapp your_app_name
10. Add app to the list of installed apps in settings.py file: you_app_name
11. Migrate changes: in the terminal window type python3 manage.py migrate
12. Run the server to test if the app is installed, in the terminal "The install worked successfully! Congratulations!"<br>

### Deployment of This Project

- This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New
   App
3. You must enter a unique app name
4. Next select your region
5. Click on the Create App button
6. Click in resources and select Heroku Postgres database
7. Click Reveal Config Vars and add:
 * A new record with SECRET_KEY
 * A new record with the AWS_ACCESS_KEY_ID
 * A new record with the AWS_SECRET_ACCESS_KEY
 * A new record with the EMAIL_HOST_PASS
 * A new record with the EMAIL_HOST_USER 
 * A new record with the STRIPE_PUBLIC_KEY
 * A new record with the STRIPE_SECRET_KEY
 * A new record with the STRIPE_WH_SECRET
 * A new record with the DISABLE_COLLECTSTATIC = 1
8.  The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
9.  Next, scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
10. Scroll to the top of the page and choose the Deploy tab
11. Select Github as the deployment method
15. Confirm you want to connect to GitHub
16. Search for the repository name and click the connect button
17. Scroll to the bottom of the deploy page and select the preferred deployment type
18. Click Enable Automatic Deploys for automatic deployment when you push updates to Github<br>

## Final Deployment

1. Create a runtime.txt "python-3.9.13"
2. Create a Procfile "web: gunicorn your_project_name.wsgi"
3. When development is complete change the debug setting to: DEBUG = False in settings.py
4. In this project the summernote editor was used so for this to work in Heroku add: X_FRAME_OPTIONS = 'SAMEORIGIN' to
   settings.py.
5. In Heroku settings config vars delete the record for DISABLE_COLLECTSTATIC
6. In Heroku settings config vars set the record for USE_AWS to True<br>

### Forking This Project

To make an independent copy of a repository on Github you can fork the GitHub account. You can then be viewed and it is also possible to do changes in the copy without affecting the original repository. To fork the repository, take these steps:

1. After logging in to GitHub, locate the repository. On the top right side of the page there is a 'Fork' button. Click on the button to create a copy of the original repository.

<details><summary><b>Github Fork</b></summary>

[Back to top](<#contents>)

### Cloning This Project

To clone and set up this project you need to follow the steps below.

1. When you are in the repository, find the code tab and click it.
2. To the left of the green GitPod button, press the 'code' menu. There you will find a link to the repository. Click on the clipboard icon to copy the URL.
3. Use an IDE and open Git Bash. Change directory to the location where you want the cloned directory to be made.
4. Type 'git clone', and then paste the URL that you copied from GitHub. Press enter and a local clone will be created.

<details><summary><b>Github Create Local Clone</b></summary>

## Credits

### Content

- The images were taken from [Freepik](https://www.freepik.com/),
  [Pixabay](https://pixabay.com/),[Pexels](https://www.pexels.com//) 
- The Soilmate Plants logos and favicon are my own designed and build in [CANVA](https://www.canva.com/)
* [Code Institute - Boutique Ado Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

### Information Sources / Resources

- [W3Schools - Python](https://www.w3schools.com/python/)
- [Stack Overflow](https://stackoverflow.com/)
- [Scrimba - Pyhton](https://scrimba.com/learn/python)
- [Mdbootstrap](https://mdbootstrap.com/freebies/)
- [Startbootstrap](https://startbootstrap.com/)
- [Code Institute - Slack Community](https://slack.com/)

[Back to top](<#contents>)

### Acknowledgements

The website was completed as a Portfolio Project 5 made for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/).
I would like to thank my mentor Precious_Mentor for guiding me, and all at the Code Institute for their help and support.
