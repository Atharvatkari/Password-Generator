from flask import Flask, request, render_template
import random
import string



app = Flask(__name__)

@app.route('/index page')
def index():
    return "Hello, World!"

def generate_password(length=12, upper=True, lower=True, nums=True, syms=True):
    all_chars = ""
    if upper:
        all_chars += string.ascii_uppercase
    if lower:
        all_chars += string.ascii_lowercase
    if nums:
        all_chars += string.digits
    if syms:
        all_chars += string.punctuation

    if not any([upper, lower, nums, syms]):
        return "At least one character type should be selected."

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        length = int(request.form.get('length'))
        quantity = int(request.form.get('quantity'))
        upper = request.form.get('upper') == 'on'
        lower = request.form.get('lower') == 'on'
        nums = request.form.get('nums') == 'on'
        syms = request.form.get('syms') == 'on'
       
        '''
        all_chars = ""
        if upper:
            all_chars += string.ascii_uppercase
        if lower:
            all_chars += string.ascii_lowercase
        if nums:
            all_chars += string.digits
        if syms:
            all_chars += string.punctuation
        
        passwords=[]    
        for i in range(quantity):
            password = "".join(random.choice(length) for _ in range(quantity))
            passwords.append(password)'''
            
        password_list=[]
        
        passwords = [generate_password(length) for _ in range(quantity)]
        for i in passwords:
            password_list.append(i)
        return render_template('index.html', result=password_list)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
