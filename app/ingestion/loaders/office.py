
import os
import logfire

from unstructured.partition.docx import partition_docx
from unstructured.partition.pptx import partition_pptx


def parse_office(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    with logfire.span("Office Document Parsing", filename=file_path):

        print(f"Parsing {file_path}", flush=True)

        if ext == ".docx":
            elements = partition_docx(filename=file_path)

        elif ext == ".pptx":
            elements = partition_pptx(filename=file_path)

        else:
            raise ValueError(f"Unsupported Office format: {ext}")

        full_text = "\n".join(str(element) for element in elements)

        print(
            f"Extracted {len(full_text)} characters from {file_path}",
            flush=True
        )

        return full_text
