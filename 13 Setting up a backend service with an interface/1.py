from flask import Flask, request

app = Flask(__name__)
@app.route(f'/prime_number/<number>')
def prime(number):
    number = int(number)
    is_prime = True
    if number <= 1:
        print(False)
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    response = {
        "Number": number,
        "isPrime": is_prime,
    }
    return response
if __name__ == '__main__':
    # app.run(use_reloader=True, host='127.0.0.1', port=3000)
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
