from cvcreator import *

from datetime import date

presentations = Section('Presentations', PresenationItem)

presentations.add_item(shortname = 'learning_gem5_tutorial',
    title = 'Tutorial Organizer for Learning gem5 at HPCA 2017',
    url = 'http://learning.gem5.org/tutorial/',
    authors = [
        'Jason Lowe-Power',
    ],
    date = date(2017, 2, 1),
    location = 'Learning gem5 Tutorial held in conjuntion with HPCA 2017',
    other_links = [
        Link("http://learning.gem5.org/tutorial/",
             'Tutorial page'),
        Link('http://learning.gem5.org/',
             'Learning gem5 project'),
        Link('https://www.youtube.com/watch?v=5UT41VsGTsg&list=PL-J9GXT0E7AIidmX_DW7pooRJzjoaJtix',
             'Youtube playlist of presentations'),
    ]
)

presentations.add_item(shortname = 'ibm_talk',
    title = 'Programmable Accelerators',
    authors = [
        'Jason Lowe-Power',
    ],
    date = date(2017, 2, 1),
    location = Link('http://researcher.watson.ibm.com/researcher/view_group.php?id=7424',
                    '2016 IBM Research Workshop on Architectures for Cognitive Computing and Datacenters'),
    other_links = [
        Link("http://cs.wisc.edu/~powerjg/files/ibm-workshop-programmable-accelerators-for-pdf.pdf",
             'Presentation PDF'),
        Link('http://cs.wisc.edu/~powerjg/files/ibm-workshop-programmable-accelerators.pptx',
             'Presentation PPTX'),
    ],
    isInvited = True
)

presentations.add_item(shortname = 'gem5_horrors',
    title = 'Little Shop of gem5 Horrors',
    authors = [
        'Jason Lowe-Power',
    ],
    date = date(2015, 6, 1),
    location = 'Second gem5 Users Workshop with ISCA 42',
    other_links = [
        Link("https://docs.google.com/presentation/d/1QGA5UVaVJkkMITF2TXCY_KlwmfWef1KBzfDP6ocbj7I/pub?start=false&loop=false&delayms=3000",
             'Presentation'),
        Link('http://www.lowepower.com/jason/gem5-horrors-and-what-we-can-do-about-it.html',
             'Blog post'),
    ]
)

presentations.add_item(shortname = 'gpu_analytic_dbs',
    title = 'The Benefits of GPUs for Analytic Processing - Today and Tomorrow',
    authors = [
        'Jason Lowe-Power',
        'Yinan Li',
        'Jignesh M. Patel',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2015, 6, 1),
    location = 'Google Madison',
    other_links = [
        Link("https://docs.google.com/presentation/d/1ma-MYhqTX8qk7AFUyVLlSBEOlmEnKw0hky92yN2TZKw/pub?start=false&loop=false&delayms=3000",
             'Presentation'),
    ],
    isInvited = True
)

presentations.add_item(shortname = 'gpu_mmu_amd',
    title = 'Supporting x86-64 Address Translation for 100s of GPU Lanes',
    authors = [
        'Jason Lowe-Power',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2014, 2, 1),
    location = 'AMD Research',
    other_links = [
        Link("http://cs.wisc.edu/~powerjg/files/amd-gpummu-presentation.pptx",
             'Presentation'),
    ],
    isInvited = True
)

presentations.add_item(shortname = 'gem5-gpy_pres',
    title = 'gem5-gpu: A Simulator for Heterogeneous Processors',
    authors = [
        'Jason Lowe-Power',
        'Marc S. Orr',
        'Joel Hestness',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2012, 12, 1),
    location = 'First Annual gem5 User Workshop with MICRO 45',
    other_links = [
        Link("http://gem5.org/wiki/images/7/7d/2012_12_gem5_gpu.pdf",
             'Presentation'),
    ]
)
