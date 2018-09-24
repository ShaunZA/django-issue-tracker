# Django Issue Tracker

This project contains an Issue Tracker in the form of a ticketing system. Users can log on to the site and submit bug reports or feature requests.
Bug reports are free to submit and will get fixed ASAP, feature requests on the other hand will cost €30 to submit and will get worked on first.
Stripe has been integrated into the app to make it easy to process payments.
 
## UX
 
This web site is intended for users who use Unicorn Attractor often and have found some bugs they would like to report back or would like a new feature put in that they might think would benefit the community as a whole.

Mockups can be found in the /mockup/ folder in this Git repo.

User Stories:
- As a user of Unicorn Attractor I would like to easily submit bug reports so the developers can fix them.
- As a user of Unicorn Attractor I would like to easily submit a feature request so the developers can implement them.
- As a developer I would like to be able to easily sort the tickets out to find the right one to work on first.
- As a user I would like the opportunity to talk with a developer working on my ticket or other users.

## Features

- User Login System - Users must register with an email and username if they wish to submit bug reports or feature requests.
- Ticketing System - Users can create two types of tickets, bug reports or feature requests. Tickets contain a title, description, priority, author, date submitted, number of comments (if any) and a glyph of a bug or a new feature. The date the ticket was made and who made it are automatically added when submitted. Admins/Super Users can remove the ticket once completed from the /admin page.
- Comments System - Registered users can submit comments to individual tickets. Admins/Super Users can remove comments from the /admin page.
- Search Function - The search acts as a powerful filter in conjunction with the 'Sort By' button. It covers the title, description, priority and ticket-type within the search.
    eg. You can show all bugs with the word Unicorn in them in order of date submitted by searching "bug unicorn" and ordering by "Date Added".
- Sorting of Tickets - The 'Sort By' button can sort the tickets in by Priority, Title, Ticket Type, Author or Date Added. This was achieved with the 'django-sorting' package.

### Features Left to Implement
- Ability for user to delete own comment / ticket.
- Ability for Admin to mark ticket as done and leave it up instead of deleting.

## Technologies Used

- [Django Framework](https://jquery.com)
    - Django was used in the back end to interface with python for the logic of the site.
- [Django-Sorting](https://github.com/agiliq/django-sorting)
    - Sorting was used to sort the tickets
- [Django-Pagination](https://pypi.org/project/django-pagination/)
    - Pagination was used to cut down the long list of tickets into managable chunks.
- [Bootstrap](http://getbootstrap.com/)
    - The project uses Bootstrap for its CSS and Mobile First approach to web design.
- [Font Awesome](https://fontawesome.com/)
    - Font Awesome provides very handy icons in svg format.
- [JQuery](https://jquery.com)
    - The project uses JQuery to simplify DOM manipulation.

## Testing

I tested all features manually during the process of making the site.
The following are some examples of the tests.

1. Submitting a ticket:
    1. Go to the "Create Ticket" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and 'bug' selected and verify ticket gets submitted
    5. Try to submit the form with all inputs valid and 'feature' selected and verify user gets redirected to payment form then back to creation page
    6. Once ticket is created make sure all entered information is correct and Username corresponds with the Author and the Date Added is correct

2. Comments:
    1. Click on any ticket
    2. Click 'Comment' button
    3. Try to submit the empty form and verify that an error message about the required fields appears
    4. Try to submit the form with the input valid and verify comment gets submitted

3. Search:
    1. Enter 'bug' into Search bar
    2. Verify only bug tickets show up (or tickets with bug in their name or description)
    3. leave the search bar empty and click 'Search' button
    4. make sure list of tickets still show

## Deployment

The project is deployed on Heroku, you can reach it by going to this [link](https://unicorn-issue-tracker.herokuapp.com/)
The following Config Vars are required in order to run the app on Heroku
- DATABASE_URL (for the database, you can get this by creating a new add-on in Heroku for a Postgres database)
- SECRET_KEY (Django's secret key)
- STRIPE_PUBLISHABLE (Stripes public key)
- STRIPE_SECRET (Stripes private key)

## Credits

### Media
- The logo used in the Stripe checkout process was taken from the android ROM, [AOKP](https://aokp.co/)

### Acknowledgements

- I received inspiration for this project from Github issue tracker and comments system