# 🌍 Language Translator Agent (using Gemini API + Chainlit)

This is an intelligent language translation agent built using Python, Chainlit, and Google Gemini API. It allows users to easily translate text between different languages in a friendly chatbot interface.

You simply give a command like:

Translate: Hello, how are you? in urdu 

And it replies:

ہیلو، آپ کیسے ہیں؟

The project uses the Gemini 2.0 Flash model via Chainlit, which provides a beautiful, interactive interface for AI chat experiences.

Features:
✅ Translate between any two languages  
✅ Fast and smart language processing  
✅ Simple prompt structure using `Translate | From | To`  
✅ Chat-style interface with welcome message  
✅ Clean codebase and modular setup  
✅ Uses `.env` for secure API key management  

#Technologies Used:


Python – Programming language  
Chainlit – Chat UI framework for AI apps  
Gemini API – Google’s LLM used for translation  
dotenv – For loading environment variables securely  

Project Structure:
- main.py → Chainlit app with user interaction logic  
- agents.py → Defines agent, model, runner configuration  
- .env → Store your Gemini API key here  
- README.md → Project documentation (this file)  

Getting Started:
1. Clone the Repo:
git clone https://github.com/your-username/translator-agent  
cd translator-agent  

2. Add your API Key:
Create a `.env` file in the root folder:
GEMINI_API_KEY=your_actual_api_key_here  
Make sure your key is active and you’ve access to Gemini models.

3. Install Dependencies:
pip install chainlit python-dotenv  

Run the App:
Start the Chainlit app with:
chainlit run main.py  

Then open the browser link shown in the terminal. You'll see your chat interface ready to go!

How to Use:
You can ask translations using the format:
Translate: [your sentence] | From: [source language] | To: [target language]

Example:
Translate: I love learning AI in Arabic  
Response:

أنا أحب تعلم الذكاء الاصطناعي

#How It Works:

- When the app starts, a welcome message is shown.  
- The agent waits for your input.  
- It extracts the sentence, source, and target languages.  
- Then it builds a prompt and sends it to the Gemini 2.0 Flash model.  
- The translated sentence is returned and shown to the user.  

Error Handling:
If something goes wrong (e.g., no input, wrong format, invalid API key), the app will respond with a helpful error message instead of crashing.


#Made By:

**Mueza** – A passionate learner exploring AI, LLMs, and real-world chatbot projects.

License:
This project is for educational/demo purposes. You can adapt it for personal or learning use.
