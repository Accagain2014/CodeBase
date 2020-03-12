## broadcasting
- A(n, 1) * B(m, ) => C(n, m)

## savez
vals_to_save = {key : value}
np.savez(npzFilename, **vals_to_save)
np.load('npzFilename.npz')[key]

