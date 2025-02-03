# Number Classification API

A simple API that classifies numbers based on their mathematical properties such as prime, perfect, and armstrong. It also provides a fun fact about the number.

## Features
- Returns **prime** status of the number.
- Checks if the number is **perfect**.
- Identifies whether the number is an **Armstrong number**.
- Returns **odd/even** classification.
- Calculates the **sum of digits**.
- Provides a **fun fact** from the [Numbers API](http://numbersapi.com/#42).

## API Endpoint
- **Endpoint**: `GET /api/classify-number?number={number}`
- **Method**: GET
- **Parameters**:
  - `number`: The integer to classify (must be a valid integer).
  
### Example Request:
```bash
curl -X GET "http://your-public-ec2-ip/api/classify-number?number=371"

### This is the Output of sample okay response
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

### This is the output of Sample Bad Request 
{
    "number": "alphabet",
    "error": true
}


