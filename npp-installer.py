import os
import pywinauto
from pywinauto.application import Application
import time


def download_npp():
    print("\nDownloading the installer\n")
    os.system("git clone https://github.com/Bryan-Cee/npp-installer.git")


def run_installer():
    print("Running the exe file")
    os.system("cd npp-installer")
    os.system("start .\\npp-installer\\npp.7.7.Installer.exe")
    time.sleep(3)


def install_npp():
    app = Application().connect(title='Installer Language')

    ctrl = app["Installer Language"]
    ctrl.OK.click()

    ctrl = app["Notepad++ v7.7 Setup"]
    ctrl.Next.click()
    ctrl.IAgree.click()
    ctrl.Next.click()
    ctrl.Next.click()
    ctrl.Install.click()
    ctrl.Finish.click()


if __name__ == '__main__':
    download_npp()
    run_installer()
    install_npp()

