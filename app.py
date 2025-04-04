from flask import *

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prime', methods=['GET', 'POST'])
def prime_numbers():
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            
            if num1 < 0 or num2 < 0:
                return "Input number should be greater than zero."
            if num2 < num1:
                return "The second input number should be greater than the first number."
            
            primes = [i for i in range(num1, num2 + 1) if is_prime(i)]
            return render_template('result.html', result=primes)
        
        except ValueError:
            return "Please enter valid integer values."
    
    return render_template('prime_form.html')


@app.route('/palindrome', methods=['GET', 'POST'])
def palindrome():
    if request.method == 'POST':
        input_str = request.form['input_string']
        if input_str == input_str[::-1]:
            message = f"You entered {input_str}. It is a palindrome."
        else:
            message = f"You entered {input_str}. It is not a palindrome."
        return render_template('result.html', result=message)
    
    return render_template('palindrome_form.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        
        
        fill_blank_answer = "east"
        mcq_answer = "b"
        correct_checkboxes = {"a", "d"}
        

        fill_blank_response = request.form.get("fill_blank")
        mcq_response = request.form.get("mcq")
        checkbox_responses = set(request.form.getlist("checkbox"))
        
        if fill_blank_response and fill_blank_response.lower() == fill_blank_answer:
            score += 1
        if mcq_response == mcq_answer:
            score += 1
        score += len(correct_checkboxes.intersection(checkbox_responses)) * 0.5
        
        message = f"You scored {score} out of 3."
        return render_template('result.html', result=message)
    
    return render_template('quiz_form.html')

app.run(debug=True, host = "0.0.0.0", port = 80)