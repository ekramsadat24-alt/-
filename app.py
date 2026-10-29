from flask import Flask, render_template
import os

app = Flask(__name__)

COUNTER_FILE = 'visitor_count.txt'

def get_visitor_count():
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'w', encoding='utf-8') as f:
            f.write('0')
        return 0
    try:
        with open(COUNTER_FILE, 'r', encoding='utf-8') as f:
            return int(f.read().strip())
    except:
        return 0

def increment_visitor_count():
    count = get_visitor_count() + 1
    with open(COUNTER_FILE, 'w', encoding='utf-8') as f:
        f.write(str(count))
    return count

@app.route('/')
def home():
    current_visitors = increment_visitor_count()
    return render_template('index.html', visitors=current_visitors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)