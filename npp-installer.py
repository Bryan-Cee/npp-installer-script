import os
from pywinauto.application import Application
import time


def download_npp():
    if os.path.exists("npp-installer"):
        print("Deleting previous downloaded installer")
        os.system("rmdir npp-installer /S /Q")
        print("\nDownloading the installer\n")
        os.system("git clone https://github.com/Bryan-Cee/npp-installer.git")
    else:
        print("\nDownloading the installer\n")
        os.system("git clone https://github.com/Bryan-Cee/npp-installer.git")


def run_installer():
    print("\nRunning the exe file\n")
    os.system("start .\\npp-installer\\npp.7.7.Installer.exe")
    time.sleep(3)


def install_npp():
    print("Selecting the dialog box\n")
    app = Application().connect(title='Installer Language')

    ctrl = app["Installer Language"]
    print("Clicking the OK button\n")
    ctrl.OK.click()

    ctrl = app["Notepad++ v7.7 Setup"]

    print("Clicking the Next button\n")
    ctrl.Next.click()

    print("Clicking the `I Agree` button\n")
    ctrl.IAgree.click()

    time.sleep(1)

    print("Clicking the Next button\n")
    ctrl.Next.click()

    print("Clicking the Next button\n")
    ctrl.Next.click()

    print("Clicking the Install button\n")
    ctrl.Install.click()

    print("Clicking the Finish button\n")
    ctrl.Finish.click()

    print("Installation finished")


if __name__ == '__main__':
    download_npp()
    run_installer()
    install_npp()
