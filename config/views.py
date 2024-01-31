from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)
openai.api_key = api_key

def chatbot(request):
    #  Configure OpenAI API client with your api key
    chatbot_response = None
    # If the user has submitted a question
    print("before if statement")
    if api_key is not None and request.method == 'POST':
        print("inside if statement")
        user_input = request.POST.get('user_input')
        # prompt = user_input 
        prompt = f"translate this text to Kurdish and use Latin alphabet: {user_input}"
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.5,
            max_tokens=256,
            # stop="." # Stop the sequence on the first period.
        )
        print("before response")
        print(response)
        chatbot_response = response.choices[0].text
    
    context = dict(
        response_chatbot=chatbot_response,
    )
    return render(request, 'core/main.html',context)

def main_home(request):
    return render(request, 'core/base.html')