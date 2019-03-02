### POINTS: 2
### KEY: Really Nice job man!

# Mini-Project Django

THIS IS A SOLO PROJECT.

* A School needs a website to record the teaching time for each teacher to import it into an invoicing system. 

* To do this, create an entirely new Django project from scratch. 

* Make a site that will display and manage time card entries to/from a SQLite database. 

* The attributes that can be entered in a timecard site should be ```Teacher name, school, subject, hours, date of work, and date of entry```.

* Make the ```date of entry``` be the default time the entry is made and invisible to the normal user (only visible via Django admin console)

* On the homepage, show all entries in the database. They should be hyper-linked as follows:
-- Selecting the ```Teacher Name``` should show all entries for the selected Teacher
-- Selecting the ```Teacher School``` should show the hours for all Teachers from the selected School (if you want to get awesome and use some grouping by Teacher and such for a better resulting output like showing total hours or whatever, rock on. You don't have to, but figure you are up for the challenge).

* For each entry displayed in any View, offer an option to edit or delete the entry in the form of hyperlink or button

* Ask for a confirmation prior to deleting an entry and an ability for the User to abort/cancel the request and return to home page if they so choose.

================================================================

### Extra HAPPY HAPPY JOY JOY Bonus: 

Functionality is the key and what matters most for grade. Can be ugly as all get out if works, but aesthetics do matter in app design so make the app as visually appealing as time allows. 

Feel free to use your own CSS and/or basic BootStrap (https://getbootstrap.com/docs/4.3/getting-started/introduction/) to gussy things up. 

In addition to wrapping your page content in a ```<div class='container'>``` and maybe throwing your header in a ```<h1 class='jumbotron'>```you might assign any HTML tables ```class='table'``` and any form submit buttons ```<input class="btn btn-primary" type="submit" value="Submit"/>``` for starters, then explore if u have time. You're welcome :-P 

### Extra, Extra Bonus:
Give me a way to export all this time card data as Comma Separated Values (CSV) so I can easily import into my other system.



