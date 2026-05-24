from flask import Flask, jsonify, request

app = Flask(__name__)

ITEMS = [
    {
        "id": "iphone-15",
        "category": "electronics",
        "name": "iPhone 15 128GB",
        "tags": ["iphone", "mobile", "apple"],
        "offers": [
            {"platform": "Amazon", "price": 64999, "rating": 4.6, "deliveryMinutes": 1440},
            {"platform": "Flipkart", "price": 66499, "rating": 4.5, "deliveryMinutes": 2880},
            {"platform": "Croma", "price": 67990, "rating": 4.4, "deliveryMinutes": 240},
        ],
    }
]


def recommendation(item):
    cheapest = min(item["offers"], key=lambda offer: offer["price"])
    fastest = min(item["offers"], key=lambda offer: offer["deliveryMinutes"])
    best = max(
        item["offers"],
        key=lambda offer: (cheapest["price"] / offer["price"]) * 42
        + (offer["rating"] / 5) * 28
        + (fastest["deliveryMinutes"] / offer["deliveryMinutes"]) * 20
        + 10,
    )
    return {"best": best, "cheapest": cheapest, "fastest": fastest}


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "oneCompare Flask API"})


@app.get("/api/search")
def search():
    query = request.args.get("q", "").lower()
    category = request.args.get("category", "all")
    results = [
        item
        for item in ITEMS
        if (category == "all" or item["category"] == category)
        and (not query or query in f"{item['name']} {' '.join(item['tags'])}".lower())
    ]
    return jsonify({"results": results})


@app.get("/api/recommend/<item_id>")
def recommend(item_id):
    item = next((entry for entry in ITEMS if entry["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Comparison item not found"}), 404
    return jsonify({"item": item, "recommendation": recommendation(item)})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
