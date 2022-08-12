# %% Importing Libraries
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %% The Problem Definition-1
x0, y0 = 0, 5
step = np.array([5/2, 5/4, 5/8, 5/16, 5/32])
def f(x, y): return -x/y
def circle(x): return math.sqrt(5**2-x**2)

# %% The Problem Definition-2
# x0, y0 = 0, 2
# step = np.array([1])
# def f(x, y): return 4*(math.exp(0.8*x))-0.5*y


# %% Solution
error = np.array([])
for h in step:
    x = np.array([x0])
    y = np.array([y0])
    y_exact = np.array([y0])
    error_h = np.array([0])
    y_euler = np.array([y0])
    xi = h
    while xi <= 5:
        f0 = f(x[-1], y[-1])
        y_euler = np.append(y_euler, y[-1]+f(x[-1], y[-1])*h)
        f1 = f(xi, y_euler[-1])
        y = np.append(y, y[-1]+(f0+f1)*h/2)
        x = np.append(x, xi)
        y_exact = np.append(y_exact, circle(xi))
        error_h = np.append(error_h, abs(y[-1]-circle(xi)))
        if xi == 2.5:
            error = np.append(error, abs(y[-1]-circle(xi)))
        xi = xi+h
    # points = np.array([x, y])
    points = {'x': x, 'y_euler': y_euler, 'y_heun': y,
              'y_exact': y_exact, 'error@h': error_h}
    points = pd.DataFrame(points)
    print(points)
    plt.plot(x, y, '*-')
plt.xlim(0, 5)
plt.ylim(0, 5)

plt.title('Solution')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
ax = plt.gca()
ax.set_aspect('equal')
plt.show()

# %% Order of Convergence
# print(error)
# print(step)
logstep = np.log(step)
logerror = np.log(error)

slope = np.array([None])
logslope = np.array([None])
for i in range(len(step)-1):
    slope = np.append(slope, ((error[i+1]-error[i])/(step[i+1]-step[i])))
    logslope = np.append(
        logslope, ((logerror[i+1]-logerror[i])/(logstep[i+1]-logstep[i])))
# print(slope)
# print(logslope)
convergence = pd.DataFrame(
    {'step': step, 'error': error, 'slope': slope, 'logslope': logslope})
print(convergence)
plt.plot(step, error, '*-')
plt.plot(np.log(step), np.log(error), '*-')
plt.title('Global Convergence')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
ax = plt.gca()
ax.set_aspect('equal')
plt.show()

# %%
