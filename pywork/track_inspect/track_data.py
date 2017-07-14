import scipy.io as sio


'''
sio.loadmat
sio.savemat
sio.whosmat
'''


mat_contents = sio.loadmat('baseline_wacv.mat')

print(mat_contents)

for k,v in mat_contents:
    if k == 'a':
        continue
    print(k, ': ', v)