import openai

# Function to initiate a real-time conversation with the model
def start_conversation():
    # Set your OpenAI API key
    openai.api_key = "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"

    # Start the conversation history with an initial system message
    conversation_history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Start chatting with the AI! Type 'exit' to end the conversation.\n")

    while True:
        # Get user input for each turn of the conversation
        user_input = input("You: ")

        # Exit the loop if the user types 'exit'
        if user_input.lower() == "exit":
            print("Ending conversation.")
            break

        # Add user input to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Make a request to the OpenAI API with the conversation history and enable streaming
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Use the real-time model
            messages=conversation_history,
            stream=True  # Stream the response in real-time
        )

        # Print the response as it's being streamed
        print("AI: ", end="")
        for chunk in response:
            content = chunk["choices"][0]["delta"].get("content", "")
            if content:
                print(content, end="")  # Print each part of the AI response as it's generated

        print()  # Print a new line for the next prompt

        # Add the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": content})

if __name__ == "__main__":
    start_conversation()
