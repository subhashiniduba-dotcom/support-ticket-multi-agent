"""
crew.py
Connects the four agents and their tasks into one sequential workflow.
"""

from crewai import Crew, Process

from src.agents import (
    create_classifier_agent,
    create_router_agent,
    create_response_drafter_agent,
    create_quality_reviewer_agent,
)

from src.tasks import (
    create_classification_task,
    create_routing_task,
    create_response_task,
    create_quality_task,
)


def create_support_crew(ticket: str):
    # Create the four specialized agents
    classifier = create_classifier_agent()
    router = create_router_agent()
    response_drafter = create_response_drafter_agent()
    quality_reviewer = create_quality_reviewer_agent()

    # Create the four tasks
    classification_task = create_classification_task(
        classifier,
        ticket
    )

    routing_task = create_routing_task(
        router,
        ticket
    )

    response_task = create_response_task(
        response_drafter,
        ticket
    )

    quality_task = create_quality_task(
        quality_reviewer,
        ticket
    )

    # Create the sequential multi-agent crew
    crew = Crew(
        agents=[
            classifier,
            router,
            response_drafter,
            quality_reviewer,
        ],
        tasks=[
            classification_task,
            routing_task,
            response_task,
            quality_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    return crew