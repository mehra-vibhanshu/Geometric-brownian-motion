# Geometric Brownian Motion Asset Price Simulator

A high-performance quantitative asset simulator built from scratch using Python. This engine structures simulations using parallel vector matrices to project multiple independent future timelines simultaneously, perfectly mirroring how modern risk-management platforms scale computational operations.

## Architectural Design & Matrix Structure

Unlike basic iterative loops that process one path at a time, this simulator allocates a static 2D memory grid utilizing **NumPy Vectorization**. 

* **Rows (Time Dimension):** Represents time flowing downward through 252 trading days in a year.
* **Columns (Path Dimension):** Represents 10 independent, concurrent market timelines running in parallel.

By executing the continuous compounding math across entire horizontal rows simultaneously, processing speeds are highly optimized for scaling across thousands of asset paths.

## Core Mathematics Applied

The engine relies on the continuous-time stochastic process of **Geometric Brownian Motion (GBM)**:

$$S_t = S_{t-1} \times e^{(\mu - 0.5\sigma^2)dt + \sigma Z \sqrt{dt}}$$

* **Drift ($\mu$):** The annualized expected asset growth rate (5% in this simulation), adjusted downward for volatility drag over time step $dt$.
* **Volatility ($\sigma$):** The annualized random stock price fluctuations (20% in this simulation).
* **Random Shock ($Z$):** A standard normal random variable $Z \sim N(0,1)$ generating daily market noise.

The use of Euler's constant ($e$) ensures that asset prices dynamically scale based on percentage returns and remain mathematically bounded above a floor of \$0 (stock prices cannot go below zero).

## 🛠️ Tech Stack & Dependencies

* **Python 3.14**
* **NumPy** (Vectorization & Multi-dimensional Matrix Operations)
* **Matplotlib** (Data Visualization)

## 📈 Sample Simulation Output

The resulting chart visualizes the log-normal distribution of potential market outcomes, mapping out both high-performing outlier timelines and baseline support levels over a full trading year.

![GBM Simulation Chart](gbm_simulation.png)

## 🔧 How to Run the Project Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/mehra-vibhanshu/geometric-Brownian-motion.git](https://github.com/mehra-vibhanshu/geometric-Brownian-motion.git)

2. pip install numpy matplotlib
