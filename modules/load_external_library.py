import os
from homepagebuilder.interfaces.Events import on
from homepagebuilder.core.io import File
from homepagebuilder.core.project import Project

LIBRARIES_PATH = ['external_library']

@on("project.import.return")
def load_external_libraries(project:Project, *args, **kwargs):
    library_files = []
    for library_path in LIBRARIES_PATH:
        library_files.append(File(os.path.join(project.base_path, library_path, "__LIBRARY__.yml")))
    project.base_library.add_sub_libraries(library_files)
    print(f"Loaded external libraries from: {', '.join(LIBRARIES_PATH)}")
