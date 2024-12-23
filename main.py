from pathlib import Path
import os

def create_package_structure(package_name):
    # Create main package directory
    os.makedirs(package_name, exist_ok=True)

    # Create package subdirectories
    Path(f"{package_name}/{package_name}").mkdir(exist_ok=True)
    Path(f"{package_name}/tests").mkdir(exist_ok=True)

    # Create necessary files
    files = {
        f"{package_name}/{package_name}/__init__.py": "",
        f"{package_name}/tests/__init__.py": "",
        f"{package_name}/setup.py": "",
        f"{package_name}/README.md": "",
        f"{package_name}/LICENSE": "",
        f"{package_name}/MANIFEST.in": "",
        f"{package_name}/requirements.txt": ""
    }

    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)

    print(f"Package structure created for '{package_name}'")

# Let's create a sample package
package_name = "loclx_colab"  # You can change this to your desired package name
create_package_structure(package_name)

# Created/Modified files during execution:
# my_package/
# ├── my_package/
# │   └── __init__.py
# ├── tests/
# │   └── __init__.py
# ├── setup.py
# ├── README.md
# ├── LICENSE
# ├── MANIFEST.in
# └── requirements.txt