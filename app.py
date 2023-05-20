from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lagos, Nigeria',
        'salary': '#200,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Abuja, Nigeria',
        'salary': '#300,000'
    },
    {
        'id': 3,
        'title': 'Full Stack Web Developer',
        'location': 'Lagos, Nigeria',
        'salary': '#250,000'
    },
    {
        'id': 4,
        'title': 'Front-end Engineer',
        'location': 'Remote',
        'salary': '#300,000'
    },
    {
        'id': 5,
        'title': 'Back-end Engineer',
        'location': 'San Francisco, USA',
        'salary': '$350,000'
    }
]


@app.route('/')
def index():
    return render_template("home.html", jobs=JOBS, company_name='CareerLinkUp')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
