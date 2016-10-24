paths = [
    '2298276436_224766aeb3_b',
    '2723419631_e43d602038_b',
    '2428331013_075f888875_b'
]
methods = [
    'dcnn',
    'global',
    'comprehensive',
    'knn',
    'learning',
    'close-form',
    'shared'
]

inputfile = open('hit.input', 'w+')
inputfile.write('vid\n')
for path in paths:
    for method in methods:
        inputfile.write('%s/,%s\n'%(path, method))
inputfile.close()
