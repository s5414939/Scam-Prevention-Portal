from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/scenarios')
def scenarios():
    return render_template('scenarios.html', title='Scenarios')

@app.route('/scenarioscover')
def scenarioscover():
    return render_template('scenarioscover.html', title='Scenarios')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/overview')
def overview():
    return render_template('overview.html', title='Scams Overview')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

@app.route('/janescenarioresult')
def janescenarioresult():
    return render_template('janescenarioresult.html', title='Scenario Result')

@app.route('/markscenarioresult')
def mark_scenario_result():
    return render_template('markscenarioresult.html', title='Mark Scenario Result')

@app.route('/emailoneresult')
def emailoneresult():
    return render_template('emailoneresult.html', title='Email One Result')

@app.route('/emailtworesult')
def emailtworesult():
    return render_template('emailtworesult.html')

@app.route('/emailthreeresult')
def emailthreeresult():
    return render_template('emailthreeresult.html')

@app.route('/emailfourresult')
def emailfourresult():
    return render_template('emailfourresult.html')

@app.route('/videosection')
def videosection():
    return render_template('videosection.html', title='Video Section')

# Handle GET and POST requests for the feedback form under one route definition
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            feedback_text = request.form['feedback']
            flash('Thank you for your feedback!', 'success')
            return redirect(url_for('feedback'))
        except Exception as e:
            flash('An error occurred while submitting your feedback. Please try again.', 'error')
            return redirect(url_for('feedback'))
    else:
        return render_template('feedback.html', title='Feedback')

if __name__ == '__main__':
    app.run(debug=True)
