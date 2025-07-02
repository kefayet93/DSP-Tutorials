# Least Squares FIR Filter Design: Applications in DSP Wireless System Design

This repository contains Digital Signal Processing (DSP) algorithms implemented in Python. We begin with the implementation of a basic finite impulse response (FIR) filter using the Least-Squares (LS) estimation method to estimate the filter coefficients.

## What is Least-Squares FIR Filter Design?
Least Squares (LS)-based estimation is a method of estimating the frequency response of a discrete-time (DT) system. 
**The total channel (Tx + Channel + Rx) response can be modeled using a finite impulse response (FIR) filter: 

$$     y[n] = \sum\limits_{k = 0}^{L-1} h[k]. x[n-k] $$

In the above, $$x[n]$$, $$y[n]$$, and $$h[k]$$ represent known transmitted samples, captured received samples, and an FIR filter of length $$L$$, respectively. 
## Parameter Estimation
**Step 2: Preparing the input Convolution Matrix**

From the known input samples $$x[n]$$, we need to form the convolution matrix **X**:
* $$x$$ = $$[x[0], x[1], ..., x[N-1]]^T$$
* For an FIR filter of length $$L$$:
  
$$ [
\begin{pmatrix}
  x[L-1] & x{L-2}  & \cdots  & x[0] \\
  x{L}   & x[L-1]  & \cdots  & x[1] \\
  \vdots & \vdots  & \ddots  & \vdots \\
  x[N-1] & x[N-2]  & \cdots  & x[N-L]  \\
\end{pmatrix}
]$$
                       
## Importance in DSP and Wireless System Design
* **Channel Estimation:** estimating the channel impulse response of a multipath wireless channel and performing channel equalization at the receiver for phase, time, and carrier synchronization.
* **Channel Equalization:** estimating the inverse of the channel response to compensate for interference at the receiver, for example, compensating inter-symbol interference (ISI) in an orthogonal frequency division multiplexing (OFDM) receiver.
* **Echo Cancellation:** modeling transmitter leakage channel in full-duplex radios simultaneously transmitting and receiving (STAR) at the same frequency band, and cancelling self-interference (SI) signal at the digital baseband.
