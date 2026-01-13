# Training Deep Neural Networks

We have learned how to train neural networks, but so far they were shallow, with only a few hidden layers. For very complex problems—such as recognizing many types of objects in high-resolution images—we often need much deeper neural networks with many layers and many neurons.

However, training deep neural networks is challenging for several reasons.

## Challenges

### 1. Vanishing or Exploding Gradients

- In deep networks, gradients can become too small or too large, making the earlier layers very difficult to train.

### 2. Limited Labeled Data

- Large neural networks require a large amount of labeled data, which can be expensive or difficult to obtain.

### 3. Slow Training

- Training very deep models with many parameters can take a long time.

### 4. Overfitting

- Models with millions of parameters can easily overfit the training data, especially when the dataset is small or noisy.

## What This Chapter Covers

In this chapter, each of these problems is explained step by step, along with practical techniques to solve them.  
The chapter covers:
- 🧠 Solutions to the vanishing or exploding gradients problem
- 🔁 Transfer learning and unsupervised pretraining for limited data
- ⚡ Advanced optimization methods that speed up training
- 🛡️ Regularization techniques to reduce overfitting

With these tools, training very deep neural networks becomes possible -- Welcome to Deep Learning! 🚀

<img width="489" height="353" alt="image" src="https://github.com/user-attachments/assets/e23d0368-fbb0-44ea-b3f5-789b728c9ede" />

## References

Xavier Glorot, Yoshua Bengio, 2010, https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf

How to deal: https://medium.com/dscier/how-to-deal-with-vanishing-and-exploding-gradients-in-neural-networks-24eb00c80e84

Vanishing & Exploding GD: https://medium.com/@venkatyogesh003/understanding-vanishing-and-exploding-gradients-in-deep-learning-61a5f38d1605

Glorot and He Initialization: https://medium.com/@sanjay_dutta/understanding-glorot-and-he-initialization-a-guide-for-college-students-00f3dfae0393
