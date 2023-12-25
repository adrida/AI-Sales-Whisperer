
from get_similar_program import search_programs
import plotly.graph_objects as go
import re

def extract_float_from_string(string):
    pattern = r"[-+]?\d*\.\d+|\d+"
    match = re.search(pattern, string)
    if match:
        return float(match.group())
    else:
        return None

def generate_gauge_chart_and_markdown(input_string):

    probability_to_close = extract_float_from_string(input_string.split("\n--SEPARATION_ELMENTS--\n")[0].split("ELEMENT1:")[1])
    

    if probability_to_close >= 0.8:
        gauge_color = 'green'
    if probability_to_close >= 0.8:
        gauge_color = 'lightgreen'
    elif probability_to_close >= 0.5:
        gauge_color = 'yellow'
    elif probability_to_close >= 0.3:
        gauge_color = 'salmon'
    else:
        gauge_color = 'red'

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability_to_close * 100,
        title={'text': f"Closing Probability"},
        gauge={'axis': {'range': [None, 100]},
               'bar': {'color': gauge_color},
               'threshold':{'line': {'color': 'black', 'width': 6},
                   'thickness': 0.75, 'value': probability_to_close * 100}
               },
        number={'suffix': '%'},
        
    ))
    fig.update_layout(
        height=300
    )

    return fig


def get_insights():
    global last_occurrence
    with open('status_content.txt') as f:
                insights = f.read()
                sem_results = search_programs(insights, 10)
                results_query = "**Programs suggested by Sales Whisperer:** \n"+ sem_results
                fig = generate_gauge_chart_and_markdown(insights.replace('{\n','{').replace('\n}', '}').replace('\\','').replace('\n','').replace('\\n',''))
                try:
                    markdown_string = insights.split("ELEMENT2:\n")[1]
                except:
                    markdown_string = insights.split("ELEMENT2:")[1]
                    
    return fig, markdown_string.replace("ENDELEMENTS", ""), results_query.replace('\\n','\n')

