import sys
import os


pipelinetools_package_path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(sys_path_pipelinetools)

sys.path.append(pipelinetools_package_path)


# # import pipeline_tools

from pipeline_tools.project_config import report, settings, validator
 
pipeline_resolution_data = settings.project_settings()
# # print(pipeline_resolution_data)
validator.validator_function(pipeline_resolution_data[1])
report.reportGeneration(pipeline_resolution_data[0], pipeline_resolution_data[1], pipeline_resolution_data[2])