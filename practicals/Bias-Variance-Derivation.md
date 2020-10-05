For an estimate of the model parameters $\hat{\theta}$, its mean-squared error with respect to the true parameter set $\theta$ is given by:

$$\text{MSE}_{\theta} = \mathcal{E}\left\{(\hat{\theta} - \theta)^2\right\}$$
Where $\mathcal{E}$ is the expectation value operator.

This can be algebraically manipulated as follows:

$$\begin{matrix} \text{MSE}_{\theta} &=&  \mathcal{E}\left\{(\hat{\theta} - \theta)^2\right\} \\
&=& \mathcal{E}\left\{\hat{\theta}^T\hat{\theta} - 2\hat{\theta}^T{\theta} + \theta^T\theta\right\} \\
&=& \mathcal{E}\left\{\hat{\theta}^T\hat{\theta}\right\} - 2\mathcal{E}\left\{\hat{\theta}^T\theta\right\} + \mathcal{E}\left\{\theta^T\theta\right\} & \text{Using the linearity of } \mathcal{E} \\
&=& \mathcal{E}\left\{\hat{\theta}^T\hat{\theta}\right\} - 2 \theta^T\mathcal{E}\left\{\hat{\theta}\right\} + \theta^T\theta & \text{Because } \mathcal{E}\left\{\theta\right\} = \theta \end{matrix}$$


The variance of $\hat{\theta}$ is given by:
$$\begin{matrix}\text{Var}(\hat{\theta}) &=& \mathcal{E}\left\{\left(\mathcal{E}\{\hat{\theta}\}-\hat{\theta}\right)^2\right\} \\
&=& \mathcal{E}\left\{\mathcal{E}^2\{\hat{\theta}\}+\hat{\theta}^2 - 2\mathcal{E}\{\hat{\theta}\}\hat{\theta}\right\} \\
&=& \mathcal{E}^2\left\{\hat{\theta}\right\} + \mathcal{E}\left\{\hat{\theta}^2\right\} - 2\mathcal{E}\left\{\hat{\theta}\right\}\mathcal{E}\left\{\hat{\theta}\right\} & \text{Using linearity and idempotence of } \mathcal{E} \\
&=&\mathcal{E}\left\{\hat{\theta}^2\right\}-\mathcal{E}^2\left\{\hat{\theta}\right\} \\
&=& \mathcal{E}\left\{\hat{\theta}^T \hat{\theta}\right\}-\mathcal{E}^T\left\{\hat{\theta}\right\}\mathcal{E}\left\{\hat{\theta}\right\} & \text{In vector notation}\end{matrix}$$

The squared bias of $\hat{\theta}$ is given by:

$$\begin{matrix}\text{Bias}^2(\hat{\theta}) &=& \left(\mathcal{E}\{\hat{\theta}\}-\theta\right)^2 \\
&=& \mathcal{E}^T\left\{\hat{\theta}\right\}\mathcal{E}\left\{\hat{\theta}\right\} - 2\theta^T\mathcal{E}\left\{\hat{\theta}\right\} + \theta^T \theta & \text{In vector notation}   \end{matrix}$$

Summation of variance and squared bias yields:

$$\begin{matrix} \text{Var}(\hat{\theta}) + \text{Bias}^2(\hat{\theta}) &=& \mathcal{E}\left\{\hat{\theta}^T \hat{\theta}\right\}-\mathcal{E}^T\left\{\hat{\theta}\right\}\mathcal{E}\left\{\hat{\theta}\right\} + \mathcal{E}^T\left\{\hat{\theta}\right\}\mathcal{E}\left\{\hat{\theta}\right\} \\ &&- 2\theta^T\mathcal{E}\left\{\hat{\theta}\right\} + \theta^T \theta \\
&=& \mathcal{E}\left\{\hat{\theta}^T\hat{\theta}\right\} - 2 \theta^T\mathcal{E}\left\{\hat{\theta}\right\} + \theta^T\theta\end{matrix} $$

Which is equal to the mean squared error.