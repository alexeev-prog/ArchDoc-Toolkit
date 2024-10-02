import os
from datetime import date
from abc import ABC, abstractmethod
from typing import Protocol, List, Callable, TypeVar, Generic, Dict, Any
from pycolor_palette_loguru.paint import (
	info_message,
	warn_message,
	error_message,
	other_message,
	debug_message,
	run_exception,
)


class Issue(Protocol):
	def get_id(self) -> str:
		return None

	def get_title(self) -> str:
		return None

	def get_description(self) -> str:
		return None

	def get_author(self) -> str:
		return None

	def get_type(self) -> str:
		return None

	def get_priority(self) -> int:
		return None

	def set_status(self, status: str) -> None:
		return None

	def get_status(self) -> int:
		return None


class DefaultIssue:
	def __init__(self, issue_id: str, title: str, description: str, author: str, issue_type: str, priority: int):
		self.id = issue_id
		self.title = title
		self.description = description
		self.author = author
		self.type = issue_type
		self.priority = priority
		self.status = "Open"

	def get_id(self) -> str:
		return self.id

	def get_title(self) -> str:
		return self.title

	def get_description(self) -> str:
		return self.description

	def get_author(self) -> str:
		return self.author

	def get_type(self) -> str:
		return self.type

	def get_priority(self) -> int:
		return self.priority

	def set_status(self, status: str) -> None:
		self.status = status

	def get_status(self) -> int:
		return self.status


class DocumentationGenerator(ABC):
	"""
	Abstract basic class for generators of docs sections
	"""

	@abstractmethod
	def generate_section(self) -> None:
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

	def generate_section(self) -> None:
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

	def generate_section(self) -> None:
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
				file.write(f'\n## Abbreviations\n')

				for abbreviation, desc in self.abbreviations.items():
					file.write(f' + **{abbreviation}**: {desc}\n')

			if len(self.defines) > 0:
				file.write(f'\n## Defines\n')

				for define, desc in self.defines.items():
					file.write(f' + **{define}**: {desc}\n')

		info_message(f"Template for '{self.section_name}' section generated successfully!")


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
			generator.generate_section()
			info_message(f'Generate section: {generator.section_name}')
