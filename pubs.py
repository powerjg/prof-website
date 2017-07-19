
from cvcreator import *

from datetime import date

all_pubs = Section('Publications', PublicationItem)

# These are my peer-reviewed publications
pubs = SubSection(all_pubs, '')

pubs.add_item(shortname = 'bpoe_3d_bandwidth_model',
    title = 'When to use 3D Die-Stacked Memory for Bandwidth-Constrained Big-Data Workloads',
    url = 'http://arxiv.org/abs/1608.07485',
    authors = [
        'Jason Lowe-Power',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2016, 4, 3),
    location = 'The Seventh Workshop on Big Data Benchmarks, Performance Optimization, and Emerging Hardware (BPOE 7) at ASPLOS',
    other_links = [
        Link("http://www.cs.wisc.edu/multifacet/papers/bpoe16_3d_bandwidth_model.pdf",
             'Local link to paper'),
        Link('http://www.cs.wisc.edu/multifacet/papers/bpoe16_3d_bandwidth_model_talk.pdf',
             'Presentation'),
        Link('http://www.lowepower.com/jason/when-to-use-3d-die-stacking-for-bandwidth-constrained-big-data-workloads.html',
             'Blog post'),
    ]
)

pubs.add_item(shortname = 'border_control',
    title = 'Border Control: Sandboxing Accelerators',
    url = 'http://dx.doi.org/10.1145/2830772.2830819',
    authors = [
        'Lena E. Olson',
        'Jason Power',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2015, 12, 1),
    location = 'Proceedings of the 48th Annual IEEE/ACM International Symposium on Microarchitecture, MICRO 48',
    other_links = [
        Link('http://www.cs.wisc.edu/multifacet/papers/micro15_border_control.pdf',
             'Local link to paper'),
    ]
)

pubs.add_item(shortname = 'gpu_scan_agg',
    title = 'Toward GPUs being mainstream in analytic processing: An initial argument using simple scan-aggregate queries',
    url = 'http://dx.doi.org/10.1145/2771937.2771941',
    authors = [
        'Jason Power',
        'Yinan Li',
        'Jignesh M. Patel',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2015, 6, 1),
    location = 'Proceedings of the Eleventh International Workshop on Data Management on New Hardware, DaMoN \'15',
    other_links = [
        Link('http://www.cs.wisc.edu/multifacet/papers/damon15_gpu_analytic_processing.pdf',
             'Local link to paper'),
        Link('http://www.cs.wisc.edu/multifacet/papers/damon15_gpu_analytic_processing_talk.pdf',
             'Presentation'),
        Link('http://www.lowepower.com/jason/when-to-use-3d-die-stacking-for-bandwidth-constrained-big-data-workloads.html',
             'Blog post'),
    ],
)

pubs.add_item(shortname = '3d_scan',
    title = 'Implications of Emerging 3D GPU Architecture on the Scan Primitive',
    url = 'http://dx.doi.org/10.1145/2783888.2783896',
    authors = [
        'Jason Power',
        'Yinan Li',
        'Jignesh M. Patel',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2015, 3, 1),
    location = 'SIGMOD Record. Volume 44, Issue 1',
    other_links = [
        Link('http://www.cs.wisc.edu/multifacet/papers/sigmodrecord15_3d_gpu_scan.pdf',
             'Local link to paper'),
    ],
)

pubs.add_item(shortname = 'gpummu',
    title = 'Supporting x86-64 Address Translation for 100s of GPU Lanes',
    url = 'http://dx.doi.org/10.1109/HPCA.2014.6835965',
    authors = [
        'Jason Power',
        'Mark D. Hill',
        'David A. Wood',
    ],
    date = date(2014, 2, 1),
    location = 'Proceedings of the 20th IEEE International Symposium On High Performance Computer Architecture, HPCA 20',
    other_links = [
        Link('http://www.cs.wisc.edu/multifacet/papers/hpca14_gpummu_appendix.pdf',
             'Local link to paper (with appendix)'),
        Link('http://www.cs.wisc.edu/multifacet/papers/hpca14_gpummu_presentation.pptx',
             'Presentation'),
        Link('http://research.cs.wisc.edu/multifacet/gpummu-hpca14/',
             'Data, code, and reproducability details')
    ],
)

pubs.add_item(shortname = 'HSC',
    title = 'Heterogeneous System Coherence for Integrated CPU-GPU Systems',
    url = 'http://dx.doi.org/10.1145/2540708.2540747',
    authors = [
        'Jason Power',
        'Arkaprava Basu',
        'Junli Gu',
        'Sooraj Puthoor',
        'Bradford M. Beckmann',
        'Mark D. Hill',
        'Steven K. Reinhardt',
        'David A. Wood',
    ],
    date = date(2013, 12, 1),
    location = 'Proceedings of the 46th Annual IEEE/ACM International Symposium on Microarchitecture, MICRO 46',
    other_links = [
        Link('http://www.cs.wisc.edu/multifacet/papers/micro13_hsc.pdf',
             'Local link to paper'),
        Link('http://www.cs.wisc.edu/~powerjg/files/micro13-hsc-presentation.pptx',
             'Presentation'),
        Link('http://www.cs.wisc.edu/~powerjg/files/micro13-hsc-poster.pptx',
             'Poster')
    ],
)

thesis = SubSection(all_pubs, 'Thesis')

thesis.add_item(shortname = 'thesis',
    title = 'On Heterogeneous Compute and Memory Systems',
    authors = [
        'Jason Lowe-Power',
    ],
    date = date(2017, 6, 1),
    other_links = [
        Link('http://research.cs.wisc.edu/multifacet/theses/jason_lowepower_phd.pdf',
             'PDF Link')
    ],
    url = 'http://research.cs.wisc.edu/multifacet/theses/jason_lowepower_phd.pdf',
    location = 'University of Wisconsin. PhD Thesis',
)

books = SubSection(all_pubs, 'Books')

books.add_item(shortname = 'learning_gem5',
    title = "Learning gem5",
    url = 'http://learning.gem5.org/book/',
    authors = ['Jason Lowe-Power'],
    other_links = [
        Link('https://www.youtube.com/watch?v=5UT41VsGTsg',
             'Youtube link for HPCA tutorial'),
        Link('https://github.com/powerjg/learning_gem5',
             'Project github page'),
    ],
    details = 'Open source online book aimed to familiarize new users with the gem5 architectural simulator. '
              'This is a current work-in-progress, so check back often for updates.',
)
