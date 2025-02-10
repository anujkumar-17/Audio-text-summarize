from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool
from pathlib import Path

# Get the absolute path of the project directory
BASE_DIR = Path(__file__).parent.resolve()

# Define full paths for files
file_writer_tool_summary = FileWriterTool(
    file_name='summary.txt',
    directory=str(BASE_DIR / 'audio_to_text_translator')
)

file_writer_tool_action_items = FileWriterTool(
    file_name='action_items.txt',
    directory=str(BASE_DIR / 'audio_to_text_translator')
)

file_writer_tool_sentiment = FileWriterTool(
    file_name='sentiment.txt',
    directory=str(BASE_DIR / 'audio_to_text_translator')
)
# file_writer_tool_summary = FileWriterTool(file_name='summary.txt', directory='audio_to_text_translator')
# file_writer_tool_action_items = FileWriterTool(file_name='action_items.txt', directory='audio_to_text_translator')
# file_writer_tool_sentiment = FileWriterTool(file_name='sentiment.txt', directory='audio_to_text_translator')

@CrewBase
class AudioTextTranslatorCrew():
	"""Audio Text Translator Crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def audio_to_text_translator_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['audio_to_text_translator_summarizer'],
			tools=[file_writer_tool_summary, file_writer_tool_action_items, file_writer_tool_sentiment],
		)
	
	@agent
	def audio_to_text_translator_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['audio_to_text_translator_writer'],
		)

	@task
	def audio_to_text_translator_summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['audio_to_text_translator_summary_task'],
		)

	@task
	def audio_to_text_translator_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['audio_to_text_translator_writing_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Research Crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)