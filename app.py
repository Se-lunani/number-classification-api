from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        num = int(request.args.get('number'))
        fun_fact = requests.get(f"http://numbersapi.com/{num}").text
        response = {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": ["armstrong" if is_armstrong(num) else "normal", "odd" if num % 2 else "even"],
            "digit_sum": sum(int(d) for d in str(num)),
            "fun_fact": fun_fact
        }
        return jsonify(response), 200
    except ValueError:
        return jsonify({"number": request.args.get('number'), "error": True}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

