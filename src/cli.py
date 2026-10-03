"""
cli.py
Simple command-line interface for the support-ticket triage system.
"""

from src.crew import create_support_crew


def run_cli():
    print("=" * 60)
    print("       SUPPORT TICKET TRIAGE - MULTI-AGENT SYSTEM")
    print("=" * 60)

    print("\nEnter a customer support ticket.")
    print("Type 'exit' to quit.\n")

    while True:
        ticket = input("Customer Ticket: ").strip()

        if ticket.lower() == "exit":
            print("\nGoodbye!")
            break

        if not ticket:
            print("Please enter a support ticket.\n")
            continue

        print("\n" + "=" * 60)
        print("STARTING MULTI-AGENT WORKFLOW")
        print("=" * 60)

        try:
            crew = create_support_crew(ticket)

            result = crew.kickoff()

            print("\n" + "=" * 60)
            print("FINAL CUSTOMER RESPONSE")
            print("=" * 60)
            print(result)

        except Exception as error:
            print("\nAn error occurred:")
            print(error)

        print("\n" + "-" * 60 + "\n")