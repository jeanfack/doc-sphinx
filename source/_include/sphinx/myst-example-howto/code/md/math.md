The **Black-Scholes** formula (#Black-Scholes):

$$
	\mathrm C(\mathrm S,\mathrm t)= \mathrm N(\mathrm d_1)\mathrm S - \mathrm N(\mathrm d_2) \mathrm K \mathrm e^{-rt}
$$ (Black-Scholes)

$$
	\mathrm d_1= \frac{1}{\sigma \sqrt{\mathrm t}} \left[\ln{\left(\frac{S}{K}\right)} + t\left(r + \frac{\sigma^2}{2} \right) \right]
$$

$$
	\mathrm d_2= \frac{1}{\sigma \sqrt{\mathrm t}} \left[\ln{\left(\frac{S}{K}\right)} + t\left(r - \frac{\sigma^2}{2} \right) \right]
$$

$$
	N(x)=\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} \mathrm e^{-\frac{1}{2}z^2} dz
	\label{eq:5}
$$

The **Ornstein-Uhlenbeck** process [](#Ornstein-Uhlenbeck):

```{math}
:label: Ornstein-Uhlenbeck
dr_t = -\theta(r_t - \mu)dt + \sigma dW_t
```
