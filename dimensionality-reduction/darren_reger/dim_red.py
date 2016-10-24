import matplotlib.pyplot as plt
import scipy.misc
import numpy as np
from scipy.sparse.linalg import eigs

# c = scipy.misc.imread('clooney1.jpg')
# c = scipy.misc.imread('clooney1.jpg',flatten=True)
# plt.imshow(c)
# plt.show()

c1 = scipy.misc.imresize(scipy.misc.imread('clooney1.jpg',flatten=True),(120,80)).astype(float)
c2 = scipy.misc.imresize(scipy.misc.imread('clooney2.jpg',flatten=True),(120,80)).astype(float)
c3 = scipy.misc.imresize(scipy.misc.imread('clooney3.jpg',flatten=True),(120,80)).astype(float)
c4 = scipy.misc.imresize(scipy.misc.imread('clooney4.jpg',flatten=True),(120,80)).astype(float)
c5 = scipy.misc.imresize(scipy.misc.imread('clooney5.jpg',flatten=True),(120,80)).astype(float)
avg_clooney = (c1+c2+c3+c4+c5)/5.0

o1 = scipy.misc.imresize(scipy.misc.imread('obama1.jpg',flatten=True),(120,80)).astype(float)
o2 = scipy.misc.imresize(scipy.misc.imread('obama2.jpg',flatten=True),(120,80)).astype(float)
o3 = scipy.misc.imresize(scipy.misc.imread('obama3.jpg',flatten=True),(120,80)).astype(float)
o4 = scipy.misc.imresize(scipy.misc.imread('obama4.jpg',flatten=True),(120,80)).astype(float)
o5 = scipy.misc.imresize(scipy.misc.imread('obama5.jpg',flatten=True),(120,80)).astype(float)
avg_obama = (o1+o2+o3+o4+o5)/5.0

t1 = scipy.misc.imresize(scipy.misc.imread('trump1.jpg',flatten=True),(120,80)).astype(float)
t2 = scipy.misc.imresize(scipy.misc.imread('trump2.jpg',flatten=True),(120,80)).astype(float)
t3 = scipy.misc.imresize(scipy.misc.imread('trump3.jpg',flatten=True),(120,80)).astype(float)
t4 = scipy.misc.imresize(scipy.misc.imread('trump4.jpg',flatten=True),(120,80)).astype(float)
t5 = scipy.misc.imresize(scipy.misc.imread('trump5.jpg',flatten=True),(120,80)).astype(float)
avg_trump = (t1+t2+t3+t4+t5)/5.0

b1 = scipy.misc.imresize(scipy.misc.imread('bernie1.jpg',flatten=True),(120,80)).astype(float)
b2 = scipy.misc.imresize(scipy.misc.imread('bernie2.jpg',flatten=True),(120,80)).astype(float)
b3 = scipy.misc.imresize(scipy.misc.imread('bernie3.jpg',flatten=True),(120,80)).astype(float)
b4 = scipy.misc.imresize(scipy.misc.imread('bernie4.jpg',flatten=True),(120,80)).astype(float)
b5 = scipy.misc.imresize(scipy.misc.imread('bernie5.jpg',flatten=True),(120,80)).astype(float)
avg_bern = (b1+b2+b3+b4+b5)/5.0

k1 = scipy.misc.imresize(scipy.misc.imread('kim1.jpg',flatten=True),(120,80)).astype(float)
k2 = scipy.misc.imresize(scipy.misc.imread('kim2.jpg',flatten=True),(120,80)).astype(float)
k3 = scipy.misc.imresize(scipy.misc.imread('kim3.jpg',flatten=True),(120,80)).astype(float)
k4 = scipy.misc.imresize(scipy.misc.imread('kim4.jpg',flatten=True),(120,80)).astype(float)
k5 = scipy.misc.imresize(scipy.misc.imread('kim5.jpg',flatten=True),(120,80)).astype(float)
avg_kim = (k1+k2+k3+k4+k5)/5.0

def print_plots(sub1,sub2,pics):
    f, axarr = plt.subplots(sub1,sub2)
    for ax,pic in zip(axarr.ravel(),pics):
        ax.imshow(pic,cmap='gray')
        # Turn off tick labels
        ax.set_yticklabels([])
        ax.set_xticklabels([])
    plt.show()


pics1 = [c1,c2,c3,c4,c5,o1,o2,o3,o4,o5,t1,t2,t3,t4,t5,b1,b2,b3,b4,b5,k1,k2,k3,k4,k5]
# print_plots(5,5,pics1)
pics2 = [avg_clooney,avg_obama,avg_trump,avg_bern,avg_kim,avg_kim]
# print_plots(3,2,pics2)

def make_image_vector(image_list,new_size):
    D = np.empty([len(image_list),new_size])
    i=0
    for image in image_list:
        D[i,:] = image.reshape(1,new_size)
        i+=1
    return D

D = make_image_vector(pics1,120*80)
A = np.dot(D.transpose(),D)
vals,vecs = eigs(A,20,which='LM')
faces = [vecs[:,i].reshape(120,80).astype(float) for i in range(6)]
#print vals
#print vals[0].astype(float)/vals[1].astype(float)
#print_plots(3,2,faces)

vec_c = avg_clooney.reshape(1,120*80)
vec_o = avg_obama.reshape(1,120*80)
vec_t = avg_trump.reshape(1,120*80)
vec_b = avg_bern.reshape(1,120*80)
vec_k = avg_kim.reshape(1,120*80)


# np.dot(avg_clooney.reshape(1,120*80),vecs).astype(float)

def print_keys(people):
    f, axarr = plt.subplots(3,2)
    for ax, person in zip(axarr.ravel(),people):
        ax.bar(range(20)[1:],np.dot(person.reshape(1,120*80),vecs).astype(float)[0][1:])
    plt.show()

# print_keys(pics2)
# plt.bar(range(20),np.dot(avg_kim.reshape(1,120*80),vecs).astype(float)[0])

t1 = scipy.misc.imresize(scipy.misc.imread('testkim1.jpg',flatten=True),(120,80)).astype(float)
t2 = scipy.misc.imresize(scipy.misc.imread('testkourtney1.jpg',flatten=True),(120,80)).astype(float)
t3 = scipy.misc.imresize(scipy.misc.imread('testtaylor.jpg',flatten=True),(120,80)).astype(float)
t4 = scipy.misc.imresize(scipy.misc.imread('darrentest.jpg',flatten=True),(120,80)).astype(float)
test_pics = [t1,t2,t3,t4]

vect1 = t1.reshape(1,120*80)
vect2 = t2.reshape(1,120*80)
vect3 = t3.reshape(1,120*80)
vect4 = t4.reshape(1,120*80)

proj1 = np.dot(vect1,vecs)[0]
proj2 = np.dot(vect2,vecs)[0]
proj3 = np.dot(vect3,vecs)[0]
proj4 = np.dot(vect4,vecs)[0]

recon1 = np.dot(vecs,proj1).reshape(120,80)
recon2 = np.dot(vecs,proj2).reshape(120,80)
recon3 = np.dot(vecs,proj3).reshape(120,80)
recon4 = np.dot(vecs,proj4).reshape(120,80)
recons = [recon1,recon2,recon3,recon4]

def print_plots2(sub1,sub2,test_pics,recons,vecs):
    f, axarr = plt.subplots(sub1,sub2)
    for ax,pic in zip(axarr.ravel()[:4],test_pics):
        ax.imshow(pic,cmap='gray')
        # Turn off tick labels
        ax.set_yticklabels([])
        ax.set_xticklabels([])
    for ax, person in zip(axarr.ravel()[4:8], test_pics):
        ax.bar(range(20)[1:],np.dot(person.reshape(1,120*80),vecs).astype(float)[0][1:])
    for ax,pic in zip(axarr.ravel()[8:],recons):
        ax.imshow(pic.astype(float),cmap='gray')
        # Turn off tick labels
        ax.set_yticklabels([])
        ax.set_xticklabels([])
    plt.show()

projclooney = np.dot(avg_clooney.reshape(1,120*80),vecs)[0]
projobama = np.dot(avg_obama.reshape(1,120*80),vecs)[0]
projtrump = np.dot(avg_trump.reshape(1,120*80),vecs)[0]
projbern = np.dot(avg_bern.reshape(1,120*80),vecs)[0]
projkim = np.dot(avg_kim.reshape(1,120*80),vecs)[0]
avg_people = [projclooney,projobama,projtrump,projbern,projkim]

# print_plots2(3,4,test_pics,recons,vecs)


def print_similarity(test_image,avg_people):
    labels = ['clooney','obama','trump','bernie','kim']
    plt.bar(range(5),[np.linalg.norm(x-test_image) for x in avg_people],align='center')
    plt.xticks(range(5), labels)
    plt.show()

def who_do_i_look_like(test_image_jpg,vecs,avg_people):
    test = scipy.misc.imresize(scipy.misc.imread(test_image_jpg,flatten=True),(120,80)).astype(float)
    vec_test = test.reshape(1,120*80)
    proj_test = np.dot(vec_test,vecs)[0]
    labels = ['','clooney','obama','trump','bernie','kim']
    f, axarr = plt.subplots(2,2)
    axarr[0,0].imshow(test.astype(float),cmap='gray')
    axarr[0,1].bar(range(5),[np.linalg.norm(x-proj_test) for x in avg_people],align='center')
    axarr[0,1].set_xticklabels(labels)
    axarr[1,0].imshow(np.dot(vecs,proj_test).reshape(120,80).astype(float),cmap='gray')
    axarr[1,1].bar(range(20)[1:],np.dot(vec_test,vecs).astype(float)[0][1:])
    plt.show()

# who_do_i_look_like('doobietest.jpg',vecs,avg_people)
