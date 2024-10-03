import os
from datetime import date
from abc import ABC, abstractmethod
from typing import Protocol, List, Callable, Generic, Dict, Any, T
from pycolor_palette_loguru.paint import (
	info_message,
	warn_message,
	other_message,
	debug_message,
)

from archdoc_toolkit.data import CPP_GITIGNORE, PYTHON_GITIGNORE


class Issue(Protocol):
	"""
	This class describes an issue.
	"""
	def get_id(self) -> str:
		"""
		Gets the identifier.

		:returns:   The identifier.
		:rtype:     str
		"""
		return None

	def get_title(self) -> str:
		"""
		Gets the title.

		:returns:   The title.
		:rtype:     str
		"""
		return None

	def get_description(self) -> str:
		"""
		Gets the description.

		:returns:   The description.
		:rtype:     str
		"""
		return None

	def get_author(self) -> str:
		"""
		Gets the author.

		:returns:   The author.
		:rtype:     str
		"""
		return None

	def get_type(self) -> str:
		"""
		Gets the type.

		:returns:   The type.
		:rtype:     str
		"""
		return None

	def get_priority(self) -> int:
		"""
		Gets the priority.

		:returns:   The priority.
		:rtype:     int
		"""
		return None

	def set_status(self, status: str) -> None:
		"""
		Sets the status.

		:param      status:  The status
		:type       status:  str

		:returns:   None
		:rtype:     None
		"""
		return None

	def get_status(self) -> int:
		"""
		Gets the status.

		:returns:   The status.
		:rtype:     int
		"""
		return None


class DefaultIssue:
	"""
	This class describes a default issue.
	"""
	def __init__(self, issue_id: str, title: str, description: str, author: str, issue_type: str, priority: int):
		"""
		Constructs a new instance.

		:param      issue_id:     The issue identifier
		:type       issue_id:     str
		:param      title:        The title
		:type       title:        str
		:param      description:  The description
		:type       description:  str
		:param      author:       The author
		:type       author:       str
		:param      issue_type:   The issue type
		:type       issue_type:   str
		:param      priority:     The priority
		:type       priority:     int
		"""
		self.id = issue_id
		self.title = title
		self.description = description
		self.author = author
		self.type = issue_type
		self.priority = priority
		self.status = "Open"

	def get_id(self) -> str:
		"""
		Gets the identifier.

		:returns:   The identifier.
		:rtype:     str
		"""
		return self.id

	def get_title(self) -> str:
		"""
		Gets the title.

		:returns:   The title.
		:rtype:     str
		"""
		return self.title

	def get_description(self) -> str:
		"""
		Gets the description.

		:returns:   The description.
		:rtype:     str
		"""
		return self.description

	def get_author(self) -> str:
		"""
		Gets the author.

		:returns:   The author.
		:rtype:     str
		"""
		return self.author

	def get_type(self) -> str:
		"""
		Gets the type.

		:returns:   The type.
		:rtype:     str
		"""
		return self.type

	def get_priority(self) -> int:
		"""
		Gets the priority.

		:returns:   The priority.
		:rtype:     int
		"""
		return self.priority

	def set_status(self, status: str) -> None:
		"""
		Sets the status.

		:param      status:  The status
		:type       status:  str

		:returns:   None
		:rtype:     None
		"""
		self.status = status

	def get_status(self) -> int:
		"""
		Gets the status.

		:returns:   The status.
		:rtype:     int
		"""
		return self.status


class IssueManager(Generic[T]):
	"""
	This class describes an issue manager.
	"""
	def __init__(self) -> None:
		"""
		Constructs a new instance.
		"""
		self.issues: Dict[str, issue: T] = {}

	def add_issue(self, issue: T) -> None:
		"""
		Adds an issue.

		:param      issue:  The issue
		:type       issue:  T

		:returns:   None
		:rtype:     None
		"""
		info_message(f'New issue created: {issue.get_id()}')
		self.issues[issue.get_id()] = issue

	def update_issue(self, issue_id: str, updates: Dict[str, Any]) -> None:
		"""
		Update issue

		:param      issue_id:    The issue identifier
		:type       issue_id:    str
		:param      updates:     The updates
		:type       updates:     Dict[str, Any]

		:returns:   None
		:rtype:     None

		:raises     ValueError:  issue does not exist
		"""
		if issue_id in self.issues:
			issue = self.issues[issue_id]
			for key, value in updates.items():
				if hasattr(issue, key):
					setattr(issue, key, value)
					info_message(f'Issue "{issue_id}" has been updated')
		else:
			raise ValueError(f'Issue with ID "{issue_id}" does not exist.')

	def get_issue(self, issue_id: str) -> T:
		"""
		Gets the issue.

		:param      issue_id:    The issue identifier
		:type       issue_id:    str

		:returns:   The issue.
		:rtype:     T

		:raises     ValueError:  Issue does not exist
		"""
		if issue_id in self.issues:
			return self.issues[issue_id]
		else:
			raise ValueError(f'Issue with ID "{issue_id}" does not exist.')

	def process_issues(self) -> None:
		"""
		Process issues

		:returns:   None
		:rtype:     None
		"""
		print('-' * 40)
		debug_message('Process issues...')
		for issue in self.issues.values():
			other_message(f'Processing issue: {issue.get_title()}', "ISSUE")
			other_message(f'Description: {issue.get_description()}', "ISSUE")
			other_message(f'Author: {issue.get_author()}', "ISSUE")
			other_message(f'Type: {issue.get_type()}', "ISSUE")
			other_message(f'Priority: {issue.get_priority()}', "ISSUE")
			other_message(f'Status: {issue.get_status()}', "ISSUE")
			print('-' * 40)


class Module:
	"""
	This class describes a module.
	"""
	def __init__(self, name: str, description: str, files: List[str]):
		"""
		Constructs a new instance.

		:param      name:         The name
		:type       name:         str
		:param      description:  The description
		:type       description:  str
		:param      files:        The files
		:type       files:        List[str]
		"""
		self.name = name
		self.description = description
		self.files = files

	def get_name(self) -> str:
		"""
		Gets the name.

		:returns:   The name.
		:rtype:     str
		"""
		return self.name

	def get_description(self) -> str:
		"""
		Gets the description.

		:returns:   The description.
		:rtype:     str
		"""
		return self.description

	def get_files(self) -> List[str]:
		"""
		Gets the files.

		:returns:   The files.
		:rtype:     List[str]
		"""
		return self.files


class FileStructureGenerator:
	"""
	This class describes a file structure generator.
	"""

	def __init__(self, project_name: str, project_description: str, 
				root_dir: str, user: str, 
				repo_name: str, license: str):
		"""
		Constructs a new instance.

		:param      project_name:         The project name
		:type       project_name:         str
		:param      project_description:  The project description
		:type       project_description:  str
		:param      root_dir:             The root dir
		:type       root_dir:             str
		:param      user:                 The user
		:type       user:                 str
		:param      repo_name:            The repo name
		:type       repo_name:            str
		:param      license:              The license
		:type       license:              str
		"""
		self.project_name = project_name
		self.project_description = project_description
		self.root_dir = root_dir
		self.user = user
		self.repo_name = repo_name
		self.license = license

	def generate_gitignore(self, languages: List[str]):
		"""
		Generate .gitignore file

		:param      languages:  The languages
		:type       languages:  List[str]
		"""
		result_gitignore = ''

		for language in languages:
			if language.upper() == "PYTHON":
				result_gitignore += PYTHON_GITIGNORE
			elif language.upper() in ['C++', 'CPP', 'CXX']:
				result_gitignore += CPP_GITIGNORE
			else:
				warn_message(f'Language {language} is not supported.')

		gitignore_file = os.path.join(self.root_dir, '.gitignore')
		with open(gitignore_file, 'w') as file:
			file.write(result_gitignore)

		info_message('.gitignore file is generated')

	def generate_readme(self) -> None:
		"""
		Generate README.md file

		:returns:   None
		:rtype:     None
		"""
		readme_path = os.path.join(self.root_dir, 'README.md')

		lines = [
			f'# {self.project_name}\n',
			f'<p align="center">{self.project_description}</p>',
			'<br>',
			'<p align="center">'
			f'<img src="https://img.shields.io/github/languages/top/{self.user}/{self.repo_name}?style=for-the-badge">',
			f'<img src="https://img.shields.io/github/languages/count/{self.user}/{self.repo_name}?style=for-the-badge">',
			f'<img src="https://img.shields.io/github/stars/{self.user}/{self.repo_name}?style=for-the-badge">',
			f'<img src="https://img.shields.io/github/issues/{self.user}/{self.repo_name}?style=for-the-badge">',
			f'<img src="https://img.shields.io/github/last-commit/{self.user}/{self.repo_name}?style=for-the-badge">',
			'</p>\n\n'
			'> [!CAUTION]',
			f'> At the moment, {self.project_name} is under active development (alpha), many things may not work, and this version is not recommended for use (all at your own risk).\n',
			f'{self.project_description}\n',
			'> [!NOTE]',
			'> This project is generated by the [Architecture Document Toolkit](https://github.com/alexeev-prog/ArchDoc-Toolkit).\n',
			'## Copyright',
			f'ArchDoc-Toolkit is released under the {self.license}.\n',
			f'Copyright © 2024 {self.user}. All rights reversed.',
			f'\n---\n\n*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*'
		]

		with open(readme_path, 'w') as file:
			for line in lines:
				file.write(f'{line}\n')

		info_message('Readme file is generated')

	def generate_structure(self, docs_dir: str, modules: List[Module]) -> None:
		"""
		Generate project structure with modules

		:param      modules:  The modules
		:type       modules:  List[Module]

		:returns:   None
		:rtype:     None
		"""
		os.makedirs(docs_dir, exist_ok=True)

		for module in modules:
			module_dir = os.path.join(docs_dir, module.get_name())
			os.makedirs(module_dir, exist_ok=True)

			debug_message(f'Create project structure: module {module.get_name()}')

			for file_name in module.get_files():
				with open(os.path.join(module_dir, f'{file_name}_archdoc.md'), 'w') as f:
					f.write(f'# File: {file_name}\n')
					f.write(f'{module.get_description()}\n\n')
					f.write(f'*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*')

		info_message('Project structure generated successfully!')


class DocumentationGenerator(ABC):
	"""
	Abstract basic class for generators of docs sections
	"""

	@abstractmethod
	def generate_sections(self) -> None:
		"""Generate a template for current doc section"""
		info_message('Generate a section')


class IntroductionGenerator(DocumentationGenerator):
	"""
	This class describes an introduction generator.
	"""

	def __init__(self, section_name: str, description: str, doc_root: str):
		"""
		Constructs a new instance.

		:param      section_name:  The section name
		:type       section_name:  str
		:param      doc_root:      The document root
		:type       doc_root:      str
		"""
		self.section_name = section_name
		self.description = description
		self.doc_root = doc_root

	def generate_sections(self) -> None:
		"""
		Generate section

		:returns:   None
		:rtype:     None
		"""
		section_dir = os.path.join(self.doc_root, self.section_name.replace(" ", "_"))
		section_file = os.path.join(section_dir, f'{self.section_name.replace(" ", "_")}.md')

		with open(section_file, "w") as file:
			file.write(f"# {self.section_name}\n\n")
			file.write(f'*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
			file.write('Provide a comprehsive introduction to the project, including its purpose, key features and overall architecture.')
			file.write('\n\n---\n\n')
			file.write(f'{self.description}')

		info_message(f"Template for '{self.section_name}' section generated successfully!")


class AbbrAndDefGenerator(DocumentationGenerator):
	"""
	This class describes an abbr and definition generator.
	"""

	def __init__(self, section_name: str, description: str, doc_root: str):
		"""
		Constructs a new instance.

		:param      section_name:  The section name
		:type       section_name:  str
		:param      doc_root:      The document root
		:type       doc_root:      str
		"""
		self.section_name = section_name
		self.description = description
		self.doc_root = doc_root
		self.abbreviations = {}
		self.defines = {}

	def add_abbreviation(self, name: str, value: str) -> None:
		"""
		Adds an abbreviation.

		:param      name:   The name
		:type       name:   str
		:param      value:  The value
		:type       value:  str

		:returns:   None
		:rtype:     None
		"""
		self.abbreviations[name] = value

	def add_define(self, name: str, value: str) -> None:
		"""
		Adds a define.

		:param      name:   The name
		:type       name:   str
		:param      value:  The value
		:type       value:  str

		:returns:   None
		:rtype:     None
		"""
		self.defines[name] = value

	def generate_sections(self) -> None:
		"""
		Generate section

		:returns:   None
		:rtype:     None
		"""
		section_dir = os.path.join(self.doc_root, self.section_name.replace(" ", "_"))
		section_file = os.path.join(section_dir, f'{self.section_name.replace(" ", "_")}.md')

		with open(section_file, "w") as file:
			file.write(f"# {self.section_name}\n\n")
			file.write(f'*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*\n\n')
			file.write('Explains basic abbreviations, abbreviations and terms used in this project')
			file.write('\n\n---\n\n')
			file.write(f'{self.description}\n')

			if len(self.abbreviations) > 0:
				file.write('\n## Abbreviations\n')

				for abbreviation, desc in self.abbreviations.items():
					file.write(f' + **{abbreviation}**: {desc}\n')

			if len(self.defines) > 0:
				file.write('\n## Defines\n')

				for define, desc in self.defines.items():
					file.write(f' + **{define}**: {desc}\n')

		info_message(f"Template for '{self.section_name}' section generated successfully!")


class IssueDocumentationGenerator(DocumentationGenerator):
	"""
	This class describes an issue documentation generator.
	"""

	def __init__(self, issues: List[Issue], doc_root: str):
		"""
		Constructs a new instance.

		:param      issues:    The issues
		:type       issues:    list
		:param      doc_root:  The document root
		:type       doc_root:  str
		"""
		self.issues = issues
		self.doc_root = doc_root
		self.section_name = 'Issues'

	def generate_sections(self) -> None:
		"""
		Generate docs section

		:returns:   None
		:rtype:     None
		"""
		issues_dir = os.path.join(self.doc_root, "issues")
		os.makedirs(issues_dir, exist_ok=True)

		for issue in self.issues:
			issue_file = os.path.join(issues_dir, f'{issue.get_id()}_{issue.get_title().replace(" ", "_")}.md')
			with open(issue_file, "w") as f:
				f.write(f'# Issue ID: {issue.get_id()}\n')
				f.write(f'\n + Title: {issue.get_title()}\n')
				f.write(f'\n + description: {issue.get_description()}\n')
				f.write(f'\n + author: {issue.get_author()}\n')
				f.write(f'\n + type: {issue.get_type()}\n')
				f.write(f'\n + priority: {issue.get_priority()}\n')
				f.write(f'\n + status: {issue.get_status()}\n')
				f.write(f'\n\n*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*')
				f.write('\n')
			info_message(f'Documentation for issue "{issue.get_title()}" generated.')


class ModuleDocumentationGenerator(DocumentationGenerator):
	"""
	This class describes a module documentation generator.
	"""
	def __init__(self, modules: List[Module], doc_root: str):
		"""
		Constructs a new instance.

		:param      modules:   The modules
		:type       modules:   List[Module]
		:param      doc_root:  The document root
		:type       doc_root:  str
		"""
		self.modules = modules
		self.doc_root = doc_root

	def generate_sections(self) -> None:
		"""
		Generate sections

		:returns:   None
		:rtype:     None
		"""
		modules_dir = os.path.join(self.doc_root, "modules")
		os.makedirs(modules_dir, exist_ok=True)

		for module in self.modules:
			module_file = os.path.join(modules_dir, f"{module.get_name()}.md")
			with open(module_file, "w") as f:
				f.write(f'# Module: {module.get_name()}\n')
				f.write(f'## Description:\n{module.get_description()}\n')
				f.write('## Files:\n')
				for file in module.get_files():
					f.write(f' + {file}\n')

				f.write(f'\n\n*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*')

			info_message(f'Documentation for module "{module.get_name()}" generated.')


class DocumentationManager:
	"""
	This class describes a documentation manager.
	"""
	
	def __init__(self, project_name: str, project_description: str, doc_root: str, section_names: list[str]):
		"""
		Constructs a new instance.

		:param      project_name:         The project name
		:type       project_name:         str
		:param      project_description:  The project description
		:type       project_description:  str
		:param      doc_root:             The document root
		:type       doc_root:             str
		:param      section_names:        The section names
		:type       section_names:        list
		"""
		self.project_name = project_name
		self.project_description = project_description
		self.doc_root = doc_root
		self.section_names = section_names
		self.section_generators: list[DocumentationGenerator] = []

	def initialize_project(self) -> None:
		"""
		Initialize a new project, create needed project structure
		
		:returns:   None
		:rtype:     None
		"""
		if not os.path.exists(self.doc_root):
			os.makedirs(self.doc_root)

		for section_name in self.section_names:
			section_dir = os.path.join(self.doc_root, section_name.replace(" ", "_"))
			if not os.path.exists(section_dir):
				os.makedirs(section_dir)

		print(f"Project '{self.project_name} initialized successfully!'")

	def update_table_of_contents(self) -> None:
		"""
		Update table of contents

		:returns:   None
		:rtype:     None
		"""
		table_of_contents = "# Table of contents\n\n"

		for section_name in self.section_names:
			table_of_contents += f'- [{section_name}](./{section_name.replace(" ", "_")}/{section_name.replace(" ", "_")}.md)\n'

		with open(os.path.join(self.doc_root, "ArchDoc.md"), 'w') as file:
			file.write(table_of_contents)
			file.write('\n---\n\n')
			file.write(f'{self.project_description}')
			file.write(f'\n\n*Last updated: {date.today().strftime("%Y-%m-%d %H:%M:%S")}*')

		info_message('Table of contents updated successfully!')

	def register_section_generator(self, generator: DocumentationGenerator) -> None:
		"""
		Register new section generator

		:param      generator:  The generator
		:type       generator:  DocumentationGenerator

		:returns:   None
		:rtype:     None
		"""
		self.section_generators.append(generator)
		info_message(f'Register new section: {generator.section_name}')

	def generate_sections(self) -> None:
		"""
		Generate sections of docs

		:returns:   { description_of_the_return_value }
		:rtype:     None
		"""
		for generator in self.section_generators:
			generator.generate_sections()
			info_message(f'Generate section: {generator.section_name}')


class ProjectManager:
	"""
	This class describes a project manager.
	"""

	def __init__(self, project_name: str, documentation_root: str, documentation_manager: DocumentationManager):
		"""
		Constructs a new instance.
		
		:param      project_name:           The project name
		:type       project_name:           str
		:param      documentation_root:     The documentation root
		:type       documentation_root:     str
		:param      documentation_manager:  The documentation manager
		:type       documentation_manager:  DocumentationManager
		"""
		self.project_name = project_name
		self.documentation_manager = documentation_manager
		self.documentation_root = documentation_root
		self.code_modules: List[Module] = []
		self.build_hooks: List[Callable[[], None]] = []
		self.issue_manager = IssueManager[Issue]()

	def add_module(self, name: str, description: str, files: List[str]) -> None:
		"""
		Adds a module.

		:param      name:         The name
		:type       name:         str
		:param      description:  The description
		:type       description:  str
		:param      files:        The files
		:type       files:        List[str]

		:returns:   None
		:rtype:     None
		"""
		module = Module(name, description, files)
		self.code_modules.append(module)

	def generate_documentation(self, documentation_manager: DocumentationManager):
		"""
		{ function_description }

		:param      documentation_manager:  The documentation manager
		:type       documentation_manager:  DocumentationManager
		"""
		issue_gen = IssueDocumentationGenerator(list(self.issue_manager.issues.values()), self.documentation_root)
		module_gen = ModuleDocumentationGenerator(self.code_modules, self.documentation_root)

		issue_gen.generate_sections()
		module_gen.generate_sections()
		documentation_manager.generate_sections()

	def generate_project_structure(self, file_structure_gen, gitignore_languages: List[str]) -> None:
		"""
		{ function_description }

		:param      file_structure_gen:   The file structure generate
		:type       file_structure_gen:   FileStructureGenerator
		:param      gitignore_languages:  The gitignore languages
		:type       gitignore_languages:  List[str]

		:returns:   None
		:rtype:     None
		"""
		file_structure_gen.generate_structure(self.documentation_root, self.code_modules)
		file_structure_gen.generate_gitignore(gitignore_languages)
		file_structure_gen.generate_readme()

	def add_build_hook(self, hook: Callable[[], None]) -> None:
		"""
		Adds a build hook.

		:param      hook:  The hook
		:type       hook:  Callable[[], None]

		:returns:   None
		:rtype:     None
		"""
		self.build_hooks.append(hook)

	def add_issue(self, issue: Issue) -> None:
		"""
		Adds an issue.

		:param      issue:  The issue
		:type       issue:  Issue

		:returns:   None
		:rtype:     None
		"""
		self.issue_manager.add_issue(issue)

	def update_issue(self, issue_id: str, updates: Dict[str, Any]):
		"""
		Update issue

		:param      issue_id:  The issue identifier
		:type       issue_id:  str
		:param      updates:   The updates
		:type       updates:   Dict[str, any]
		"""
		self.issue_manager.update_issue(issue_id, updates)

	def get_issue(self, issue_id: str) -> Issue:
		"""
		Gets the issue.

		:param      issue_id:  The issue identifier
		:type       issue_id:  str

		:returns:   The issue.
		:rtype:     Issue
		"""
		return self.issue_manager.get_issue(issue_id)

	def build_project(self) -> None:
		"""
		Builds a project.

		:returns:   The project.
		:rtype:     None
		"""
		info_message(f'Building project "{self.project_name}...')

		for hook in self.build_hooks:
			debug_message(f'Execute hook: {hook.__name__}')
			hook()

		info_message("Project built successfully!")

	def process_issues(self) -> None:
		"""
		Process issues

		:returns:   None
		:rtype:     None
		"""
		self.issue_manager.process_issues()
