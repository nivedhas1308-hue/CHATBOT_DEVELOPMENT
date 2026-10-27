Week 9 – Building an Interactive AI Chatbot using Ollama

Project Overview
This project develops an interactive education chatbot using Python and the locally running Llama 3.2 model through Ollama.

 Objectives
- Build an AI chatbot using a local Large Language Model.
- Answer educational questions in simple language.
- Maintain conversation context.
- Save questions and responses for future analysis.

 Technologies Used
- Python
- Ollama
- Llama 3.2
- Pandas
- Jupyter Notebook

 Project Structure
- `chatbot.py` – Command-line chatbot.
- `dataset/sample_questions.csv` – Sample educational questions.
- `dataset/chat_history.csv` – Saved command-line conversations.
- `dataset/responses.csv` – Saved chatbot responses.
- `dataset/chatbot_logs.txt` – Readable conversation logs.
- `notebook/Week9_Chatbot_Development.ipynb` – Notebook implementation.
- `requirements.txt` – Python dependencies.

Implementation
The chatbot accepts user questions, generates answers using Llama 3.2, maintains conversation history, and stores interactions in files for later analysis.

Conclusion
The project demonstrates how to build and test a local AI chatbot using Python and Ollama. The notebook and saved conversation files support further development and analysis.