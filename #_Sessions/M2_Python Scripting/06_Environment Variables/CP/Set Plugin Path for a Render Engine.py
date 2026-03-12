import os 

os.environ['RENDER_PLUGIN_PATH'] = 'z:/StudionTools/RenderEnginePlugins'

plugin_path = os.getenv('RENDER_PLUGIN_PATH')
print(f'Render Plugin Path: {plugin_path} ')