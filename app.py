from gpt4free import you
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    output = ""
    i=0
    for chunk in you.Completion.create(prompt = str(request.form.get('prompt'))):
        if i==0:
            output+=chunk[1]
        i+=1
        print(chunk, end="\n", flush=True)
    
    return jsonify( {'response' : output} )

if __name__ == '__main__': 
    app.run(debug=False, host='0.0.0.0')