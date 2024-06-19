from sqlalchemy import text
from database import engine

def get_name_from_email(email):
    results = None
    sql = text(f"SELECT * FROM tempx.candidate_profile where email={email}") 
    with engine.connect() as conn:
        results = conn.execute(sql)
        # View the records 
        for record in results: 
            print("\n", record)
    return len(results.fetchall())

def get_name_from_email_bd(email):
    results = None
    sql = text(f"SELECT * FROM tempx.candidate_profile where email={email}") 
    with engine.connect() as conn:
        results = conn.execute(sql)
        # View the records 
        for record in results: 
            print("\n", record)
    return len(results.fetchall())

def get_rows():
    results = None
    sql = text("SELECT * FROM tempx.candidate_refer ") 
    with engine.connect() as conn:
        results = conn.execute(sql)
        # # View the records 
        # for record in results: 
        #     print("\n", record)
    return len(results.fetchall())

def insert_rows(data):
    print(data)
    data_ins = { "referred_by_email": data.get('Referred By Email ') , 
          "name": data.get('Full Name'), 
          "email": "",
          "phone_number": f"+1{data.get('Mobile Number')}",
           "invited_time": data.get('Timestamp') }
    statement = text("""INSERT INTO tempx.candidate_refer (referred_by_email, name, email, phone_number, invited_time) VALUES(:referred_by_email, :name, :email, :phone_number, :invited_time)""").params(**data_ins)
    print(statement)
    print(data_ins)
    with engine.connect() as conn:
        print('inside insert conn')
        # Begin a transaction
        trans = conn.begin()
        try:
            # Execute the statement
            results = conn.execute(statement)
            print(results)
            # Commit the transaction
            trans.commit()
        except Exception as e:
            # Rollback the transaction in case of error
            trans.rollback()
            print(f"Error occurred: {e}")
    
