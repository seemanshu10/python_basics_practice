# AssetPublisher

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/github/license/yourstudio/AssetPublisher)
![Build](https://img.shields.io/github/actions/workflow/status/yourstudio/AssetPublisher/build.yml)

AssetPublisher is a Python-based tool designed for VFX pipelines to help artists and TDs publish assets (models, rigs, animations) into the studio’s shared environment.  
It handles versioning, file validation, and automatic structure creation.


## ✨ Features

- Auto-versioning of published files  
- Ensures naming convention compliance  
- Generates metadata for pipeline tracking  
- Supports Maya, Houdini, and Nuke outputs  
- Logs every publish action for auditing



## Requirements
- Python 3.8+
- Maya 2022+
- PySide2
- requests, pyyaml


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourstudio/AssetPublisher.git
   cd AssetPublisher
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add the path to your pipeline environment:
   ```bash
   export PYTHONPATH=$PYTHONPATH:/path/to/AssetPublisher
   ```


## Usage
Run from the terminal or shelf button inside Maya:
```bash
python asset_publisher.py --asset "hero_rig" --type rig --user "alex"
```

Or from Python directly:
```python
from asset_publisher import publish

publish(asset_name="hero_rig", asset_type="rig", user="alex")
```

### Optional Flags
* `--dry-run` : Test publish without writing files
* `--note "Fixing eye blink bug"` : Add a change note


### Folder Structure
```
AssetPublisher/
├── asset_publisher/
│ ├── init.py
│ ├── core.py
│ └── ui.py
├── tests/
│ └── test_core.py
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for details.


## Contributors

- Alex Rivera — Pipeline TD  
- Jamie Lee — Rigging Lead  
- Priya Kaur — Developer


## Contact / Support

For support or bug reports, open an issue on GitHub or contact:  
pipeline-support@yourstudio.com


## Changelog

### [v1.2.0] - 2025-07-10
- Added support for Houdini .hip publishes  
- Improved validation error reporting

### [v1.0.0] - 2025-06-01
- Initial release with Maya support


## Screenshots

![UI Screenshot](docs/images/ui_main.png)  
*Main publishing UI inside Maya*


## Roadmap

- [x] Maya support  
- [ ] Add Blender export compatibility  
- [ ] Auto-publish from render farm  
- [ ] User-based access control