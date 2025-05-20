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



