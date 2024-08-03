from langchain_community.document_loaders import PyPDFLoader
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import json
import re

class Document(BaseModel):
    title: str = Field(description="Name of the Person")
    education: str = Field(description="Education of the Person (Exclude coursework and other irrelevant details)")
    experience: str = Field(description="Experience of the Person (Structure bullet points where applicable)")
    skills: List[str] = Field(description="Skill set of the Person")

parser = JsonOutputParser(pydantic_object=Document)

def load_pdf():
    loader = PyPDFLoader("resume.pdf")
    pages = loader.load()
    return pages

# Enhanced prompt with clear instructions
prompt_template =r"""
Task: You are an expert in analyzing resumes in PDF format. Your task is to carefully read the provided resume and extract the following key information into valid JSON format.

Instructions:
- For each section (title, education, experience, skills), extract the data exactly as presented.
- If any section is missing from the resume, leave the field empty in the JSON output.
- In the education section, exclude coursework and any irrelevant details.
- In the experience section, structure any bullet points as list items in the JSON.
- Ensure the JSON output is clean, well-formatted, and free of special characters like `\n` and `\u`.

Additional Notes:
- Use the format exactly as shown in the example.
- Maintain the order of the fields as presented in the example.
- Handle missing sections by leaving those fields as empty arrays or strings in the JSON.
- Make sure to extract the information accurately and exclude any unnecessary details.\n{format_instructions}\n{context}
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

llm = ChatGroq(api_key="GROQ_API_KEY")

pages = load_pdf()
chain = prompt | llm | parser

response = chain.invoke({
    "context": pages
})

def clean_text(text):
    text = text.encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'Relevant Coursework:.*', '', text)
    return text

response['education'] = clean_text(response.get('education', ''))
response['experience'] = clean_text(response.get('experience', ''))

formatted_response = json.dumps(response, indent=4)
print(formatted_response)

with open("output.json", "w") as json_file:
    json_file.write(formatted_response)
