from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

class HomePage(MethodView):
    def get(self):
        #return "<h2>Hello</h2>"
        #return render_template('templates/index.html')
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        #return "I am the bill form page!"
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)

class Resultpage(MethodView):
    #def get(self):
        #return "Here we will see the results!"
    def post(self):
        billform = BillForm(request.form)
        amount = billform.amount.data
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = billform.days_in_house1.data

        the_bill = flat.Bill(amount, period)
        #the_bill = flat.Bill(billform.amount.data, billform.period.data)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(billform.name2.data, billform.days_in_house2.data)
        #return amount
        return render_template('results.html', name1=flatmate1.name, amount1=flatmate1.pays(the_bill, flatmate2), name2=flatmate2.name, amount2=flatmate2.pays(the_bill, flatmate1))
        return f"{flatmate1.name} pays {flatmate1.pays(the_bill, flatmate2)}"

class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Perioid: ", default="December 2020")

    name1 = StringField("Name: ", default="John")
    days_in_house1= StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Marry")
    days_in_house2= StringField("Days in the house: ", default=12)
                        
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=Resultpage.as_view('results_page'))

app.run(debug=True)
