from minigrad.nn import MLP
from minigrad.nn import mse_loss

xs = [[2.0, 3.0, -1.0],
      [3.0, -1.0, 0.5],
      [0.5, 1.0, 1.0],
      [1.0, 1.0, -1.0]]

ys = [1.0, -1.0, -1.0, 1.0]

#1 is the output layer.
model = MLP(3, [4, 4, 1])
epochs = 200

for i in range(epochs):
    #forward-pass
    #model only takes one input at a time rn
    out_pred = [model(x)[0] for x in xs]
    #mse loss
    loss = mse_loss(out_pred, ys)
    #zero the grad
    model.zero_grad()
    #backward on loss
    loss.backward()
    #update every param
    learning_rate = 0.01
    for p in model.parameters():
        p.val -= learning_rate * p.gradient
        
    print(f"epoch: {i}, loss:{loss}")
    print("\nfinal predictions: ")
    for x, target in zip(xs, ys):
        pred = model(x)[0]
        print(f"  target: {target:5.1f}  predicted: {pred.val:.4f}")
        