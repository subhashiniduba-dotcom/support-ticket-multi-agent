"""
tasks.py
Defines the four tasks in the support-ticket workflow.
"""

from crewai import Task


def create_classification_task(agent, ticket):
    return Task(
        description=f"""
Analyze the following customer support ticket:

"{ticket}"

Identify:
1. Category of the issue
2. Severity level
3. Important details from the ticket

Do not solve the customer's problem.
Only classify and extract the important information.
""",
        expected_output="""
A clear classification containing:
- Category
- Severity
- Key details
""",
        agent=agent
    )


def create_routing_task(agent, ticket):
    return Task(
        description=f"""
Review the customer support ticket:

"{ticket}"

Using the classification provided by the previous agent, determine
which department should handle this ticket.

Possible departments include:
- Technical Support
- Billing
- Account Support
- Security
- General Support

Explain briefly why the selected department is appropriate.
Do not write a customer response.
""",
        expected_output="""
A clear routing decision containing:
- Department
- Reason for routing
""",
        agent=agent
    )


def create_response_task(agent, ticket):
    return Task(
        description=f"""
Create a professional customer support response for this ticket:

"{ticket}"

Use the classification and routing information from the previous agents.

The response should:
- Be polite and professional
- Directly address the customer's issue
- Be easy to understand
- Avoid inventing facts
- Avoid promising something that is not supported by the ticket

Write only the customer-facing response.
""",
        expected_output="""
A polished customer-facing support response.
""",
        agent=agent
    )


def create_quality_task(agent, ticket):
    return Task(
        description=f"""
Review the support response created for this customer ticket:

"{ticket}"

Check the response for:

1. Accuracy
2. Relevance
3. Professional tone
4. Clarity
5. Unsupported claims
6. Whether it actually addresses the customer's issue

If there are problems, correct them.

Return the final customer-facing response only.
""",
        expected_output="""
A final polished customer support response that is accurate,
relevant, professional, and free from unsupported claims.
""",
        agent=agent
    )