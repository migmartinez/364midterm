# 364midterm

***CODE REQUIREMENTS***
X Ensure that the SI364midterm.py file has all the setup (app.config values, import statements, code to run the app if that file is run, etc) necessary to run the Flask application, and the application runs correctly on http://localhost:5000 (and the other routes you set up)

X Add navigation in base.html with links (using a href tags) that lead to every other viewable page in the application. (e.g. in the lecture examples from the Feb 9 lecture, like this )

X Ensure that all templates in the application inherit (using template inheritance, with extends) from base.html and include at least one additional block.

X Include at least 2 additional template .html files we did not provide.

X At least one additional template with a Jinja template for loop and at least one additional template with a Jinja template conditional.
	- These could be in the same template, and could be 1 of the 2 additional template files.

X At least one errorhandler for a 404 error and a corresponding template.

X At least one request to a REST API that is based on data submitted in a WTForm.

X At least one additional (not provided) WTForm that sends data with a GET request to a new page.

X At least one additional (not provided) WTForm that sends data with a POST request to the same page.

X At least one custom validator for a field in a WTForm.

X At least 2 additional model classes.

X Have a one:many relationship that works properly built between 2 of your models.

X Successfully save data to each table.

X Successfully query data from each of your models (so query at least one column, or all data, from every database table you have a model for).

X Query data using an .all() method in at least one view function and send the results of that query to a template.

X Include at least one use of redirect. (HINT: This should probably happen in the view function where data is posted...)

X Include at least one use of url_for. (HINT: This could happen where you render a form...)

X Have at least 3 view functions that are not included with the code we have provided. (But you may have more! Make sure you include ALL view functions in the app in the documentation and ALL pages in the app in the navigation links of base.html.)

***ADDITIONAL REQUIREMENTS***
- Include an additional model class (4 total with at least 3 columns)

X Code that allows user to submit duplicate data to a form, but will not save it
***ALL ROUTES + THEIR CORRESPONDING TEMPLATES:***
'/' --> 'base.html'
'/names' --> 'name_example.html'
'/leaderboards' --> 'leaderboards.html'
'/movies' --> 'movie_sugg.html'
'/games' --> 'game_sugg.html'

***APP DESCRIPTION***

This app is designed for friend groups who are looking for something new to do, and track which friends truly appreciate them! There is a Game Suggestions section which calls on the IGDB REST API to suggest a video game to play, there is a Leaderboards section to see who has the most buds of all, and there is a Movie Suggestions section where users can type in their favorite movie and it will be displayed back to them.