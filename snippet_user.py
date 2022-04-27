from emorynlp.EmoryExtractor import EmoryExtractor
from dailydialog.DailydialogExtractor import DailydialogExtractor
from meld.MeldExtractor import MeldExtractor
from reccon.RecconExtractor import RecconExtractor

emory_extractor = EmoryExtractor()
emory_extractor.download_files()

daily_extractor = DailydialogExtractor()
daily_extractor.download_files()

reccon_extractor = RecconExtractor()
reccon_extractor.download_files()