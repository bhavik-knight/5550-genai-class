#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from market_research_assignment.crew import MarketResearchAssignment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    print("Welcome to the Market Research Crew!")
    print("Please select the companies you want to research from the list below:")
    
    companies = [
        "stripe.com",
        "espncricinfo.com",
        "olympics.com",
        "imdb.com",
        "ibm.com"
    ]
    
    for i, company in enumerate(companies, 1):
        print(f"{i}) {company}")
        
    try:
        user_input = input("Enter the number of the company you want to research: ")
        selected_index = int(str.strip(user_input))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    if 1 <= selected_index <= len(companies):
        selected_domain = companies[selected_index - 1]
    else:
        print(f"Invalid choice. Please select a number between 1 and {len(companies)}.")
        return

    print(f"\nProcessing research for: {selected_domain}")
    inputs = {
        'company_domain': selected_domain,
        'current_year': str(datetime.now().year)
    }

    try:
        MarketResearchAssignment().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew for {selected_domain}: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        MarketResearchAssignment().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MarketResearchAssignment().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        MarketResearchAssignment().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = MarketResearchAssignment().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
