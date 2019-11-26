# Ophiuchus-Demo
Demo stack/site using [Ophiuchus](https://github.com/brwyatt/Ophiuchus)

**NOTE: This project (and, more importantly, it's parent project, [Ophiuchus](https://github.com/brwyatt/Ophiuchus)) is currently under heavy development and should be considered experimental**

## Development

### Setup

1. Create Python Virtual Environment
   `python3 -m venv env`
2. Activate Python Virtual Environment
   `source env/bin/activate`
3. Install for development
   `pip3 install -r requirements-dev.txt`
4. Install pre-commit hooks:
   `pre-commit install`

### Development

Existing Handlers can be updated and changes will be included next time the
site is build or run, as long as the module is installed in editable mode
(which it will be if installed via `requirements-dev.txt`). New Handlers will
require a re-install of the module (`pip3 install -e .`) in order to pick up
the new entry\_points.

### Running locally

To run the site locally (for testing), within the virtual environment, run
`ophiuchus runlocal <ENTRY_POINT_GROUP>` with the name of the entry\_point
group for your site. More than one group may be passed at a time and will
be assigned sequential port numbers, and each endpoint will be provided in a
config object provided to each handler.
