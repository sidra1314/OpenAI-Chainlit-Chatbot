# Gemini Chatbot using Chainlit and Gemini API

Ye project ek interactive chatbot banata hai jo Google Gemini API (model: `gemini-2.0-flash`) ka istemal karta hai. Chatbot Chainlit framework ke zariye asynchronous chat handle karta hai aur conversation ko local file mein save karta hai.

---

## Project Overview

- User se input leta hai aur Gemini language model ko prompt bhejta hai.
- Model ka response user ko chat interface mein dikhata hai.
- Puri conversation local JSON file mein save karta hai.
- Gemini API ko OpenAI style asynchronous client ke zariye integrate kiya gaya hai.

---

## Code Explanation

### Imports aur Setup

```python
import os
import json
import chainlit as cl
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel
