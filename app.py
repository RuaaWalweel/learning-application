from flask import Flask, render_template, request, jsonify
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API key (replace with your own OpenAI API key)
openai.api_key = 'your-openai-api-key-here'  # Replace with your actual key

# Default route to serve the index.html file
@app.route('/')
def index():
    return render_template('index.html')

# Route for Subjects page
@app.route('/subjects')
def subjects():
    return render_template('subjects.html')

# Route for Grades page
@app.route('/grades')
def grades():
    return render_template('grades.html')

# Route for Chatbot page
@app.route('/chat')
def chat():
    return render_template('chatbot.html')

# Route for About page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for Login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for Profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

# API route to handle POST request and integrate with OpenAI
@app.route('/api', methods=['POST'])
def chat_api():
    # Get the message from the POST request
    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Call OpenAI API to generate a response based on user input using GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # GPT-3.5 Turbo model
            messages=[{
                "role": "system", "content": "You are a helpful assistant."
            }, {
                "role": "user", "content": user_message
            }]
        )

        # Extract the response from OpenAI API
        bot_reply = response['choices'][0]['message']['content'].strip()

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
