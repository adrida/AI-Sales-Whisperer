import numpy as np
import pandas as pd
from openai import OpenAI
import config 

client = OpenAI(api_key=config.OPENAI_API_KEY)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def _get_embedding(text, model="text-embedding-ada-002"):
    """
    Get the embedding for a given text using the specified model.
    Args:
    - text: The input text for which embedding needs to be retrieved.
    - model: The model to use for generating the text embedding.
    Returns:
    - The text embedding.
    """
    try:
        text = text.replace("\n", " ")
    except:
        None
    return client.embeddings.create(input = [text], model=model).data[0].embedding

def search_programs(user_input,nb_programs_to_display=10, path_to_csv = "data_planeta_july2023.csv",):
    user_input_real = user_input
    df = pd.read_csv(path_to_csv).dropna(subset=["Embeddings"])
    try:
        df["embeddings"] = df.Embeddings.apply(lambda x: x["Embeddings"])
    except:
        pass
    try:
        df["embeddings"] = df.Embeddings.apply(lambda x: np.array(eval(x)))
    except:
        pass
    embedding = _get_embedding(user_input_real, model='text-embedding-ada-002')
    try:
        df['similarity'] = df.Embeddings.apply(lambda x: cosine_similarity(eval(x), embedding))
    except:
        breakpoint()
    results = df.sort_values('similarity', ascending=False).head(int(nb_programs_to_display)).to_dict(orient="records")
    final_string = ""
    i = 1
    for result in results:
        similarity = str(round(result["similarity"]*100,2)) + "%"
        content = str(result["summary_french"])
        extracted_string_program = ""
        extracted_string_program += content.split("##")[1].split("\n\n")[0] + " (Compatibility: " + similarity +  ")\n\n"

        for sub_element in content.split("##")[2:]:
            extracted_string_program += sub_element
            
        extracted_string_program=extracted_string_program.replace("\n# ", "\n### ").replace("55555","###")
            
        displayed_string = "##"+extracted_string_program + "\n\n------\n\n"
        
        final_string += displayed_string
        i += 1
        # Add here openAI translate step
    return final_string
