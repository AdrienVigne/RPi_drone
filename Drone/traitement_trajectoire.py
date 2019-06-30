from numpy import sin,cos, arccos,arctan,pi,sqrt

class Trajectoire(object):
    """docstring for Trajectoire."""

    def __init__(self, longitude_base,latitude_base,altitude_base):
        super(Trajectoire, self).__init__()
        self.longitude_base = longitude_base
        self.latitude_base = latitude_base
        self.altitude_base = altitude_base
        self.rayon_terre = 6378137

        self.centre = (self.longitude_base*pi/180,self.latitude_base*pi/180)
        self.x0 = self.rayon_terre * cos(self.centre[0]) * cos(self.centre[1])
        self.y0 = self.rayon_terre * cos(self.centre[0]) * sin(self.centre[1])
        self.z0 = self.rayon_terre * sin(self.centre[0])
        self.phi = []
        self.theta = []


    def trajet(self,x_t,y_t,z_t):
        X = [self.x0+X for X in x_t]
        Y = [self.y0+Y for Y in y_t]
        Z = [self.z0+Z for Z in z_t]


        for i in range(len(X)):
            rho =sqrt( (X[i]**2)+(Y[i]**2)+(Z[i]**2))
            phi_temp = arccos(Z[i]/rho)*180/pi
            if phi_temp > 90 :
                phi_temp = 90 -phi_temp
            self.phi.append(phi_temp)
            self.theta.append(arctan(Y[i]/X[i])*180/pi)
        #print(self.theta,self.phi)
        return (self.theta,self.phi)
