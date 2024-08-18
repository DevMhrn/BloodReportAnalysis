import os
from crewai import Crew, Process, Task, Agent
from agents import ReportReader_Agent, Analyzer_Agent, Recommendation_Agent
from tools import SerperDevTool, WebsiteSearchTool
from tasks import ReportReader_task, Analyze_blood_Sample_task, Find_articles_from_Web_task, Recommendation_task



crew = Crew(
    agents=[ReportReader_Agent, Analyzer_Agent, Recommendation_Agent],
    tasks=[ReportReader_task, Analyze_blood_Sample_task, Find_articles_from_Web_task, Recommendation_task],
    verbose=True
)

results = crew.kickoff()

# Convert results to a string
results_str = str(results)

# Define the file name with "Blood Report Analysis"
output_file = "Blood Report1.md"

# Write the results to the file
with open(output_file, "w") as file:
    file.write("# Blood_Report_Analysis \n\n")
    file.write(results_str)

print(f"Results have been written to {output_file}")