import numpy as np
import tkinter


def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1.0 - x)


class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.random.rand(self.input.shape[1], 4)
        self.weights2 = np.random.rand(4, 1)
        self.y = y
        self.output = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output),
                                                  self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def printoff(self):
        p = str(str(nn.output).split('\n')).replace("]", " ").replace("[", " ") \
            .replace(" ", "").replace("'", '').replace(",", ' ')
        q = p.split(' ')
        r = round(10 * float(q.pop(0).replace("'", ''))) / 10, \
            round(10 * float(q.pop(0).replace("'", ''))) / 10, \
            round(10 * float(q.pop(0).replace("'", ''))) / 10, \
            round(10 * float(q.pop(0).replace("'", ''))) / 10
        r = str(r).replace(")", '').replace("(", '').replace(",", "")
        print("Raw:\n" + p + "\n\n" + "Rounded:\n" + r)
        print("---------------------break---------------------")

        file = open("history.txt", "a")
        file.write("Raw:\n" + p + "\n\n" + "Rounded:\n" + r + "\n")
        file.write("---------------------break---------------------\n")
        file.close()
        return "Raw:\n" + p + "\n\n" + "Rounded:\n" + r


def buttonthing():


    label.config(text=nn.printoff())


if __name__ == "__main__":
    X = np.array([[0, 0.6, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    y = np.array([[0], [1], [0.9], [0]])
    nn = NeuralNetwork(X, y)

    for i in range(1500):
        nn.feedforward()
        nn.backprop()


root = tkinter.Tk()
root.title("Example")
root.geometry("450x158")
titleText = "Example:"
instructions = tkinter.Label(root, text=titleText, font=('Lucida Console', 12))
instructions.pack()


button = tkinter.Button(root, text='Return', command=buttonthing)
button.pack()

label = tkinter.Label(root, font=('Lucida Console', 11), wraplength=468, relief='sunken', width=45, height=6, anchor='w', justify='left')
label.pack()

root.mainloop()
