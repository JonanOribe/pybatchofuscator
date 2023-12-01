from src.batchofuscator import launch_batch_ofuscator
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
       print("No arguments were given")
    else:
        launch_batch_ofuscator(sys.argv)

