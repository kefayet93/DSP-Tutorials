# Least Squares FIR Filter Design: Applications in DSP Wireless System Design

This repository contains Digital Signal Processing (DSP) algorithms implemented in Python. We start with the implementation of a basic finite impulse response (FIR) filter using Least-Squares (LS) estimation method for estimating the filter coefficients.

## What is Least-Squares FIR Filter Design?
** Least Squares (LS)-based estimation is a method of estimating the frequency response of a discrete-time (DT) system. 
**The total channel (Tx + Channel + Rx) response can be modeled using a finite impulse response (FIR) filter: 

$$     y[n] = \sum\limits_{k = 0}^{L-1} h[k]. x[n-k] $$

## Importance in DSP and Wireless System Design
* **Channel Estimation:** estimating the channel impulse response of a multipath wireless channel and performing channel equalization at the receiver for phase, time, and carrier synchronization.
* **Equalization:** 
