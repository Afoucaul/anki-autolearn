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
        self.close()


hook = Hook()
hooks.addHook('cardAnswered', hook)

action = QAction("Autolearn schedule", aqt.mw)
action.triggered.connect(lambda: ScheduleDialog(aqt.mw, hook))
aqt.mw.form.menuTools.addAction(action)
