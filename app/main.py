from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/_add_numbers")
def add_numbers():
    """add 2 numbers:

    Example:
    http://localhost:5400/_add_numbers?a=10&b=5

    Returns:
        [type]: [description]
    """
    a = request.args.get("a", 0, type=int)
    b = request.args.get("b", 0, type=int)
    return jsonify(result=a + b)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5400")

