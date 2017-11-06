from math import exp

def makeGuess(xValue, values):
    guess = values[0]
    guess += xValue + values[1]
    return 1.0 / (1.0 + exp(-guess))

rate = 0.1
epochs = 1000
values = [0, 1, 0, 1, 0, 1, 1, 1]
result = [0, 0]
prevSqrErrors = 0

print('training data to be evaluated:')
for x in range(len(values)):
    print(x + 1, values[x])

for epoch in range(epochs):
    sqrErrors = 0
    for x in values:
        guess = makeGuess(x + 1, result)
        error = values[x] - guess
        sqrErrors += error**2
        result[0] += rate * error * guess * (1.0 - guess)
        result[1] += rate * error * guess * (1.0 - guess) * (x  + 1)
    # print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, rate, sqrErrors))
    if sqrErrors == prevSqrErrors:
        print('Optimal found, discontinuing iteration after epoch %d' % epoch)
        break
    prevSqrErrors = sqrErrors
print('final weights:', result)
for x in range(len(values)):
    guess = makeGuess(x + 1, result)
    print('x value=%d, y=%d, prediction=%3f' % (x + 1, values[x], guess))


