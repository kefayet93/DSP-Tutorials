# Least Squares FIR Filter Design: Applications in DSP Wireless System Design

This repository contains Digital Signal Processing (DSP) algorithms implemented in Python. We begin with the implementation of a basic finite impulse response (FIR) filter using the Least-Squares (LS) estimation method to estimate the filter coefficients.

## What is Least-Squares FIR Filter Design?
Least Squares (LS)-based estimation is a method of estimating the frequency response of a discrete-time (DT) system. 
**The total channel (Tx + Channel + Rx) response can be modeled using a finite impulse response (FIR) filter: 

$$     y[n] = \sum\limits_{k = 0}^{L-1} h[k]. x[n-k] $$

In the above, $$x[n]$$, $$y[n]$$, and $$h[k]$$ represent known transmitted samples, captured received samples, and FIR filter, respectively. 
## Parameter Estimation
**Step 1: Preparing the input Convolution Matrix**


## Importance in DSP and Wireless System Design
* **Channel Estimation:** estimating the channel impulse response of a multipath wireless channel and performing channel equalization at the receiver for phase, time, and carrier synchronization.
* **Channel Equalization:** estimating the inverse of the channel response to compensate for interference at the receiver, for example, compensating inter-symbol interference (ISI) in an orthogonal frequency division multiplexing (OFDM) receiver.
* **Echo Cancellation:** modeling transmitter leakage channel in full-duplex radios simultaneously transmitting and receiving (STAR) at the same frequency band, and cancelling self-interference (SI) signal at the digital baseband.
