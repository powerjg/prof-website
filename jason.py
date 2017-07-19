
import sys
sys.path.append('..')

from cvcreator import *

from datetime import date

website = Website('Jason\'s Website')

from pubs import all_pubs
from presentations import presentations

website.add_section(all_pubs)

website.add_section(presentations)

website.export('output')
