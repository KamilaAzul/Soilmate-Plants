# Testing

Back to the [README](README.md)

## Testing User Stories

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

[Back to top](<#table-of-content>)

## Code Validation
The code on the Soilmate Plants site has been tested through W3C Markup Validation Service, W3C CSS Validation Service, CI Python Linter and JSHint.

### Markup Validation
 Errors were at first found on the site in the W3C Markup Validation Service but could quite easily be fixed (see bugs section). After fixing the inital errors that W3C Markup Validation Service reported, no errors were returned except 1 connected to a form on the profile page (more information about that in the bugs section).

<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](readme/assets/images/html_validation_no_error.png)
</details><br/>

[Back to top](<#table-of-content>)

### CSS Validation
When validating my own code the W3C CSS Validator reports no errors but 16 errors connected to Bootstrap were reported.

<details><summary><b>CSS Validation Result</b></summary>

**Main CSS**
![CSS Result - Main](readme/assets/images/css_validator_main.png)

**Profile CSS**
![CSS Result - Profile](readme/assets/images/css_validator_profile.png)

**Checkout CSS**
![CSS Result - Checkout](readme/assets/images/css_validator_checkout.png)

</details><br/>

[Back to top](<#table-of-content>)

### PEP Validation
CI Python Linter [Code Institute Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code in the project. Following files have been validated:

**App Bag**
* admin.py -  No errors reported
* apps.py -  No errors or warnings reported
* contexts.py -  No errors or warnings reported
* urls.py -  No errors or warnings reported
* views.py -  No errors or warnings reported
* bag_tools.py - No errors or warnings reported

**App Blog**
* admin.py - No errors reported
* apps.py - No errors reported
* forms.py - No errors reported
* models.py - No errors reported
* urls.py - No errors reported
* views.py - No errors reported

**App Checkout**
* __init__.py - No errors reported
* admin.py - No errors reported
* apps.py - No errors reported
* forms.py - No errors reported
* models.py - No errors reported
* signals.py - No errors reported
* urls.py - No errors reported
* views.py - No errors reported
* webhook_handler.py - 2 line-too-long errors reported which I was not able to fix before sending in the project for assessment
* webhooks.py - 1 line-too-long errors reported which I was not able to fix before sending in the project for assessment

**App Home**
* apps.py - No errors reported
* urls.py - No errors reported
* views.py - No errors reported

**App Products**
* admin.py - No errors reported
* apps.py - No errors reported
* forms.py - No errors reported
* models.py - No errors reported
* urls.py - No errors reported
* views.py - No errors reported

**App Profiles**
* apps.py - No errors reported
* forms.py - No errors reported
* models.py - No errors reported
* urls.py - No errors reported
* views.py - No errors reported

**kollektiv_fem**
* urls.py - No errors reported
* views.py - No errors reported

**other**
* custom_storages.py - No errors reported

[Back to top](<#table-of-content>)

### JavaScript Validation
The [JSHint](https://jshint.com/) validator results can be seen below:

No errors were returned when passing through JSHint but the test with no errors.

* stripe_elements.js in checkout app - No errors reported
* inline jscript in bag.html in bag app - No errors reported
* inline jscript in products.html in products app - No errors reported
* inline jscript in base.html in root templates - No errors reported
* inline jscript in footer.html in root templates - No errors reported

[Back to top](<#table-of-content>)

## Additional Testing

### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below the list of tests that has been conducted can be found.

| Status | **Main Website - User Logged Out - Navigation**
|:-------:|:--------|
| &check; | The free shipping treshold changes in the top bar changes when changing the treshold in the settings file
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication opens the sing in page or views a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and views the carousel and blog posts
| &check; | Clicking the By Added Date link in the Products menu lists all products and sorts them by added date.
| &check; | Clicking the By Price link in the Products menu lists all products and sorts them by price.
| &check; | Clicking the By Rating link in the Products menu lists all products and sorts them by rating.
| &check; | Clicking the By Name link in the Products menu lists all products and sorts them by name.
| &check; | Clicking the All Products link in the Products menu lists all products.
| &check; | Clicking the Tapes link in the Categories menu lists all products within the category tape
| &check; | Clicking the CDS link in the Categories menu lists all products within the category cds
| &check; | Clicking the Posters link in the Categories menu lists all products within the category posters
| &check; | Clicking the Pins link in the Categories menu lists all products within the category pins
| &check; | Clicking the T-shirts link in the Categories menu lists all products within the category t-shirts
| &check; | Clicking the Tank Tops link in the Categories menu lists all products within the category tank tops
| &check; | Clicking the Tote Bags link in the Categories menu lists all products within the category tote bags
| &check; | Clicking the Vinyls link in the Categories menu lists all products within the category vinyls
| &check; | Clicking the New Arrivals link in the Special Offers menu lists all products with the tag new arrivals
| &check; | Clicking the Product Of The Month link in the Special Offers menu lists all products with the tag product of the month
| &check; | Clicking the Register link in the My Account menu loads the sign up page
| &check; | Clicking the Login link in the My Account menu loads the loginpage
| &check; | Clicking on the cart link in the menu bar loads the shopping bag page
| &check; | Input an empty query in the search box triggers an error messages and lists all products
| &check; | Input a valid query in the search box lists the correct products

| Status | **Main Website - User Logged Out - Carousel**
|:-------:|:--------|
| &check; | 2 images are being looped in the carousel
| &check; | On image 1 the call to action button 'Start Shopping' loads the product page and lists all products.
| &check; | On image 2 the call to action button 'Subscrib' takes the site user to the footer.
| &check; | The navigation options in the carousel is working (left / right and bottom navigation)

| Status | **Main Website - User Logged Out - Blog**
|:-------:|:--------|
| &check; | The 3 latest blog posts are rendered for the user on the home page
| &check; | Clicking the View All Blog Posts button loads the View All Blog Posts page
| &check; | The correct image and information for each blog post is being shown.
| &check; | Clicking the Read More button on a blog post card loads the blog detail page
| &check; | Clicking the Tag on the blog post card loads the blog posts with the same tags
| &check; | Clicking the Back To Home button on the blog detail page loads the home page

| Status | **Main Website - User Logged Out - Blog - View All Blog Posts**
|:-------:|:--------|
| &check; | 9 Products are rendered for the user on the product pages before pagination is activated
| &check; | Clicking the Read More button on a blog post card loads the blog detail page
| &check; | When clicking on the pagination previous / next buttons the previous / next 9 posts are being rendered
| &check; | When clicking on the pagination first / last buttons the first / last 9 posts are being rendered
dered
| &check; | When clicking on the category link all the blog posts with that category is being shown and the pagination takes the categories into consideration.
| &check; | Clicking the Back To Home button on the blog detail page loads the home page

| Status | **Main Website - User Logged Out - Products**
|:-------:|:--------|
| &check; | When using the sorting function below the product page headline the products are being sorted accordingly.
| &check; | 9 Products are rendered for the user on the product pages before pagination is activated
| &check; | When clicking on the pagination previous / next buttons the previous / next 9 products are being rendered
| &check; | When clicking on the pagination first / last buttons the first / last 9 products are being rendered
| &check; | Clicking the Read More button on a product loads the product detail page
| &check; | Clicking the Tag on the product card / product detail loads the products with the same tags
| &check; | Clicking the Category on the product card / product detail loads the products with the same category
| &check; | The correct image and information for each product is being shown
| &check; | When adding products to the cart the total updates correctly to the right of the cart symbol in the menu.
| &check; | Clicking the Keep Shopping button on the product detail page lists all products
| &check; | Clicking the Add To Bag button on the product detail page adds the quantity and size to the shopping bag and shows a flash message with the bag content and totals in the top right together (with a working link to the shopping bag)
| &check; | Clicking the Add To Wishlist button on the product detail page opens the sign-in page because wishlists only works for logged in users
| &check; | It's possible to change the quantity on the product detail page
| &check; | If the product has sizes a size dropdown is visible on the product detail page
| &check; | When clicking on the product image on the product detail page a modal opens with the image

| Status | **Main Website - User Logged Out - Shopping Bag**
|:-------:|:--------|
| &check; | The correct products and information are showing in the shopping bag (including correct sizes when product has size)
| &check; | When changing the quantity and click update the quantity updates
| &check; | When clicking the remove link the product is being removed from the shopping bag
| &check; | Clicking the Keep Shopping button on the product detail page lists all products
| &check; | Clicking the Secure Checkout button on the product detail page loads the secure checkout page

| Status | **Main Website - User Logged Out - Checkout**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order summary (including correct sizes when product has size)
| &#10008; | The form validation is working except that the Full Name field can include numbers and the phone number field can include text
| &check; | In the bottom of the form an option log in or sign up is visible
| &check; | When clicking the Adjust Bag Button the Shopping Bag page loads
| &check; | The payment with card number is working correctly (tested with Stripe test numbers)
| &check; | The payment with card number that needs to be authenticated is working correctly (tested with Stripe test numbers). The authentication window is visible.

| Status | **Main Website - User Logged Out - Order Confirmation Page**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order confirmation and an e-mail has been sent to the registered site user e-mail
| &check; | Webhooks are working and is confirmed in Stripe developer dashboard
| &check; | When clicking the Back To The Store button all products are being listed

| Status | **Main Website - User Logged Out - Footer**
|:-------:|:--------|
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Register a valid e-mail address in the e-mail signup in the footer is working
| &check; | Register a non-valid e-mail address in the e-mail signup in the footer triggers an error message
| &check; | Register a non-valid e-mail address in the e-mail signup in the footer triggers an error message
| &check; | Clicking the Kollektiv Fem link in the footer area opens the Kollektiv Fem site in a new window
| &check; | Clicking the Privacy Policy link in the footer area opens loads the privacy policy page
| &check; | Clicking the FAQ link in the footer area opens loads the FAQ page

[Back to top](<#table-of-content>)

| Status | **Main Website - User Logged In - Navigation**
|:-------:|:--------|
| &check; | The free shipping treshold changes in the top bar changes when changing the treshold in the settings file
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication opens the sing in page or views a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and views the carousel and blog posts
| &check; | Clicking the By Added Date link in the Products menu lists all products and sorts them by added date.
| &check; | Clicking the By Price link in the Products menu lists all products and sorts them by price.
| &check; | Clicking the By Rating link in the Products menu lists all products and sorts them by rating.
| &check; | Clicking the By Name link in the Products menu lists all products and sorts them by name.
| &check; | Clicking the All Products link in the Products menu lists all products.
| &check; | Clicking the Tapes link in the Categories menu lists all products within the category tape
| &check; | Clicking the CDS link in the Categories menu lists all products within the category cds
| &check; | Clicking the Posters link in the Categories menu lists all products within the category posters
| &check; | Clicking the Pins link in the Categories menu lists all products within the category pins
| &check; | Clicking the T-shirts link in the Categories menu lists all products within the category t-shirts
| &check; | Clicking the Tank Tops link in the Categories menu lists all products within the category tank tops
| &check; | Clicking the Tote Bags link in the Categories menu lists all products within the category tote bags
| &check; | Clicking the Vinyls link in the Categories menu lists all products within the category vinyls
| &check; | Clicking the New Arrivals link in the Special Offers menu lists all products with the tag new arrivals
| &check; | Clicking the Product Of The Month link in the Special Offers menu lists all products with the tag product of the month
| &check; | Clicking the My Profile link the My Account menu loads the my profile page
| &check; | Clicking the My Wishlist link in the My Account menu loads the wishlist page
| &check; | Clicking on the cart link in the menu bar loads the shopping bag page
| &check; | Input an empty query in the search box triggers an error messages and lists all products
| &check; | Input a valid query in the search box lists the correct products

| Status | **Main Website - User Logged In - Carousel**
|:-------:|:--------|
| &check; | 2 images are being looped in the carousel
| &check; | On image 1 the call to action button 'Start Shopping' loads the product page and lists all products.
| &check; | On image 2 the call to action button 'Subscrib' takes the site user to the footer.
| &check; | The navigation options in the carousel is working (left / right and bottom navigation)

| Status | **Main Website - User Logged In - Blog**
|:-------:|:--------|
| &check; | The 3 latest blog posts are rendered for the user on the home page
| &check; | Clicking the View All Blog Posts button loads the View All Blog Posts page
| &check; | The correct image and information for each blog post is being shown.
| &check; | Clicking the Read More button on a blog post card loads the blog detail page
| &check; | Clicking the Tag on the blog post card loads the blog posts with the same tags
| &check; | Clicking the Back To Home button on the blog detail page loads the home page

| Status | **Main Website - User Logged In - Blog - View All Blog Posts**
|:-------:|:--------|
| &check; | 9 Products are rendered for the user on the product pages before pagination is activated
| &check; | Clicking the Read More button on a blog post card loads the blog detail page
| &check; | When clicking on the pagination previous / next buttons the previous / next 9 posts are being rendered
| &check; | When clicking on the pagination first / last buttons the first / last 9 posts are being rendered
dered
| &check; | When clicking on the category link all the blog posts with that category is being shown and the pagination takes the categories into consideration.
| &check; | Clicking the Back To Home button on the blog detail page loads the home page

| Status | **Main Website - User Logged In - Products**
|:-------:|:--------|
| &check; | When using the sorting function below the product page headline the products are being sorted accordingly.
| &check; | 9 Products are rendered for the user on the product pages before pagination is activated
| &check; | When clicking on the pagination previous / next buttons the previous / next 9 products are being rendered
| &check; | When clicking on the pagination first / last buttons the first / last 9 products are being rendered
| &check; | Clicking the Read More button on a product loads the product detail page
| &check; | Clicking the Tag on the product card / product detailloads the products with the same tags
| &check; | Clicking the Category on the product card / product detail loads the products with the same category
| &check; | The correct image and information for each product is being shown
| &check; | When adding products to the cart the total updates correctly to the right of the cart symbol in the menu.
| &check; | Clicking the Keep Shopping button on the product detail page lists all products
| &check; | Clicking the Add To Bag button on the product detail page adds the quantity and size to the shopping bag and shows a flash message with the bag content and totals in the top right together (with a working link to the shopping bag)
| &check; | Clicking the Add To Wishlist button on the product detail page adds the product to the users wishlist and changes the button to 'In Your Wishlist'
| &check; | It's possible to change the quantity on the product detail page
| &check; | If the product has sizes a size dropdown is visible on the product detail page
| &check; | When clicking on the product image on the product detail page a modal opens with the image

| Status | **Main Website - User Logged In - Shopping Bag**
|:-------:|:--------|
| &check; | The correct products and information are showing in the shopping bag (including correct sizes when product has size)
| &check; | When changing the quantity and click update the quantity updates
| &check; | When clicking the remove link the product is being removed from the shopping bag
| &check; | Clicking the Keep Shopping button on the product detail page lists all products
| &check; | Clicking the Secure Checkout button on the product detail page loads the secure checkout page

| Status | **Main Website - User Logged In - Checkout**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order summary (including correct sizes when product has size)
| &check; | It the user has updated the profile information the information is prefilled in the form.
| &check; | In the bottom of the form an option to save the delivery inforation to the users profile is visible
| &#10008; | The form validation is working except that the Full Name field can include numbers and the phone number field can include text.
| &check; | When clicking the Adjust Bag Button the Shopping Bag page loads
| &check; | The payment with card number is working correctly (tested with Stripe test numbers)
| &check; | The payment with card number that needs to be authenticated is working correctly (tested with Stripe test numbers). The authentication window is visible.

| Status | **Main Website - User Logged In - Order Confirmation Page**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order confirmation and an e-mail has been sent to the registered site user e-mail
| &check; | Webhooks are working and is confirmed in Stripe developer dashboard
| &check; | When clicking the Back To The Store button all products are being listed

| Status | **Main Website - User Logged In - Footer**
|:-------:|:--------|
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Register a valid e-mail address in the e-mail signup in the footer is working
| &check; | Register a non-valid e-mail address in the e-mail signup in the footer triggers an error message
| &check; | Register a non-valid e-mail address in the e-mail signup in the footer triggers an error message
| &check; | Clicking the Kollektiv Fem link in the footer area opens the Kollektiv Fem site in a new window
| &check; | Clicking the Privacy Policy link in the footer area opens loads the privacy policy page
| &check; | Clicking the FAQ link in the footer area opens loads the FAQ page

[Back to top](<#table-of-content>)

| Status | **Main Website - Admin Logged In - Navigation**
|:-------:|:--------|
| &check; | The free shipping treshold changes in the top bar changes when changing the treshold in the settings file
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that needs authentication opens the sing in page or views a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page and views the carousel and blog posts
| &check; | Clicking the By Added Date link in the Products menu lists all products and sorts them by added date.
| &check; | Clicking the By Price link in the Products menu lists all products and sorts them by price.
| &check; | Clicking the By Rating link in the Products menu lists all products and sorts them by rating.
| &check; | Clicking the By Name link in the Products menu lists all products and sorts them by name.
| &check; | Clicking the All Products link in the Products menu lists all products.
| &check; | Clicking the Tapes link in the Categories menu lists all products within the category tape
| &check; | Clicking the CDS link in the Categories menu lists all products within the category cds
| &check; | Clicking the Posters link in the Categories menu lists all products within the category posters
| &check; | Clicking the Pins link in the Categories menu lists all products within the category pins
| &check; | Clicking the T-shirts link in the Categories menu lists all products within the category t-shirts
| &check; | Clicking the Tank Tops link in the Categories menu lists all products within the category tank tops
| &check; | Clicking the Tote Bags link in the Categories menu lists all products within the category tote bags
| &check; | Clicking the Vinyls link in the Categories menu lists all products within the category vinyls
| &check; | Clicking the New Arrivals link in the Special Offers menu lists all products with the tag new arrivals
| &check; | Clicking the Product Of The Month link in the Special Offers menu lists all products with the tag product of the month
| &check; | Clicking the My Profile link the My Account menu loads the my profile page
| &check; | Clicking the My Wishlist link in the My Account menu loads the wishlist page
| &check; | Clicking the My Manage Products link the My Account menu loads the my product management page
| &check; | Clicking the Manage Blog link in the My Account menu loads the blog management page
| &check; | Clicking on the cart link in the menu bar loads the shopping bag page
| &check; | Input an empty query in the search box triggers an error messages and lists all products
| &check; | Input a valid query in the search box lists the correct products

| Status | **Main Website - Admin Logged In - Carousel**
|:-------:|:--------|
| &check; | 2 images are being looped in the carousel
| &check; | On image 1 the call to action button 'Start Shopping' loads the product page and lists all products.
| &check; | On image 2 the call to action button 'Subscrib' takes the site user to the footer.
| &check; | The navigation options in the carousel is working (left / right and bottom navigation)

| Status | **Main Website - Admin Logged In - Blog**
|:-------:|:--------|
| &check; | The 3 latest blog posts are rendered for the user on the home page
| &check; | Clicking the View All Blog Posts button loads the View All Blog Posts page
| &check; | The correct image and information for each blog post is being shown.
| &check; | Clicking the Read More button on a blog post card loads the blog detail page
| &check; | Clicking the Tag on the blog post card loads the blog posts with the same tags
| &check; | Clicking the Back To Home button on the blog detail page loads the home page
| &check; | When clicking the Edit button to the right of the Read More button below the blog post the blog management edit page is loaded

| Status | **Main Website - Admin Logged In - Blog - View All Blog Posts**
|:-------:|:--------|
| &check; | 9 Products are rendered for the user on the product pages before pagination is activated
| &check; | Clicking the Read More button on a blog post card loads the blog detail page
| &check; | When clicking on the pagination previous / next buttons the previous / next 9 posts are being rendered
| &check; | When clicking on the pagination first / last buttons the first / last 9 posts are being rendered
dered
| &check; | When clicking on the category link all the blog posts with that category is being shown and the pagination takes the categories into consideration.
| &check; | Clicking the Back To Home button on the blog detail page loads the home page
| &check; | When clicking the Edit button to the right of the Read More button below the blog post the blog management edit page is loaded

| Status | **Main Website - Admin Logged In - Products**
|:-------:|:--------|
| &check; | When using the sorting function below the product page headline the products are being sorted accordingly.
| &check; | 9 Products are rendered for the user on the product pages before pagination is activated
| &check; | When clicking on the pagination previous / next buttons the previous / next 9 products are being rendered
| &check; | When clicking on the pagination first / last buttons the first / last 9 products are being rendered
| &check; | Clicking the Read More button on a product loads the product detail page
| &check; | Clicking the Tag on the product card / product detail loads the products with the same tags
| &check; | Clicking the Category on the product card / product detail loads the products with the same category
| &check; | When clicking the Edit button to the right of the Read More button below the product the product management edit page is loaded
| &check; | The correct image and information for each product is being shown
| &check; | When adding products to the cart the total updates correctly to the right of the cart symbol in the menu.
| &check; | Clicking the Keep Shopping button on the product detail page lists all products
| &check; | Clicking the Add To Bag button on the product detail page adds the quantity and size to the shopping bag and shows a flash message with the bag content and totals in the top right together (with a working link to the shopping bag)
| &check; | Clicking the Add To Wishlist button on the product detail page adds the product to the users wishlist and changes the button to 'In Your Wishlist'
| &check; | It's possible to change the quantity on the product detail page
| &check; | If the product has sizes a size dropdown is visible on the product detail page
| &check; | When clicking on the product image on the product detail page a modal opens with the image
| &check; | When clicking the Edit button to the right of the Add To The Wishlist button below the product the product management edit page is loaded

| Status | **Main Website - Admin Logged In - Product Management - Add Product**
|:-------:|:--------|
| &check; | The form validation is working and does not accept negative numbers on price field
| &check; | When setting the status to draft the product is not visible in the product list for ordinary users
| &check; | When not adding an image to the product a default image is being used instead automatically
| &check; | When doing a search in the product list the correct products are being shown in the list (and the correct amount is being shown as well)
| &check; | When clicking the Cancel button the standard product view is being loaded and all products are being listed
| &check; | When clicking the Add Product button the standard product view is being loaded viewing the newly added product

| Status | **Main Website - Admin Logged In - Product Management - Edit Product**
|:-------:|:--------|
| &check; | When clicking the Edit button the form is prefilled with the product information and the action is changed to 'You are editing this product'.
| &check; | When clicking the Delete Product button a warning modal is being loaded for confirmation. After confirmation the Add Product page is being loaded
| &check; | When doing a search in the blog history list the correct blog posts are being shown in the list (and the correct amount is being shown as well)
| &check; | When clicking the Cancel button the Add Product page is being loaded
| &check; | When clicking the Update button Product Detail page is being loaded viewing the newly updated product

| Status | **Main Website - Admin Logged In - Blog Management - Add Blog Post**
|:-------:|:--------|
| &check; | The form validation is working
| &check; | When setting the status to draft the blog post is not visible in the blog area on the home page for ordinary users
| &check; | When not adding an image to the blog post a default image is being used instead automatically
| &check; | When clicking the Cancel button the home page is being loaded
| &check; | When clicking the Add Blog Post button the product detail is being loaded viewing the newly created blog post
| &check; | When doing a search in the blog history list the correct blog posts are being shown in the list (and the correct amount is being shown as well)

| Status | **Main Website - Admin Logged In - Product Management - Edit Blog Post**
|:-------:|:--------|
| &check; | When clicking the Edit button the form is prefilled with the blog post information and the action is changed to 'You are editing this post'.
| &check; | When clicking the Delete Post button a warning modal is being loaded for confirmation. After confirmation the Add Blog Post page is being loaded
| &check; | When clicking the Cancel button the Add Blog Post page is being loaded
| &check; | When clicking the Update button Blog Post Detail page is being loaded viewing the newly updated blog post
| &check; | When doing a search in the blog history list the correct blog posts are being shown in the list (and the correct amount is being shown as well)

| Status | **Main Website - Admin Logged In - Shopping Bag**
|:-------:|:--------|
| &check; | The correct products and information are showing in the shopping bag (including correct sizes when product has size)
| &check; | When changing the quantity and click update the quantity updates
| &check; | When clicking the remove link the product is being removed from the shopping bag
| &check; | Clicking the Keep Shopping button on the product detail page lists all products
| &check; | Clicking the Secure Checkout button on the product detail page loads the secure checkout page

| Status | **Main Website - Admin Logged In - Checkout**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order summary (including correct sizes when product has size)
| &check; | It the user has updated the profile information the information is prefilled in the form.
| &check; | If the bottom of the form an option to save the delivery inforation to the users profile is visible
| &#10008; | The form validation is working except that the Full Name field can include numbers and the phone number field can include text.
| &check; | When clicking the Adjust Bag Button the Shopping Bag page loads
| &check; | The payment with card number is working correctly (tested with Stripe test numbers)
| &check; | The payment with card number that needs to be authenticated is working correctly (tested with Stripe test numbers). The authentication window is visible.

| Status | **Main Website - Admin Logged In - Order Confirmation Page**
|:-------:|:--------|
| &check; | The correct products, information and delivery amount are showing in the order confirmation and an e-mail has been sent to the registered site user e-mail
| &check; | Webhooks are working and is confirmed in Stripe developer dashboard
| &check; | When clicking the Back To The Store button all products are being listed

| Status | **Main Website - Admin Logged In - Footer**
|:-------:|:--------|
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the Facebook link in the footer area opens Facebook in a new window
| &check; | Register a valid e-mail address in the e-mail signup in the footer is working
| &check; | Register a non-valid e-mail address in the e-mail signup in the footer triggers an error message
| &check; | Register a non-valid e-mail address in the e-mail signup in the footer triggers an error message
| &check; | Clicking the Kollektiv Fem link in the footer area opens the Kollektiv Fem site in a new window
| &check; | Clicking the Privacy Policy link in the footer area opens loads the privacy policy page
| &check; | Clicking the FAQ link in the footer area opens loads the FAQ page

[Back to top](<#table-of-content>)

### Automated Testing
No automated testing has been done during this project.

### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S5/S6/S7       | iPhone 6/7/8       | iPhone 12pro         |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

[Back to top](<#table-of-content>)

### Browser Compatibility
* Google Chrome Version (107.0.5304.110)
* Mozilla Firefox (version 107.0)
* Min (version 1.26.0)
* Apple Safari (version 16.0)
* Microsoft Edge (version 107.0.1418.42)

[Back to top](<#table-of-content>)

### Lighthouse
Google Lighthouse in Chrome Developer Tools was used to test the site within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. I tested the *home page*, *view all blog posts page*, *view all products page*, *product management page* and *blog management page*. The testing showed the following:

* Home Page - Performance: 70, Accessibility: 100, Best Practises: 100, SEO: 92
* View All Blog Posts Page - Performance: 68, Accessibility: 100, Best Practises: 100, SEO: 92
* View All Products Page - Performance: 64, Accessibility: 99, Best Practises: 100, SEO: 92
* Product Management - Performance: 75, Accessibility: 100, Best Practises: 100, SEO: 100
* Blog Management - Performance: 75, Accessibility: 100, Best Practises: 100, SEO: 100

From a general point of view these are quite good results. On all pages the performance is a little bit to low and it is mainly connected to the image sizes. I did some compressing on all the images(approx -50% in size) but still the performance result landed around 70-80. The decrease in the SEO results are mainly connected to the 'read more' links that is not a optimal description from a SEO point of view. In the view all products page the SEO result is affected by the heading elements not being in sequentially-descending order, but this is an active design choice and not a big issue (but I thought it would be proper to highlight it here so that it's clear I'm aware of it).

<details><summary><b>Lighthouse Home Result</b></summary>

![Lighthouse Home Result](readme/assets/images/lighthouse_home.png)
</details><br/>

<details><summary><b>Lighthouse View All Blog Posts Page Result</b></summary>

![Lighthouse View All Blog Posts Page](readme/assets/images/lightouse_all_blog_posts.png)
</details><br/>

<details><summary><b>Lighthouse View All Products Page Result</b></summary>


![Lighthouse View All Products Page Result](readme/assets/images/lightouse_all_products.png)
</details><br/>

<details><summary><b>Lighthouse Product Management Result</b></summary>

![Lighthouse Product Management Result](readme/assets/images/lighthouse_product_management.png)
</details><br/>

<details><summary><b>Lighthouse Blog Management Result</b></summary>

![Lighthouse Blog Management](readme/assets/images/lighthouse_blog_management.png)
</details><br/>

### WAVE
[WAVE](https://wave.webaim.org/) was used to check accessibility. 2 errors were found (1 missing form label and 1 contrast error). The missing form label is connected to the Mailchimp code why I don't want to change anything there. The contrast error is connected to the carousel but when I run the check in other contrast checking software there is no error. So I decided to keep it as it is.

<details><summary><b>WAVE Result</b></summary>

![WAVE Result](readme/assets/images/wave_result.png)
</details><br/>

### a11y Color Contrast Accessibility Validator
[a11y](https://color.a11y.com/Contrast/) was used to check the color contrast accessibility. 0 errors were found.

<details><summary><b>a11y Result</b></summary>

![a11y Result](readme/assets/images/a11y_contrast_test.png)
</details><br/>

[Back to top](<#table-of-content>)

### Peer Review
Additional testing of the site was conducted by people outside of the software development field. Some smaller spelling and grammar errors were found on the site and corrected. No major challenges connected to the design or handling of the site.

## Known bugs
No known bugs besides those in the fixed / unfixed bugs section.

### Fixed Bugs
**2022-11-10**
* Bug: When trying to log in to the site locally a CSRF verification failed appears. This fail was connected to CSRF Trusted Origins which could be fixed by adding a row to settings.py. It is a little bit of a hassle to change the address from time to time due to that the local adress changes.

<details><summary><b>CSRF Fail</b></summary>

![CSRF Fail](readme/assets/images/csrf_fail.png)
![CSRF Fix](readme/assets/images/csrf_fix.png)
</details><br/>

**2022-11-10**
* Bug: I got an Uncaught TypeError connected to the toast messages. This hade to do with me using a newer version of Bootstrap which could be easily fixed.

**2022-11-11**
* Bug: I got quite a lot of problems when I deployed the site to Heroku the first time. I got a 'failed to build backports.zoneinfo'. It was actually quite an easy fix. I added a runtime.txt to the root folder with information about what python version Heroku should install to work with the Heroku version at the time.

**2022-11-14**
* Bug: My mentor noticed that it was possible to add a negative number in the price field when adding a product in the product management area. I fixed this by adding a validation check in the product model (MinValueValidator).

<details><summary><b>Negative Price Bug</b></summary>

![Negative Price Bug 1](readme/assets/images/negative_price_bug_1.png)
![Negative Price Bug 2](readme/assets/images/negative_price_bug_2.png)
![Negative Price Fix](readme/assets/images/negative_price_fix.png)
</details><br />

**2022-11-16**
* Bug: The CSS Validation reported an error that is connected to Bootstrap. When I validate my own CSS code there are no errors at all. So this might be a Font Awesome bug that is out of my control. But I thought it would be proper to highlight the error here in the bugs section.

* Bug: The HTML Validation reported some errors that could be quite easily fixed.

<details><summary><b>HTML Validator Error</b></summary>

**HTML Validator Error Home**

![HTML Validator Error Home](readme/assets/images/html_validator_bug_home.png)

**HTML Validator Error Wishlist**
![HTML Validator Error Wishlist](readme/assets/images/html_validator_bug_wishlist.png)

**HTML Validator Error Remove Wishlist**
![HTML Validator Error Remove Wishlist](readme/assets/images/html_validator_bug_remove_wishlist.png)

**HTML Validator Error Footer**
![HTML Validator Error Footer](readme/assets/images/html_validator_bug_footer.png)

**HTML Validator Error Profile**
![HTML Validator Error Footer](readme/assets/images/html_validator_bug_profile_page.png)
</details><br />

**2022-11-22**
* Bug: When creating a new product and adding a price more than 999.999.99 EUR the site crasches during checkout (throws a 500 error / InvalidRequestError). This bug was fixed by changing the number of accepted digits in the products model. **Update** The problem did show up again during the handshake with Stripe. I have solved this to lower the number of accepted digits, which works fine for the products on this site.

<details><summary><b>999.999.99 EUR Checkout Bug</b></summary>

![999.999.99 EUR Checkout Bug](readme/assets/images/bug_amount.png)
</details><br />


### Unfixed Bugs

**2022-11-10**
* Bug: The Pagination on the site works really well except when the user chooses a specific category or a specific sorting. The problem is when the user clicks the next/previous button on the pagination the category/sorting attribute disappears which means that the next/previous pagination page does not take the users choice into consideration. I managed to fix parts of the problem and had two sessions with two different tutors without success. I tried to solve the problem by adding if statements in the url to keep the category/sorting but it quite fast got really complex. Me and the tutors discussed if it could be easier to handle it from the product views but I needed to move on with the project to not get stuck on this issue to long. The pagination works as it should with the exception when the user chooses category/sorting. Here is an example of the code that partly worked (which I removed in the deployed project. **2022-11-17** *Update: Since this bug was noticed I have added a view all blog posts (and possibility for the user to view all blog posts with a specific category). This means that the pagination bug is fixed on the view all blog posts template.* **2022-11-18** *Update: I have now fixed one bug connected to the list all products-view, the pagination now takes category into consideration if the uses chooses to filter the products on category.*
```
{% if product_list.has_next %}
<li class="page-item"><a class="page-link" href="
        {% if current_sorting == 'None_None' %}?page={{ product_list.next_page_number }}
        {% elif current_sorting == 'None_None' and current_categories %}?page={{ product_list.next_page_number }}&category={{ category }}
        {% elif search_term %}?page={{ product_list.next_page_number }}??page={{ product_list.next_page_number }}&q= {{ search_term }}
        {% elif current_sorting %}?page={{ product_list.next_page_number }}&sort={{ sort }}&direction={{ direction }}
        {% elif current_sorting %}?page={{ product_list.next_page_number }}&sort={{ sort }}&direction={{ direction }}
        {% else %}?page={{ product_list.next_page_number }}
        {% endif %}">Next</a>
</li>
```

**2022-11-14**
* Bug: In the checkout form it is possible for the user to add ordinary letters in the phone number field. I have done some digging and it could be possible to use a validator but I haven't gotten it to work fully. I need to prioritize the rest of the project for now, why this bug is unfixed for now.
* Bug: In the checkout form it is possible for the user to add numerals in the name field. I have done some digging and it could be possible to use a validator but I haven't gotten it to work fully. I need to prioritize the rest of the project for now, why this bug is unfixed for now.

**2022-11-17**
* Bug: The HTML Validator Error connected to the Profile Page has not been corrected yet. I haven't been able to correct it without risking to break the rest of the page. The error is connected to the attribute placeholder not allowed on the select element. The form code for this section is based on the 'Boutique Ado' project with quite complex looping through the form fields. So for now I will not fix it due to the need to prioritize the rest of the project but of course if I would use the site in a live situation I would fix it. Actually if I could do the form again I would not use a loop functionality due to **unnecessary** added complexity.

**2022-11-18**
* Bug: On the add_product.html (Product Management) page the drop-down arrow on the size field is missing. I have tried several fixes without success so I decided to keep it as it is. If the site would have gone live I would have invested more time to fix the bug.

**2022-11-22**
* Bug: After adding a product from the product management view without a size and then change the product to include a size the site crasches (TypeError). This is not something I can't prioritize to fix it due to project deadline but I thought it would be proper to report it as a bug so that you know I am aware of it.

<details><summary><b>Bug When Changing Product Size To True</b></summary>

![Bug When Changing Product Size To True](readme/assets/images/bug_change_product_to_size.png)
</details><br />

**2022-11-22**
* Bug: If a user has added an item in the wishlist and admin changes the product to draft the product still is showing in the users wishlist. If admin removes the product it disappears from the users wishlist. It's quite easy to put in a check if the product is in draft or not on the wishlist (hence not show it if it's not published). I can't prioritize this due to project deadline, but I am aware of the bug (which is not a critical bug I would say).

[Back to top](<#table-of-content>)