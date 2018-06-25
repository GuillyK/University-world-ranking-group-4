# Set up X as median room values and use Use vstack to make X two-dimensional
# Remember that X normally is (N,) instead of (N,1).
X = np.vstack(data['international_students'])

# Set up Y as the target price of the houses.
Y = data['international_outlook']

# Creating [X 1] (remember the useful np.ones function from the first notebook?)
X = np.vstack(data['international_students'])
X = np.column_stack((X, np.ones(X.shape[0])))

# Now get out m and b values for our best fit line
a, b = np.linalg.lstsq(X, Y)[0]
print(a, b)

f = figure(plot_width=600, plot_height=400)

# Create a scatter-plot
f.scatter(data["international_students"], data["international_outlook"])
    
# Create the line
x = data["international_students"]
f.line(x, a * x + b, color='red')

## Add some axis information
f.xaxis.axis_label = 'international_students'
f.yaxis.axis_label = "international_outlook"

show(f)

from sklearn.metrics import mean_squared_error
r = np.array(data["international_outlook"])
x = np.array(data["international_students"])
y = a * x + b
print(len(x))
smse = sum((r-y) **2) / len(x)
print(smse)
rmse = np.sqrt(smse)
print(rmse)


mse = mean_squared_error(r, y)
print(mse)