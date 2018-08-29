
#1
#x=x0 + v0 t - v0 t0 + 0.5 a (t**2-2 t t0 + t0**2)
# =x0 - v0 t0 + 0.5 a t0**2  + v0 t - a t0 t  + 0.5 a t**2
# =x0 - v0 t0 + 0.5 a t0**2  + (v0 - a t0) t  + 0.5 a t**2
def x(x0,t0,v0,a):
    return poly1d([0.5*a,v0-a*t0,x0-v0*t0+0.5*a*t0**2],variable='t')

#2
x1=x(0,0,0,6)
x2=x(0,10,10,10)
print(x1)
print(x2)
t=np.linspace(0,45,100)
plt.title( r'meeting point: $t_{\rm fin}=%g$ m' %(  (x2-x1).r[0]  ),size=15 )
plt.plot(t,x2(t)-x1(t) )
plt.grid()
#plt.plot(t,(x2-x1)(t) )