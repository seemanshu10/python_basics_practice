from core.loader import load_shots
from ui.main_ui import display_shots


def main():
    shots = load_shots()
    display_shots(shots)


if __name__ == "__main__":
    main()