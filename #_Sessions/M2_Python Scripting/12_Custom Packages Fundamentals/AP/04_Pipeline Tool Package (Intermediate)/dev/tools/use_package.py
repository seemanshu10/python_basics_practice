import sys
import os


pipelinetools_package_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(sys_path_pipelinetools)

sys.path.insert(0, pipelinetools_package_path)


# # import pipeline_tools

from pipeline_tools.project_config import (
    get_default_settings,
    validate_resolution,
    generate_report
)
 
pipeline_resolution_data = get_default_settings()
# # print(pipeline_resolution_data)
validate_resolution(pipeline_resolution_data[1])
generate_report(pipeline_resolution_data[0], pipeline_resolution_data[1], pipeline_resolution_data[2])