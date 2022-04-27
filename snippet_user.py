from emorynlp.EmoryExtractor import EmoryExtractor
from dailydialog.DailydialogExtractor import DailydialogExtractor
from reccon.RecconExtractor import RecconExtractor
from empathetic_dialogue.EmpDiaExtractor import EmpDiaExtractor

emory_extractor = EmoryExtractor()
emory_extractor.download_files()

daily_extractor = DailydialogExtractor()
daily_extractor.download_files()

reccon_extractor = RecconExtractor()
reccon_extractor.download_files()

empdia_extractor = EmpDiaExtractor()
empdia_extractor.download_files()