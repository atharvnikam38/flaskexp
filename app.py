from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Portfolio route
@app.route('/portfolio')
def portfolio():
    projects = [
        {
            "title": "Weather App",
            "description": "Developed a weather application using Flutter, integrating API functionality to provide real-time weather updates for any location.",
            "image": "weather.png",
            "link": "https://weatherappatharv38.netlify.app/"
        },
        {
            "title": "Trainer Website",
            "description": "Designed and developed a WordPress-based website for a professional trainer. Customized themes and plugins to create a responsive and visually appealing user interface.",
            "image": "fitness.png",
            "link": "https://atharvnikam1.rf.gd"
        },
        {
            "title": "Myntra Clone",
            "description": "Developed a clone of the Myntra website to simulate an e-commerce platform. Utilized HTML, CSS, and JavaScript to create a responsive and visually appealing user interface.",
            "image": "myntra.png",
            "link": "https://github.com/atharvnikam38/MyntraClone"
        }
    ]
    return render_template('portfolio.html', projects=projects)

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template('contact.html')

# Success route
@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)