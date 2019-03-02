from anki import hooks
import aqt
from aqt.qt import *


POP_EVERY_MIN = 5



def hide_mw():
    aqt.mw.showMinimized()


def restore_mw():
    aqt.mw.showNormal()
    aqt.mw.activateWindow()
    aqt.mw.setFocus()


def hook():
    hide_mw()
    QTimer.singleShot(POP_EVERY_MIN * 60000, restore_mw)


hooks.addHook('cardAnswered', hook)




class ScheduleDialog(QDialog):
    def __init__(self, mw):
        super().__init__(mw)
        self.show()


action = QAction("Autolearn schedule", aqt.mw)
action.triggered.connect(lambda: ScheduleDialog(aqt.mw))
aqt.mw.form.menuTools.addAction(action)
