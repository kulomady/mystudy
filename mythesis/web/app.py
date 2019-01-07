from flask import Flask, render_template
from flask import request, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


class ReusableForm(Form):
	berita = TextAreaField('Berita:', validators=[validators.required()])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176aadsf'


@app.route('/')
def hello_mady():
    return render_template("mady_hello.html")

@app.route("/hoax", methods=['GET', 'POST'])
def hoax():
	form = ReusableForm(request.form)
	 
	print form.errors
	if request.method == 'POST':
		berita=request.form['berita']
		print berita
	 
	if form.validate():
		# Save the comment here.
		flash(berita)
	# else:
	# 	flash('All the form fields are required. ')
	 
	return render_template('hoax.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
