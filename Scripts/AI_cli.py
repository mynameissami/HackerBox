import os
from groq import Groq
from dotenv import load_dotenv

class Main():
   def __init__(self) -> None:
       load_dotenv()
       self.api = os.getenv('API_KEY')
       self.model_id_ini = os.getenv('MODEL_ID')
       self.default_reasoning_effort = os.getenv('REASONING_EFFORT', 'medium')  # Default to 'medium'
       # Initialize the Groq client with API key
       if not self.api:
           raise ValueError("API_KEY environment variable is not set in .env file")
       if not self.model_id_ini:
           raise ValueError("MODEL_ID environment variable is not set in .env file")
       if not self.api and not self.model_id_ini:
           raise ValueError("API_KEY and MODEL_ID environment variables are not set in .env file")
       self.client = Groq(api_key=self.api)

   def AI_initialize(self, message, model_id=None, reasoning_effort=None, supports_reasoning=None):
        if model_id is None:
            model_id = self.model_id_ini

        # Determine if reasoning is supported by the model
        if supports_reasoning is None:
            supports_reasoning = "reasoning" in model_id.lower()

        # Use provided reasoning_effort, or fallback to default
        if reasoning_effort is None:
            reasoning_effort = self.default_reasoning_effort

        # Prepare the base parameters
        params = {
            "model": model_id,
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
            "temperature": 1,
            "max_completion_tokens": 8192,
            "top_p": 1,
            "stream": True,
            "stop": None
        }

        # Only add reasoning_effort if the model supports it and a value is provided
        if supports_reasoning and reasoning_effort is not None:
            params["reasoning_effort"] = reasoning_effort

        completion = self.client.chat.completions.create(**params)
        return completion

   def AI_run(self, reasoning_effort=None, supports_reasoning=None):
       print("AI Assistant is ready! Type 'quit' to exit.")
       print(f"Using model: {self.model_id_ini}")
       print(f"reasoning_effort: {reasoning_effort}\n")

       while True:
           user_prompt = input(f"Prompt ~ {self.model_id_ini}: ")

           # Exit condition
           if user_prompt.lower() in ['quit', 'exit', 'q']:
               print("Goodbye!")
               break

           # Skip empty prompts
           if not user_prompt.strip():
               print("Please enter a valid prompt.\n")
               continue

           try:
               # Pass reasoning_effort to AI_initialize
               completion = self.AI_initialize(
                   message=user_prompt,
                   reasoning_effort=reasoning_effort,
                   supports_reasoning=supports_reasoning
               )

               # Print response
               print("\nResponse: ", end="")
               for chunk in completion:
                   content = chunk.choices[0].delta.content
                   if content:
                       print(content, end="")
               print("\n")  # New line after response

           except Exception as e:
               print(f"An error occurred: {str(e)}\n")


def AI_cli(model_id=None, temperature=1, reasoning_effort=None, supports_reasoning=None):
    try:
        ai = Main()
        if model_id:
            ai.model_id_ini = model_id
        # print(f"Using model: {ai.model_id_ini}")

        # Determine if reasoning is supported if not explicitly provided
        if supports_reasoning is None:
            supports_reasoning = "reasoning" in ai.model_id_ini.lower()

        # Use provided reasoning_effort or fallback to default
        effective_reasoning_effort = reasoning_effort if reasoning_effort is not None else ai.default_reasoning_effort
        # print(f"reasoning_effort: {effective_reasoning_effort}\n")

        # Start the interactive session with the correct parameters
        ai.AI_run(reasoning_effort=effective_reasoning_effort, supports_reasoning=supports_reasoning)

    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please ensure your .env file contains API_KEY and MODEL_ID")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    AI_cli()
