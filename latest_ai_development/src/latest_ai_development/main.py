#!/usr/bin/env python
import sys
import warnings
import argparse

from datetime import datetime

from latest_ai_development.crew import LatestAiDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with  task description.
    """

    task_description = input("enter the task description").strip() 
    inputs = {
        'task_description': task_description,
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        LatestAiDevelopment().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()