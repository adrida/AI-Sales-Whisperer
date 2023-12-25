OPENAI_API_KEY = "Paste your openAI API Key here - Follow the documentation here to https://platform.openai.com/docs/quickstart/account-setup"

TRANSCRIPT_FILE = "transcriptions/transcript.txt"

LLM_MODEL = "gpt-4"

COMMAND_WORD = "whisper"

PROMPT_INSTRUCTIONS = "You will receive each time a section of a transcription of a sales meeting (it might contain some transcription bugs). Your task is to provide two elements of two properly formatted markdown strings containing the following:\n\n\nELEMENT1:\n# A number representing simply a the probability to close the candidate based on the global feeling of how the meeting is going. (This field should only contain a number between 0 and 1)\n--SEPARATION_ELMENTS--\nELEMENT2:\n# A formatted Markdown string containing all the following elements but displayed in a proper and concise way for a sale to read during a meeting in real time (Find better suited names for each sub elements and make the markdown display clean and efficient - i.e. perfectly sized titles and effect on font - ):\n    'adjective' : # One or two words to describe the feeling of the candidate and the overall feeling of the meeting,\n    'candidate_summary' : # A summary of who the candidate is and what he is looking for. It should only contain efficient keywords, no sentences,\n    'status_prospect': #Here is the full markdown string describing as bullet points in a compact and concise way what is the status of the potential client and how close he is to being closed. All informations should be relevant for the sales person and help guide him without overwhelm him as we will read this during the sales meeting,\n    'arguments': #Here is the full markdown string describing as bullet points in a compact and concise way what arguments should the salesperson give to close the deal. It also contains actionable insights to drive the conversation. Again it should not overlead the coginitive perception of the sales.\nENDELEMENTS\n\nAll should follow exactly the asked format for elements. All bullet points will be displayed in real-time to the salesperson so they should not be overwhelming in terms of information and perfectly suited for a HUD."
PROMPT_OUTPUT_FORMAT = """
<END OF SECTION OF TRANSCRIPTION>
Two formated elements:
"""

QUERY_SYSTEM_PROMPT = "You will receive each time a section of a transcription of a sales meeting. Your task is to provide a NLP query to search through a semantic search tool in the company database for relevant programs for potential clients. This database contains a list of all programs throughout all schools so the search should be targeted.\nThe query should be very detailed to allow embeddings to match. \nIt will be pasted directly in the search bar so format it like that:\n\n{'query': Query here describing ALL of the potential client's needs,}"

PROMPT_CUSTOM_ARGUMENTS = "You will receive each time a summary section of a transcription of a sales meeting (it might contain some transcription bugs), and a list of products, one of them should be sold to the client no matter what. Your task is to provide a valid python dict for each product containing properly formatted markdown strings containing the following:\n\n{\n 'title' : # Key basic high level elements to know about the program (name, city, price etc). Keep it short in one line,\n   'arguments_to_push': # Keys elements to show the salesperson telling me what to do/say to close the deal and sell the product. It should contain key bullet points and be highly relevent and convincing for the client. For each arguments you write how efficient the argument will be in one word between parenthesis using the format of this example: (Efficacité: ++). More + means more efficient.\n}\nAll bullet points will be displayed in real-time to the salesperson so they should not be overwhelming in terms of information and perfectly suited for a HUD."

PROMPT_OUTPUT_QUERY_FORMAT = """
<END OF SECTION OF TRANSCRIPTION>
Query:
"""

PROMPT_OUTPUT_CUSTOM_FORMAT = """
<END OF INPUTS>
valid python dict:
"""