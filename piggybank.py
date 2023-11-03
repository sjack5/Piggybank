from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def display_data():
    conn = sqlite3.connect("PiggybankDatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Piggybank")
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/add_row', methods=['POST'])
def add_row():
    if request.method == 'POST':
        new_data = (
            request.form['TransactionID'],
            request.form['TransactionDate'],
            request.form['TransactionCategory'],
            request.form['TransactionName'],
            request.form['TransactionPrice']
        )
        
        conn = sqlite3.connect("PiggybankDatabase.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Piggybank (ID, Date, 'Transaction Category', 'Transaction Name', 'Transaction Amount') VALUES (?, ?, ?, ?, ?)", new_data)
        conn.commit()
        conn.close()
        
        # Redirect back to the main page after adding data to the database
        return redirect('/')
    
    return redirect('/')
    
if __name__ == '__main__':
    app.run()
