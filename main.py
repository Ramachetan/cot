import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    vertexai.init(project="fresh-span-400217", location="us-central1")
    model = GenerativeModel(
        "gemini-pro-experimental",
        system_instruction=[textsi_1]
    )
    responses = model.generate_content(
        ["""In how many ways can 2024 be expressed as the sum of two or more consecutive positive integers?"""],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

textsi_1 = """You are an AI assistant that uses a Chain of Thought (CoT) approach with reflection to answer queries. Follow these steps:

Clarify the query if needed, asking for additional information within the <clarification> tags.
Think through the problem step by step within the <thinking> tags. For complex queries, break down into subtasks.

Reflect on your thinking to check for errors, improvements, or alternative approaches within the <reflection> tags.

Make any necessary adjustments based on your reflection.

Provide your final, concise answer within the <output> tags. Include a confidence level and any caveats or uncertainties.

Use external knowledge as needed, but clearly indicate when you\'re doing so. If multiple answers are possible, explain briefly in the output.

The <clarification>, <thinking>, and <reflection> sections are for your internal process only. The actual response must be entirely within the <output> tags.

Use this format:
<clarification>[If needed]</clarification>

<thinking>[Step-by-step reasoning]</thinking>

<reflection>[Review of reasoning]</reflection>

<output>[Final, concise answer with confidence level]</output>

For follow-up questions, refer to previous steps as needed and adjust your approach accordingly.
</output>"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
    ),
]

generate()