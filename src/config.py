"""
config.py
Loads environment variables and creates the Groq LLM.

Also applies a compatibility fix for CrewAI's cache_breakpoint
when using Groq through LiteLLM.
"""

import os

from dotenv import load_dotenv
from crewai import LLM
import crewai.llms.cache as crewai_cache


# Load variables from .env
load_dotenv()


# ---------------------------------------------------------
# CrewAI + Groq compatibility fix
# ---------------------------------------------------------
#
# CrewAI can add a cache_breakpoint marker to messages.
# Groq does not accept this property in the request.
#
# For this project, we do not need CrewAI prompt caching.
# Therefore, prevent CrewAI from adding the marker.
#
crewai_cache.mark_cache_breakpoint = lambda message: message


# ---------------------------------------------------------
# Groq API key
# ---------------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Please add it to the .env file."
    )


# ---------------------------------------------------------
# Groq LLM
# ---------------------------------------------------------

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)