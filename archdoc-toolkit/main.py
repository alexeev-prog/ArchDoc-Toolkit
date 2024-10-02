from archdoc_toolkit.documentation_generator import DocumentationManager, IntroductionGenerator, AbbrAndDefGenerator

if __name__ == '__main__':
	PROJECT_NAME = "ArchDoc Toolkit"
	PROJECT_DESCRIPTION = 'A set of tools for creating and managing a project following the Architecture Document methodology'
	DOCUMENTATION_ROOT = 'docs'
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

	doc_manager.generate_sections()
