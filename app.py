from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from Flutter

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    devices = data.get('devices', [])
    print(f"Received request with {len(devices)} devices")
    
    recommendations = []
    for device in devices:
        print(f"Processing device: {device['name']} - {device['watts']} watts, {device['hoursPerDay']} hrs/day")
        tips = []
        if device['watts'] > 500:
            tips.append("Consider replacing this device with a more energy-efficient model.")
        if device['hoursPerDay'] > 8:
            tips.append("Usage exceeds 8 hrs/day. Try reducing usage time.")

        for tip in tips:
            recommendations.append({
                "device": device['name'],
                "tip": tip
            })
    
    # Add general recommendations if no specific ones were generated
    if not recommendations:
        print("No specific recommendations generated, adding general tips")
        general_tips = [
            "Turn off lights when not in use.",
            "Unplug chargers when not in use to avoid phantom energy usage.",
            "Consider using smart power strips for electronics.",
            "Use LED bulbs instead of incandescent bulbs to save energy.",
            "Make sure to fully load your dishwasher and washing machine before running them."
        ]
        
        for tip in general_tips:
            recommendations.append({
                "device": "General",
                "tip": tip
            })
    
    print(f"Returning {len(recommendations)} recommendations")
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
