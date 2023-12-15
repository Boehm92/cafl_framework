import os

class BinvoxConverter:
    def __init__(self, directory):
        self.directory = directory

    def create_file(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        target_dir = os.path.join(script_dir, os.getenv(self.directory))
        os.chdir(target_dir)
        _dir_list = os.listdir()

        for file in _dir_list:
            if file.endswith('.stl'):
                # Binvox-Befehl mit angepassten Pfaden
                # binvox_command = f"binvox -d 64 -c -t binvox {file}"
                binvox_command = f"binvox -cb -mb -e -d 64 binvox {file}"
                os.system(binvox_command)

        # Optional: Wechsle zurück zum ursprünglichen Verzeichnis
        os.chdir(script_dir)

if __name__ == '__main__':
    BinvoxConverter("TRAINING_DATASET_SOURCE").create_file()


