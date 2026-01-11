# Faster Optimizer

Training a very large deep neural network can be painfully slow. So far we have seen four ways to speed up training (and reach a better solution): applying a good initialization strategy for the connection weights, using a good activation function, using Batch Normalization, and reusing parts of a pretrained network (possibly built on an auxiliary task or using unsupervised learning). Another huge speed boost comes from using a faster optimizer than the regular Gradient Descent optimizer.

---

In this section, we will present the most popular ones:
- Momentum optimization
- Nesterov Accelerated Gradient,
- AdaGrad
- RMSProp and
- Adam and Nadam optimization

---

# References

"Some methods of speeding up the convergence of iteration methods,” B. Polyak (1964)
