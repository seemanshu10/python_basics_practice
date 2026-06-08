class VFXAsset:

    def __init__(self, asset_name, asset_type, version):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.version = version


    def display_info(self):

        print(f"Asset Name: {self.asset_name}")
        print(f"Asset Type: {self.asset_type}")
        print(f"Version : {self.version}")
        print()

    def set_version(self, version):
        self.version = version
        print(f"Version updated to {version}")
        print()

    def publish(self, artist_name, department):
        print(f"Asset published by {artist_name} from {department} department")
        print()

    def export(self, format = "abc"):
        print(f"Asset exported in {format} format")
        print()

    def pipeline_note():
        print("All VFX assets must follow studio naming conventions.")
        print()

asset = VFXAsset("Dragon", "Character", 1)

asset.display_info()
asset.set_version(2)
asset.publish("Aman", "Modeling")
asset.export()
asset.export("fbx")
VFXAsset.pipeline_note()

# print(asset.__dict__)

asset1 = VFXAsset("Dog", "Character", 1)

asset1.display_info()
asset1.set_version(2)
asset1.publish("Alice", "Rigging")
asset1.export()
asset1.export("usd")
VFXAsset.pipeline_note()

"""
P/02_Vfx Asset Class L2/main.py"
Asset Name: Dragon
Asset Type: Character
Version : 1

Version updated to 2

Asset published by Aman from Modeling department

Asset exported in abc format

Asset exported in fbx format

Asset Name: Dog
Asset Type: Character
Version : 1

Version updated to 2

Asset published by Alice from Rigging department

Asset exported in abc format

Asset exported in usd format

"""