from flask import Flask, request, jsonify
import json

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

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number', type=int)
    
    if number is None:
        return jsonify({
            "number": "invalid",
            "error": True
        }), 400

    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": [
            "prime" if is_prime(number) else "composite",
            "perfect" if is_perfect(number) else "imperfect",
            "odd" if number % 2 != 0 else "even"
        ],
        "digit_sum": digit_sum(number),
        "fun_fact": f"{number} is an interesting number!"
    }
    
    response = app.response_class(
        response=json.dumps(result, indent=4),  # Pretty-print JSON output
        status=200,
        mimetype='application/json'
    )
    
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

