from langchain.llms import CTransformers
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from typing import Any, Dict, List, Union
import streamlit as st
model_id = 'TheBloke/Mistral-7B-codealpaca-lora-GGUF'
config = {'temperature': 0.7, 'context_length': 8000}
llm = CTransformers(model=model_id, model_type='mistral', config=config)
prompt = PromptTemplate.from_template("You have {ingredients}. Let me suggest a recipe for you.")
chain = LLMChain(llm=llm, prompt=prompt)
def generate_recipe(ingredients):
    prompt = f"You have {', '.join(ingredients)}. Let me suggest a recipe for you."
    response = chain.run(prompt)
    return response


