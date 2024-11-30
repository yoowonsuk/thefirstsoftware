from flask.views import MethodView
from flask import Flask, render_template, request
from calorie import Calorie

app = Flask(__name__)


class HomePage(MethodView):
    """ Class to create webpage instances whenever a user
    visits that webpage.
    """

    def get(self):
        # Return The HTML template to the user
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = Calories()

        return render_template('calories_form_page.html',
                caloriesform=calories_form)

    def post(self):
       calorie = Calorie()
       calories = calorie.calculate()

       return render_template('calories_form_page.html',
                              calories=calories,
                              result=True)


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)


# four spaces, not tab
# enter should align
# no longer than 79 characters
# Two black lines around classes
# one black line around methods
# white space : assignement operators
# No white space: argument delcaration
# lower_case for vars, func, and methods
# uppser_case for classes (camelCase)
# comments: start with a space and a capital letter & can continue in the next lines
# Doc Strings: string starts at the first quotes, second quotes in a separate line
