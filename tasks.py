from crewai import Task
from tools import tool
from agents import blog_researcher,blog_writer


research_task = Task(
    description=(
        "Conduct thorough research on the topic '{topic}' using internet resources. "
        "Focus on gathering comprehensive details, including key points, statistics, and recent developments."
    ),
    expected_output=(
        "A detailed summary of findings including key points and insights on the topic '{topic}'."
    ),
    tools=[tool],
    agent=blog_researcher,
)


write_task = Task(
    description=(
        "Using the research summary, write an original blog post on the topic '{topic}'. "
        "Ensure the content is engaging, easy to understand, and paraphrases the information to avoid plagiarism."
    ),
    expected_output='A well-written blog post of approximately 800 words on the topic {topic}, formatted in markdown.',
    tools=[tool],
    agent=blog_writer,
    async_execution=False,
    output_file='blog-post.md'  
)