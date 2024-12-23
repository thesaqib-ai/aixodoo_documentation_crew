from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CodeDocsSearchTool
from crewai import LLM

# Uncomment the following line to use an example of a custom tool
# from aixodoo.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class AixodooCrew():
	"""Aixodoo crew"""

	@agent
	def requirement_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['requirement_analyst'],
			verbose=True,
			respect_context_window = False,
			llm=LLM(
				model="gpt-4o",
				temperature=0.8,
				max_tokens=10000,
			),
		)

	@agent
	def odoo_studio_application_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['odoo_studio_application_specialist'],
			respect_context_window = False,
			llm=LLM(
				model="gpt-4o",
				temperature=0.8,
				max_tokens=10000,
			)
		)
	
	@task
	def requirement_analysis(self) -> Task:
		return Task(
			config=self.tasks_config['requirement_analysis'],
			output_file='Requirements Report.md'
		)

	@task
	def odoo_models_modules_apps_task(self) -> Task:
		return Task(
			config=self.tasks_config['odoo_models_modules_apps_task'],
			context=[self.requirement_analysis()],
			output_file='Odoo Models, Modules and Apps.md'
		)
	@task
	def odoo_view_task(self) -> Task:
		return Task(
			config=self.tasks_config['odoo_view_task'],
			context=[self.odoo_models_modules_apps_task()],
			output_file='Odoo Views.md'
		)
	@task
	def odoo_fields_and_widgets_task(self) -> Task:
		return Task(
			config=self.tasks_config['odoo_fields_and_widgets_task'],
			context=[self.odoo_view_task()],
			output_file='Odoo FIelds and Widgets.md'
		)
	@task
	def odoo_pdf_report_task(self) -> Task:
		return Task(
			config=self.tasks_config['odoo_pdf_report_task'],
			context=[self.odoo_fields_and_widgets_task()],
			output_file='Odoo PDF Report.md'
		)
	@task
	def odoo_automation_rules_task(self) -> Task:
		return Task(
			config=self.tasks_config['odoo_automation_rules_task'],
			context=[self.odoo_pdf_report_task()],
			output_file='Odoo Automation Rules.md'
		)
	@task
	def odoo_approval_rules_task(self) -> Task:
		return Task(
			config=self.tasks_config['odoo_approval_rules_task'],
			context=[self.odoo_automation_rules_task()],
			output_file='Odoo Approval Rules.md'
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the Aixodoo crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
