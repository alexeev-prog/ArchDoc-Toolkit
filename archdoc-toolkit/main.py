
from archdoc_toolkit.documentation_generator import *


def main():
	PROJECT_NAME = "ArchDoc Toolkit"
	PROJECT_DESCRIPTION = 'A set of tools for creating and managing a project following the Architecture Document methodology'
	DOCUMENTATION_ROOT = 'app/docs'
	SECTION_NAMES = [
		"Introduction",
		"Architecture Overview",
		"Component Diagrams",
		"Deployment Diagram",
		"Key Architectural Decisions",
		"Abbreviations and Definitions"
	]

	doc_manager = DocumentationManager(PROJECT_NAME, PROJECT_DESCRIPTION, DOCUMENTATION_ROOT, SECTION_NAMES)

	doc_manager.initialize_project()
	doc_manager.update_table_of_contents()

	introduction_generator = IntroductionGenerator("Introduction", "An introduction to project", DOCUMENTATION_ROOT)
	doc_manager.register_section_generator(introduction_generator)

	abbranddef_generator = AbbrAndDefGenerator("Abbreviations and Definitions", "All definitions and abbreviations from the project", DOCUMENTATION_ROOT)
	abbranddef_generator.add_abbreviation('KISS', 'Keep It Simple, Stupid')
	abbranddef_generator.add_define("CMake", 'Crossplatform build system')
	doc_manager.register_section_generator(abbranddef_generator)

	project_manager = ProjectManager(PROJECT_NAME, DOCUMENTATION_ROOT, doc_manager)

	project_manager.add_module('data', "Module for data sets, settings and constants", ["data.py"])
	project_manager.add_module('documentation_generator', 'Module with docs generators and other managers', ["documentation_generator.py"])

	issue1 = DefaultIssue("1", "Improve documentation", "Add more details to the Architecture Overview section", "Jane Doe", "Enhancement", 2)
	issue2 = DefaultIssue("2", "Fix typo in README", "There is a typo in the project description", 'John Smith', 'Bug', 1)

	project_manager.add_issue(issue1)
	project_manager.add_issue(issue2)

	file_structure_gen = FileStructureGenerator(PROJECT_NAME, PROJECT_DESCRIPTION, 'app', 'alexeev-prog', 'ArchDoc-Toolkit', 'Apache License 2')

	project_manager.generate_project_structure(file_structure_gen, ['C++', 'Python'])
	project_manager.generate_documentation(doc_manager)

	project_manager.process_issues()


if __name__ == '__main__':
	main()
