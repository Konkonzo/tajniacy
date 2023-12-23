import cv2
import numpy as np
def wyswietlanie(los):
    img_test = cv2.imread(r"hasla/1.png")
    y,x,ch=img_test.shape
    los = los+1
    print(los)
    holder = np.zeros((y,x,25))
    for id,i in enumerate(los):
        img = cv2.imread(r"hasla/"+str(i)+".png",cv2.IMREAD_GRAYSCALE)
        holder[:,:,id] = img
    conected= np.zeros((5*y,x,5))
    for wiersz in range(5):
        conected[:,:,wiersz] = np.concatenate((holder[:,:,5*wiersz],holder[:,:,5*wiersz+1],holder[:,:,5*wiersz+2],holder[:,:,5*wiersz+3],holder[:,:,5*wiersz+4]), axis=0)
    img_out=np.concatenate((conected[:,:,0],conected[:,:,1],conected[:,:,2],conected[:,:,3],conected[:,:,4]), axis=1)
    cv2.imwrite("plansza.jpg",img_out)
