from re import I
import unreal
import os
def SD_function(input):
    obj_path = "D:/24_AI/StabilityMatrix-win-x64/Data/Packages/ComfyUI/output/"
    content_browser_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()
    files = os.listdir(obj_path)
    obj_file = None

    for file in files:
        if file.endswith('.obj'):
            print(type(input))
            if file.startswith(input):
                obj_file = os.path.join(obj_path, file)
                #break
                source_data = unreal.InterchangeManager.create_source_data(obj_file)

                import_asset_parameters = unreal.ImportAssetParameters()
                import_asset_parameters.is_automated = True

                eas = unreal.get_editor_subsystem(unreal.EditorAssetSubsystem)
                pipeline = eas.load_asset("/Interchange/Pipelines/CustomLSDAssetsPipeline")
                eas.save_loaded_asset(pipeline)
                #import_asset_parameters.override_pipelines.append(eas.load_asset("/Interchange/Pipelines/CustomLSDAssetsPipeline"))
                #import_asset_parameters.override_pipelines.append(eas.load_asset("/Game/DemoInterchange/DemoCustomChanges"))

                ic_mng = unreal.InterchangeManager.get_interchange_manager_scripted()
                ic_mng.import_asset("/game/interchange/obj/",source_data,import_asset_parameters)
                eas.save_loaded_asset(pipeline)