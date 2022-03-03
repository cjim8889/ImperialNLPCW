import numpy as np
from scipy import stats

def labels2file(p, outf_path, task2=False):
    if not task2:
        with open(outf_path,'w') as outf:
            for pi in p:
                outf.write(f"{pi}\n")


name = [1, 2, 3, 4, 5]

weight = np.array([80, 30, 50, 60, 60])
weight = weight / np.sum(weight)

print(weight)
output = []
for i in name:
    with open(f"task1 {i}.txt") as f:
        lines = f.readlines()

        lines = list(map(lambda x: int(x), lines))
        output.append(lines)

output = np.array(output)

print(output.shape)

mode = np.sum(output.T * weight, axis=1)

mode[mode >= 0.5] = 1
mode[mode < 0.5] = 0
# mode = stats.mode(output, axis=0)

labels2file(mode.astype(int), "task1.txt")

import zipfile
z = zipfile.ZipFile('submission.zip', 'w', zipfile.ZIP_DEFLATED)
z.write('task1.txt')
z.close()