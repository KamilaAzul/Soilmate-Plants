# Soilmate Plants - Introduction

Project milestone 5 for Code Institute Full-stack development program: Django Framework.<br>
Soilamate Plants is an E-commerce shop where users can find and buy plants and search for
products by filtering different categories. They can also register by filling in their personal
information on the website’s profile page. All the visitorsare welcome to drop a service review
and help the site admin to improve the service. The application has agood appearance with an easy,
clear and concise site navigation.

[Live Project Here](https://)

README Table Content

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
- [Hero image](#hero-image)
- [Plants Quality](#plants-quality)
- [Repotting](#repotting)
- [Delivery](#delivery)
- [Newsletter](#newsletter)
- [Our Plants Page](#our-plants-page)
- [Products Details](#products-details)
- [Add Product](#add-product)
- [Edit Product](#edit-product)
- [Delete Product](#delete-product)
- [Shopping Bag](#shopping-bag)
- [Update Bag](#update-bag)
- [Products Checkout](#products-checkout)
- [Products Checkout - Success](#products-checkout---success)
  - [Service Reviews under the product](#service-reviews-under-the-product)
- [Service Reviews Page](#service-reviews-page)
- [Add/Edit Service Review Page](#addedit-service-review-page)
- [Delete Review](#delete-review)
- [Profile Page](#profile-page)
- [Profile Update](#profile-update)
- [About us](#about-us)
- [Signup Page](#signup-page)
- [Login Page](#login-page)
- [Logout Page](#logout-page)
- [Reset Password Page](#reset-password-page)
- [Change Password Page](#change-password-page)
- [Page 404 - Page Not Found](#page-404---page-not-found)
- [Messages and Interaction with Users](#messages-and-interaction-with-users)
    - [Navbar](#navbar)
    - [Footer](#footer)

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
[here](https://github.com/PedroCristo/portfolio_project_5/issues)

### The Scope

#### Main Site Goals

- To provide users with a good website experience with watches and clocks on display.
- To provide users with a visually pleasing website that is intuitive and easy to navigate.
- To provide a website with a clear purpose.
- To provide tools that allow users to search for products.
- To provide users with an easy and safe way to buy their products.

## Design

#### Colours

![Colours Palete](./assets/readme/extras/watches_clocks_color_palete.png)<br>

- Since the website is a shop that sells flowers, the colors refer to the theme. The colors are warm and inspired by nature, dominated mainly by various shades of green and white.The contrast is maintained so that the content is clearly visible and easy to find, and the website is pleasant to use.

#### Typography

- The Lato font is used as the main font for the whole project. The Kaushan font is used to
display the website logo. Font-family: Josefin Slab was used to display product name on the product page.

#### Imagery

- All the images were converted to webp format to improve the website performance. The product images are
uploaded by the admin panel. 

## Database Diagram

![Database Diagrama]()<br>

## Features

## Home Page

# Hero image
# Plants Quality
# Repotting
# Delivery
# Newsletter
# Our Plants Page

- In this feature users, can see a selection of plants on sale. The sale items are chosen by the website admin. Adding a product to sale is completed through the admin panel or from the website front-end.<br>
  
# Products Details
# Add Product
# Edit Product 
# Delete Product 
# Shopping Bag

- Here, users can add products and quantities. Check the total price, and delivery costs and go 
to the secure checkout to finish the order. The user can also leave this page by pressing the button "Keep Shopping".<br>

# Update Bag
-The user can change the quantity od the products and remove unwanted products.

# Products Checkout

-- On the checkout page, users will have to fill out the form and add the credit/debit card details to finish the purchase.<br>

# Products Checkout - Success

- Once the user have successfully purchased products, a confirmation message will appear and a confirmation email will be sent.

## Service Reviews under the product

The user can leave a review under the purchased flower.

# Service Reviews Page

- On this feature, users can see all reviews left by website users. The page admin will first have to approve a review before it will appear on the website.<br>
- 
# Add/Edit Service Review Page

 The edit and delete buttons will appear if the user created a particular review.

# Delete Review

Usen can delete unwanted review.

# Profile Page

# Profile Update
# About us
Company
Out Team
Gallery
Blog Page
Contact Page
More
Customer Reviews
Design Services
Newsletter
# Signup Page
# Login Page
# Logout Page
# Reset Password Page
# Change Password Page
# Page 404 - Page Not Found
# Messages and Interaction with Users

### Navbar
  The navigation bar includes the same basic options for the user (logged in or not logged in). 
  If the user is logged in as an administrator the sub-menus look different.
 
**Navigation - User Not Logged In**

* **Home**- Lets the user find information about: **Plants Quality**, **Repotting**, **Delivery**, **Newsletter**.
* **Our Plants** - Lets the user sort/view the products by **All Plants**, **Potted trees**, **Potted plants**, **Hanging Plants**, **For Beginners**, **Exotic** and **By Rating**,
* **Special Offers** -Lets the user sort/view the products by the tags **new arrivals** and **product of the month** and **Sales**
* **About us** - Lets the user find information about the company.
* **Blog** - Lets the user see the posts about different subjects related to plant care.
* **Contact** - Allows the user to send a message to the company with a specific inquiry
* **More** - Allows the user to see **Customer Reviews** and **Desing Services**. Superuser can add **Newsletter** to send it to subscribed users. 
* **Search Box** - Lets the user search for products on the page.
* **My Account** - Lets the user either **register an account** or **login**
* **Cart** - Views the total cost of the cart when the user starts adding to it. When the user clicks on it the **bag** template opens up.
* **Search Box** - Lets the user search for products on the page.

**Navigation - User Logged In**

When user is logged in the **my account** gets more available options, **my profile** and **my wishlist**.

* **My Profile** - On the profile page the user can change delivery information and see the order history (and confirmations from earlier purchases)
* **My Wishlist** - On the wishlist page the user can find their wishlist that is populated when the user adds items to the wishlist from the product detail area. From this view the user also can remove products from the wishlist.

### Footer

On the website footer, users can see basic information about the Soilmate Plants. The information includes contact, social media, blog, copyright, newsletter.<br>
