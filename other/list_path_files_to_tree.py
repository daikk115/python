import pprint
pp = pprint.PrettyPrinter(indent=4)

list_paths = [
"a/a.1/a.1.1/b.txt",
"a/a.2",
"a/a.3/c.txt",
"a/a.3/d.txt",
"a/a.1/b.txt",
"a/a.3"
]

def function(str):
    str_splits = str.split("/")
    str_splits = str_splits[::-1] # reverse list
    tmp_dist = {}
    for name in str_splits:
        if ".txt" in name:
            tmp_dist[name] = None
        else:
            tmp_dist2 = {}
            tmp_dist2[name] = tmp_dist
            tmp_dist = tmp_dist2
    return tmp_dist

def merge_dict(A, B):
    keyAs = A.keys()
    keyBs = B.keys()
    if(len(keyBs) != 0):
        keyB = B.keys()[0]
        if B[keyB] is None:
            A[keyB] = None
        else:
            if keyB in keyAs:
                merge_dict(A[keyB], B[keyB])
            else:
                A[keyB]=B[keyB]
    return A

result = {}

for path in list_paths:
    result = merge_dict(result, function(path))

pp.pprint(result)
print("Done!")

