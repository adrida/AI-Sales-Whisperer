import config
import openai
import schedule
import time
from openai import OpenAI

client = OpenAI(api_key=config.OPENAI_API_KEY)


def generate_gpt():
    with open('transcriptions/transcript.txt') as f:
        text = f.read()
        instructions = config.PROMPT_INSTRUCTIONS
        prompt = f"""
        {text}
        {config.PROMPT_OUTPUT_FORMAT}
        """
        engine = config.LLM_MODEL

        retry = True

        while retry:
            try:
                response = client.chat.completions.create(
                model=engine,
                temperature=0.7,
                max_tokens = 800,
                messages=[
                        {"role": "system", "content": instructions},
                        {"role": "user", "content": prompt},
                    ],
                ).choices[0].message.content

                try:
                    print(response.strip())
                except Exception as e:
                    print(f"error parsing response from OpenAI {e}")
                insights = response.strip()
                retry = False
            
            except Exception as e:
                raise(e)
        with open("status_content.txt", 'w') as f1:
            f1.write(insights)
        f1.close()
    
    

def execute_generate_gpt():
    print("Generating full report and analysis of the current conversation...")
    generate_gpt()

print("Starting background generator! Welcome!")
schedule.every(20).seconds.do(execute_generate_gpt)

while True:
    schedule.run_pending()
    time.sleep(1)