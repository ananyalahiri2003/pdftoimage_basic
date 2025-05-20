## Repo function
Run this on a directory with pdfs. 
 
For each pdf file in input_folder, it 
- creates a subdir in the output_folder 
- saves one image per page of the pdf in that subdirectory.  

## Setup

### Clone the repository
git clone git@github.com:ananyalahiri2003/pdftoimage_basic.git

cd src

### Install dependencies
poetry lock --no-update

poetry install

All dependencies in pyproject.toml file. 

### Run script
poetry shell

python src/app.py \
--input-folder {input_folder} \
--output-folder {output_folder}

### License
MIT License

### Future Plans
Please suggest away. This repo is a quick turnaround for a hackathon... ideas welcome. 



