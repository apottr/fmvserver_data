from pathlib import Path
if __name__ == '__main__': 
    directory = Path(__file__).parent.resolve()
    print(directory)
