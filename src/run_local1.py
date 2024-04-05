from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import CTransformers
from src.helper import *

#Define Instruction token and System Token
B_INST ,E_INST = "[INST]","[/INST]"
B_SYS,E_SYS = "<<SYS>>\n","\n<</SYS>>\n\n"

instruction = "Convert the following text from English to Hindi: \n\n {text}"

# Taking Custom_System_Prompt instead of Default System_Prompt :

SYST_PROMPT = B_SYS + CUSTOM_SYSTEM_PROMPT + E_SYS
template = B_INST + SYST_PROMPT + instruction + E_INST

prompt = PromptTemplate(template= template,input_variables=["text"] )

llm = CTransformers(model='model\llama-2-7b-chat.ggmlv3.q4_0.bin',
                    model_type='llama',
                    config={'max_new_tokens':128,
                            'temperature':0.01}
                            )

LLM_Chain=LLMChain(prompt=prompt, llm=llm)

print(LLM_Chain.run("How are you?"))