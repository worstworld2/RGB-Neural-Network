r = 0
g = 0
b = 0

# Weights and biases for the neural network
w1 = 3.56
w2 = 8.49
w3 = 1.59
b1 = -6.67
w4 = 4.29
w5 = 8.36
w6 = 1.37
b2 = -6.34
w7 = 3.72
w8 = 8.13
w9 = 1.48
b3 = -6.11
w10 = 4.27
w11 = 3.66
w12 = 2.63
b4 = -5.47

# Input layer
def input_rgb():
    global r, g, b
    try:
        r = int(input("Enter Red value (0-255): "))
        g = int(input("Enter Green value (0-255): "))
        b = int(input("Enter Blue value (0-255): "))
    except ValueError:
        print("Please enter valid integer values for RGB.")
        return input_rgb()
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        return r, g, b
    else:
        print("Invalid RGB values. Please enter values between 0 and 255.")
        return input_rgb()
input_rgb()
x1 = r / 255
x2 = g / 255
x3 = b / 255

# Hidden layer
node1 = w1 * x1 + w2 * x2 + w3 * x3 + b1
node2 = w4 * x1 + w5 * x2 + w6 * x3 + b2
node3 = w7 * x1 + w8 * x2 + w9 * x3 + b3
# ReLU function
def ReLU(node1, node2, node3):
    if node1 < 0:
        node1 = 0
    if node2 < 0:
        node2 = 0
    if node3 < 0:
        node3 = 0
    return node1, node2, node3
node1, node2, node3 = ReLU(node1, node2, node3)

# Output layer
binary_output = w10 * node1 + w11 * node2 + w12 * node3 + b4
# Sigmoid function
def sigmoid(binary_output):
    import math
    return 1 / (1 + math.exp(-binary_output))
binary_output = sigmoid(binary_output)
binary_output = 1 if binary_output >= 0.5 else 0
if binary_output == 1:
    print("The RGB values represent a bright color.")
else:
    print("The RGB values represent a dark color.")