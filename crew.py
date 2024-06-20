from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task


crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  
)


result=crew.kickoff(inputs={'topic':'AI Agents'})
print(result)