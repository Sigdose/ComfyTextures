import unreal
import os

# Debug
print('Hello from Unreal!')

# 현재 열려 있는 Content Browser의 경로 가져오기
content_browser_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()

print("DEBUG!!!! ", content_browser_path)
# 폴더 내부의 파일 목록 가져오기
files = os.listdir("D:/24_AI/StabilityMatrix-win-x64/Data/Packages/ComfyUI/output/TEST")
# OBJ 파일 찾기
obj_file = None
for file in files:
    if file.endswith('.obj'):
        obj_file = os.path.join("D:/24_AI/StabilityMatrix-win-x64/Data/Packages/ComfyUI/output/TEST", file)
        break

if obj_file:
    # OBJ 파일 가져오기
    import_task = unreal.AssetImportTask()
    import_task.set_editor_property("filename", obj_file)
    import_task.set_editor_property("destination_path", content_browser_path)
    import_task.set_editor_property("automated", True)
    import_task.set_editor_property("save", True)

    import_task.get_objects()

    # 가져온 객체의 경로 출력
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    asset = asset_tools.import_asset_tasks([import_task])

    if asset:
        print("Imported asset:", asset.get_full_name())
    else:
        print("Failed to import asset.")
else:
    print("OBJ 파일을 찾을 수 없습니다.")