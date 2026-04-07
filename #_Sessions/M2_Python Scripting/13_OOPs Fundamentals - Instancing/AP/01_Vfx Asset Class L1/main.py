class VFXAsset:

    def display_info(self):

        self.asset_name = "DefaultAsset"
        self.asset_type = "Prop"
        self.version = 1

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

asset = VFXAsset()

asset.display_info()
asset.set_version(2)
asset.publish("Alice", "compositing")
asset.export()
asset.export("fbx")

"""
Asset Name: DefaultAsset
Asset Type: Prop
Version : 1

Version updated to 2

Asset published by Alice from compositing department

Asset exported in abc format
Asset exported in fbx format

"""