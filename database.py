from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://rtr4ox6cte2hogihn1hh:pscale_pw_SJgglkgnwWxj91Gb5aGACAA7TeQLGpXh6hc4yzuaW9a@aws.connect.psdb.cloud/careerlinkup?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        results_as_dict = result.mappings().all()
        # results_as_dict = result.mappings().fetchall()
        jobs = []
        for row in results_as_dict:
            jobs.append(row)
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT * FROM jobs WHERE id={id}")
        )
        rows = []
        for row in result.all():
            rows.append(row._mapping)
        if len(rows) == 0:
            return None
        else:
            return row


def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        conn.execute(query,
                     job_id=job_id,
                     full_name=data['full_name'],
                     email=data['email'],
                     linkedin_url=data['linkedin_url'],
                     education=data['education'],
                     work_experience=data['work_experience'],
                     resume_url=data['resume_url'])
