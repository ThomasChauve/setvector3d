import numpy as np
from scipy.stats import gaussian_kde

class setvector3d(object):
    '''
    Object to work on a set of 3d unit vector
    '''
    
    pass

    def __init__(self,data):
        '''
        :param data: data is an array of dimention 3
        :type data: np.array
        '''
        
        if np.shape(data)[1] !=3:
            print('Your array should have 3 columns X,Y,Z')
            
        
        norm_data=np.linalg.norm(data,axis=1)
        id=np.where(norm_data!=1)
        data = np.float64(data)
        for i in list(range(len(id[0]))):
            if i==0:
                print('Normalising vector length to 1')
            data[id[0][i],:]=data[id[0][i],:]/norm_data[id[0][i]]
        
        
        self.vector=data
        
        
        
        def OrientationTensor2nd(self):
            '''
            Compute the normelized second order orientation tensor
            :return eigvalue: eigen value w[i]
            :rtype eigvalue: np.array
            :return eigvector: eigen vector v[:,i]
            :rtype eigvector: np.array
            :note: eigen value w[i] is associate to eigen vector v[:,i] 
            '''
            a11 = np.float32(np.nanmean(np.float128(np.multiply(self.vector[:,0],self.vector[:,0]))))
            a22 = np.float32(np.nanmean(np.float128(np.multiply(self.vector[:,1],self.vector[:,1]))))
            a33 = np.float32(np.nanmean(np.float128(np.multiply(self.vector[:,3],self.vector[:,3]))))
            a12 = np.float32(np.nanmean(np.float128(np.multiply(self.vector[:,0],self.vector[:,1]))))
            a13 = np.float32(np.nanmean(np.float128(np.multiply(self.vector[:,0],self.vector[:,2]))))
            a23 = np.float32(np.nanmean(np.float128(np.multiply(self.vector[:,1],self.vector[:,2]))))
            
            Tensor=np.array([[a11, a12, a13],[a12, a22, a23],[a13, a23, a33]])
            eigvalue,eigvector=np.linalg.eig(Tensor)
            
            return eigvalue,eigvector
        
        
        def stereoplot(self):
            '''
            Plot a stereographic projection of the vector
            '''
            
            # Project the vector in the plan of the stereographic projection
            LpL=1./(1.+self.vector[:,2])
            xx=LpL*self.vector[:,0]
            yy=LpL*self.vector[:,1]
            xy = np.vstack([xx,yy])
            z = gaussian_kde(xy)(xy)
            # Prepare the contour plot
            Zc = mlab.griddata(xx, yy, xmin[:,j], xi, yi, interp='linear')
            plt.figure(figsize=(10,10),dpi=160)
            plt.imshow(Zc.data,extent=(-1,1,-1,1))
            plt.colorbar(orientation='vertical',aspect=4,shrink=0.5)
            # compute a 3 circle
            for i in [0.,30.,60.]:
                omega = np.linspace(0, 2*np.pi, 1000)
                x_circle = 1./(1.+np.sin(i*np.pi/180.))*np.cos(i*np.pi/180.)*np.cos(omega)
                y_circle = 1./(1.+np.sin(i*np.pi/180.))*np.cos(i*np.pi/180.)*np.sin(omega)
                if i==0:
                    plt.plot(x_circle, y_circle,'k', linewidth=3)
                else:
                    plt.plot(x_circle, y_circle,'k', linewidth=1.5)
                    plt.text(x_circle[200], y_circle[300]+0.04,'$\phi$='+str(90.-i)+'°')
            
            # plot Theta line
            plt.plot([0,0],[-1,1],'k', linewidth=1.5)
            plt.text(1-0.15, 0+0.04,'$\Theta$=0°')
            plt.text(-1+0.1, 0-0.06,'$\Theta$=180°')
            plt.plot([-1,1],[0,0],'k', linewidth=1.5)
            plt.text(-0.16, 1-0.25,'$\Theta$=90°')
            plt.text(0.01, -1+0.15,'$\Theta$=270°')
            plt.plot([-0.7071,0.7071],[-0.7071,0.7071],'k', linewidth=1.5)
            plt.plot([-0.7071,0.7071],[0.7071,-0.7071],'k', linewidth=1.5)
            
            
            # draw a cross for x and y direction
            plt.plot([1, 0],[0, 1],'+k',markersize=12)
            # write axis
            plt.text(1.05, 0, r'X')
            plt.text(0, 1.05, r'Y')
            plt.axis('equal')
            plt.axis('off')