import sys
from PyQt5.QtWidgets import QApplication
from load.load_proyecto import Biblioteca


def main():
   app = QApplication(sys.argv)
   menu = Biblioteca()
   menu.show()
   sys.exit(app.exec_())


if __name__ == "__main__":
    main()