import os
import pickle

from anki import hooks
import aqt
from aqt.qt import *


POP_EVERY_MS = 5 * 60 * 1000
SETTINGS_PATH = os.path.expanduser("~/.anki_autolearn.settings")


def save_settings(delay, path=SETTINGS_PATH):
    with open(path, 'wb') as fd:
        pickle.dump(delay, fd)


def load_settings(path=SETTINGS_PATH):
    if os.path.isfile(path):
        with open(path, 'rb') as fd:
            return pickle.load(fd)
    return POP_EVERY_MS


def hide_mw():
    aqt.mw.showMinimized()


def restore_mw():
    aqt.mw.showNormal()
    aqt.mw.activateWindow()
    aqt.mw.setFocus()


class Hook:
    def __init__(self, delay):
        self.delay = delay

    def __call__(self):
        hide_mw()
        QTimer.singleShot(self.delay, restore_mw)


class ScheduleDialog(QDialog):
    def __init__(self, mw, hook):
        super().__init__(mw)
        self.hook = hook

        layout = QFormLayout(self)

        self.spinMinutes = QSpinBox(self)
        self.spinSeconds = QSpinBox(self)
        self.okButton = QPushButton("OK")

        layout.addRow(QLabel("Minutes"), self.spinMinutes)
        layout.addRow(QLabel("Seconds"), self.spinSeconds)
        layout.addRow(self.okButton)

        self.spinMinutes.setValue(self.hook.delay // 60000)
        self.spinSeconds.setValue(self.hook.delay // 1000 % 60)
        self.okButton.clicked.connect(self.onOk)

        self.show()

    def onOk(self):
        minutes = self.spinMinutes.value()
        seconds = self.spinSeconds.value()
        self.hook.delay = (minutes * 60 + seconds) * 1000
        save_settings(self.hook.delay)
        self.close()


hook = Hook(load_settings())
hooks.addHook('cardAnswered', hook)

action = QAction("Autolearn schedule", aqt.mw)
action.triggered.connect(lambda: ScheduleDialog(aqt.mw, hook))
aqt.mw.form.menuTools.addAction(action)
