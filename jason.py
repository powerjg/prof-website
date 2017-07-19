
import sys
sys.path.append('..')

from cvcreator import *

from datetime import date

website = Website('Jason\'s Website')

from pubs import all_pubs

website.add_section(all_pubs)

website.export('output')
