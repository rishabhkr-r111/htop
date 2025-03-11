from flask import Flask, render_template_string
import subprocess
import datetime
import os
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Rishabh Kumar"
    
    username = os.path.expanduser("~")
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    
    html_template = """
    <html>
    <body>
        <h2>System Information</h2>
        <p><strong>Name:</strong> {{ name }}</p>
        <p><strong>User:</strong> {{ username }}</p>
        <p><strong>Server Time (IST):</strong> {{ server_time }}</p>
        <h3>TOP output:</h3>
        <pre>{{ top_output }}</pre>
    </body>
    </html>
    """
    
    return render_template_string(html_template, 
                                 name=name,
                                 username=username,
                                 server_time=server_time,
                                 top_output=top_output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)