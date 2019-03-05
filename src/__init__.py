from anki import hooks
import aqt
from aqt.qt import *


POP_EVERY_MS = 5 * 60 * 1000



def hide_mw():
    aqt.mw.showMinimized()


def restore_mw():
    aqt.mw.showNormal()
    aqt.mw.activateWindow()
    aqt.mw.setFocus()


class Hook:
    def __init__(self, delay=POP_EVERY_MS):
        self.delay = delay

    def __call__(self):
        hide_mw()
        QTimer.singleShot(self.delay, restore_mw)


class ScheduleDialog(QDialog):
    def __init__(self, mw):
        super().__init__(mw)

        layout = QFormLayout(self)

        self.spinMinutes = QSpinBox(self)
        self.spinSeconds = QSpinBox(self)
        self.okButton = QPushButton("OK")

        layout.addRow(QLabel("Minutes"), self.spinMinutes)
        layout.addRow(QLabel("Seconds"), self.spinSeconds)
        layout.addRow(self.okButton)

        self.spinMinutes.setValue(5)
        self.spinSeconds.setValue(0)
        self.okButton.clicked.connect(self.onOk)

        self.show()

    def onOk(self):
        minutes = self.spinMinutes.value()
        seconds = self.spinSeconds.value()
        setupHook((minutes * 60 + seconds) * 1000)
        print("Setup hook with", (minutes * 60 + seconds) * 1000, "ms")


hook = Hook()

hooks.addHook('cardAnswered', hook)


action = QAction("Autolearn schedule", aqt.mw)
action.triggered.connect(lambda: ScheduleDialog(aqt.mw))
aqt.mw.form.menuTools.addAction(action)


setupHook()
