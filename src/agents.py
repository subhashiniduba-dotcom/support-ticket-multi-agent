"""
agents.py
Defines the four specialized agents in the support-ticket workflow.
"""

from crewai import Agent

from src.config import llm


def create_classifier_agent():
    return Agent(
        role="Support Ticket Classifier",
        goal=(
            "Analyze incoming customer support tickets and identify "
            "their category, severity, and important details."
        ),
        backstory=(
            "You are an experienced support-ticket classification specialist. "
            "You carefully analyze customer issues and extract structured "
            "information. You never attempt to solve the customer's problem."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        cache=False
    )


def create_router_agent():
    return Agent(
        role="Support Ticket Router",
        goal=(
            "Determine which support department should handle the ticket "
            "and clearly explain the routing decision."
        ),
        backstory=(
            "You are a support operations specialist who routes customer "
            "issues to the correct department based on the ticket category, "
            "severity, and details."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        cache=False
    )


def create_response_drafter_agent():
    return Agent(
        role="Customer Response Drafter",
        goal=(
            "Create a professional, clear, and helpful response to the "
            "customer using the classification and routing information."
        ),
        backstory=(
            "You are an experienced customer support communication specialist. "
            "You write polite and professional responses without inventing "
            "information that is not present in the ticket."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        cache=False
    )


def create_quality_reviewer_agent():
    return Agent(
        role="Support Response Quality Reviewer",
        goal=(
            "Review the drafted customer response for accuracy, relevance, "
            "professional tone, and unsupported claims. Fix problems when needed."
        ),
        backstory=(
            "You are a quality assurance specialist for customer support. "
            "You carefully review responses before they are sent to customers."
        ),
        llm=llm,
        verbose=True,
        allow_delegation=False,
        cache=False
    )